import time
import functools
import random
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) \
                -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def verify_power(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[-1]
            if (power >= min_power):
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper
    return verify_power


def retry_spell(max_attempts: int) \
                    -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def spell(func: Callable[..., Any]) -> Callable[..., Any]:
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
    time.sleep(0.101)


@power_validator(min_power=10)
def sleep(power: int) -> str:
    return "Creating a sleeping spell"


@power_validator(min_power=20)
def ice_storm(power: int) -> str:
    return "Creating an ice storm"


@retry_spell(max_attempts=5)
def trying_power() -> str:
    if (random.random() < .8):
        raise ValueError
    else:
        return "Power was successful!"


def main() -> None:

    print("\nTesting spell timer...")
    fireball()
    print("Result: Fireball cast!")

    print("\nTesting power validator...")
    print(sleep(5))
    print(ice_storm(25))

    print("\nTesting retry spell...")
    print(trying_power())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Dan Simoe   "))
    print(guild.validate_mage_name("Dan  #"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Ice ray", 0))


if __name__ == "__main__":
    main()
