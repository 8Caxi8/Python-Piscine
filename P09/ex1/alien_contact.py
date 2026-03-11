from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError as Pe
from enum import Enum
from datetime import datetime
import json


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_contact_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise Pe("invalid_contact_id_error",
                     "Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise Pe("physical_notverified_error",
                     "Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise Pe("telepathic_witness_error",
                     "Telepathic contact "
                     "requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise Pe("singal_strength_no_message_error",
                     "Strong signals (>7.0) "
                     "should include received messages")

        return self


def display_contact(contact: AlienContact) -> None:
    print("=" * 40)
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'\n")
    else:
        print()
    print("=" * 40)


def generated_data() -> None:
    with open("alien_contacts.json") as f:
        data = json.load(f)

    for entry in data:
        try:
            display_contact(AlienContact.model_validate(entry))
        except ValidationError as e:
            print("Expected validation error:")
            for error in e.errors():
                print(error['msg'])


def custom_data() -> None:
    try:
        display_contact(AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime(2024, 1, 15, 8, 30),
                location="Area 51, Nevada",
                contact_type=ContactType.RADIO,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received="Greetings from Zeta Reticuli",
            )
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])

    try:
        display_contact(AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime(2024, 1, 15, 8, 30),
                location="Area 51, Nevada",
                contact_type=ContactType.TELEPATHIC,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=2,
                message_received="Greetings from Zeta Reticuli",
            )
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])


def main() -> None:
    print("Alien Contact Log Validation")

    try:
        generated_data()
    except FileNotFoundError:
        custom_data()


if __name__ == "__main__":
    main()
