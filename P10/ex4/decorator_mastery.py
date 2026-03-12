import time
import functools
import random


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        return func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")

    return wrapper


def power_validator(min_power: int) -> callable:
    def verify_power(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], (int, float)):
                power = args[1]
            else:
                power = args[0]
            if (power >= min_power):
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper
    return verify_power


def retry_spell(max_attempts: int) -> callable:
    def spell(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")
        return wrapper
    return spell


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for letter in name:
                if not (letter.isalpha() or letter.isspace()):
                    return False
            return True
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> None:
    time.sleep(0.5)


@power_validator(min_power=10)
def sleep(power, target, **kwargs) -> str:
    return f"Sleeping {target}"


@power_validator(min_power=20)
def ice_storm(power, target, **kwargs) -> str:
    return f"Creating an ice storm in {target}"


@retry_spell(max_attempts=5)
def trying_power() -> None:
    if (random.random() < .8):
        raise ValueError
    else:
        return "Power was successful!"


def main() -> None:

    print("\nTesting spell timer...")
    fireball()
    print("Result: Fireball cast!")

    print("\nTesting power validator...")
    print(sleep(5, "King Dwarf"))
    print(ice_storm(25, "Allies"))

    print("\nTesting retry spell...")
    print(trying_power())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Dan Simoe   "))
    print(guild.validate_mage_name("Dan  #"))
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(0, "Ice ray"))


if __name__ == "__main__":
    main()
