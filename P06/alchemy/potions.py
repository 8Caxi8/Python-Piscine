from . import elements as el


def healing_potion() -> str:
    return (f"Healing potion brewed with {el.create_fire()} "
            f"and {el.create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {el.create_earth()} "
            f"and {el.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {el.create_air()} "
            f"and {el.create_water()}")


def wisdom_potion() -> str:
    four_results = [
        el.create_fire(), el.create_water(),
        el.create_earth(), el.create_air()
    ]

    return (f"Wisdom potion brewed with all elements: "
            f"{' and '.join(four_results)}")
