from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
import json


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    status = "Operational" if station.is_operational else "Offline"

    print("=" * 40)
    print("Valid Station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}\n")
    print("=" * 40)


def generated_data() -> None:
    with open("space_stations.json") as f:
        data = json.load(f)

    for entry in data:
        try:
            display_station(SpaceStation.model_validate(entry))
        except ValidationError as e:
            print("Expected validation error:")
            for error in e.errors():
                print(error['msg'])


def custom_data() -> None:
    try:
        display_station(SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime(2024, 1, 15, 8, 30),
                notes="All systems nominal.",
            )
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])

    try:
        display_station(SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=21,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime(2024, 1, 15, 8, 30),
                notes="All systems nominal.",
            )
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])


def main() -> None:
    print("Space Station Data Validation")

    try:
        generated_data()
    except FileNotFoundError:
        custom_data()


if __name__ == "__main__":
    main()
