def ft_count_harvest_iterative() -> None:
    d: int = int(input("Days until harvest: "))
    for i in range(1, d + 1):
        print("Day", i)
    print("Harvest time!")
