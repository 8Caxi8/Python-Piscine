def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifacts: artifacts["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: str("*" + spell + "*"), spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": sum(map(lambda mage: mage["power"], mages)) / len(mages),
    }


def main() -> None:
    artifacts = [{'name': 'Ice Wand', 'power': 71, 'type': 'relic'}, {'name': 'Shadow Blade', 'power': 106, 'type': 'weapon'}, {'name': 'Crystal Orb', 'power': 93, 'type': 'relic'}, {'name': 'Light Prism', 'power': 117, 'type': 'focus'}]
    mages = [{'name': 'Luna', 'power': 62, 'element': 'lightning'}, {'name': 'Alex', 'power': 94, 'element': 'earth'}, {'name': 'Ash', 'power': 74, 'element': 'fire'}, {'name': 'Riley', 'power': 99, 'element': 'fire'}, {'name': 'Kai', 'power': 58, 'element': 'light'}]
    spells = ['heal', 'shield', 'freeze', 'meteor']

    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifacts))
    print("\nTesting power filtering...")
    print(power_filter(mages, 75))
    print("\nTesting spell transformer...")
    print(spell_transformer(spells))
    print("\nTesting mage stats calculation...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
