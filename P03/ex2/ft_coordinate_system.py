import math


class CoordError(Exception):
    pass


def parse_coordinates(parsed_coordinates: str) -> tuple[int, int, int]:
    coordinates: tuple[int, int, int]

    print(f'Parsing coordinates: "{parsed_coordinates}"')
    coordinates = tuple(coordinates_check(parsed_coordinates))
    print(f"Parsed position: {coordinates}")

    return coordinates


def coordinates_check(parsed_coordinates: str) -> list[int]:
    list_coordinates: list[str] = parsed_coordinates.split(",")
    coordinates: list[int] = []

    if len(list_coordinates) != 3:
        raise CoordError("Error: Three coordinates needed: 'x,y,z'")

    for coord in list_coordinates:
        try:
            coordinates.append(int(coord))
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            raise CoordError(f"Error details - Type: {type(e).__name__}, "
                             f"Args: {e.args}")

    return coordinates


def get_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    return math.dist(p1, p2)


def unpack_coordinates(coordinates: tuple[int, int, int]) -> None:
    print("Unpacking demonstration:")
    print(f"Player at x={coordinates[0]}, y={coordinates[1]},"
          f" z={coordinates[2]}")

    x: int
    y: int
    z: int
    (x, y, z) = coordinates

    print(f"Coordinates: X={x}, Y={y}, Z={z}\n")


def create_position() -> None:
    position = (10, 20, 5)
    print(f"Position created: {position}")

    origin = (0, 0, 0)
    distance = get_distance(origin, position)
    print(f"Distance between {origin} and {position}: {distance:.2f}\n")


def parsing(parsed_coordinates: str) -> None:
    origin = (0, 0, 0)

    try:
        coordinates = parse_coordinates(parsed_coordinates)
        distance = get_distance(origin, coordinates)
        print(f"Distance between {origin} and {coordinates}: {distance:.2f}\n")
    except CoordError as e:
        print(e)
        print()


def main() -> None:
    print("=== Game Coordinate System ===\n")
    create_position()

    parsing("3,4,0")

    parsing("abc,def,ghi")

    unpack_coordinates((3, 4, 0))


if __name__ == "__main__":
    main()
