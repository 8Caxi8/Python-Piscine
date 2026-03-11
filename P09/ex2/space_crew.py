from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError as Pe
from enum import Enum
from datetime import datetime
import json
import sys


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name:  str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization:  str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status:  str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    def _crew_experience(self) -> float:
        experienced = [crew_member for crew_member in self.crew
                       if crew_member.years_experience >= 5]

        return len(experienced) / len(self.crew)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise Pe("mission_id_error",
                     "Mission ID must start with 'M'")
        if not [crew_member.rank for crew_member in self.crew
                if crew_member.rank in (Rank.COMMANDER, Rank.CAPTAIN)]:
            raise Pe("without_commandar_captain",
                     "Mission must have at least one Commander or Captain")
        if self.duration_days > 365 and self._crew_experience() < 0.5:
            raise Pe("long_mission_experienced",
                     "Long missions (> 365 days) need 50% "
                     "experienced crew (5+ years)")
        for crew_member in self.crew:
            if not crew_member.is_active:
                raise Pe("crew_member_inactive",
                         "All crew members must "
                         "be active")

        return self


def display_spacemission(mission: SpaceMission) -> None:
    print("=" * 40)
    print("Valid mission created:")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days}")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for crew_member in mission.crew:
        print(f"- {crew_member.name} ({crew_member.rank.value}) "
              f"- {crew_member.specialization}")
    print("=" * 40)


def main() -> None:
    print("Space Mission Crew Validation")

    try:
        with open("space_missions.json") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    for entry in data:
        try:
            display_spacemission(SpaceMission.model_validate(entry))
        except ValidationError as e:
            print("Expected validation error:")
            for error in e.errors():
                print(error['msg'])


if __name__ == "__main__":
    main()
