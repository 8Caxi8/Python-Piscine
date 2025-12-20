def ft_count_harvest_recursive(i: int = 0, d: int = 0) -> None:
    if not d and not i:
        d = int(input("Days until harvest: "))
    if not d:
        print("Harvest time!")
        return
    print("Day", i + 1)
    ft_count_harvest_recursive(i + 1, d - 1)
