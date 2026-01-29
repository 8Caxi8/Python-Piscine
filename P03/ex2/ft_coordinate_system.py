import sys
import math


def parse_coordinates() -> tuple[int]:
    if len(sys.argv) == 1 or len(sys.argv) > 2 or len(sys.argv[1]) == 0:
        print("Error: One coordinate tuple needed: "
              'python3 ft_coordinate_system.py "x,y,z"\n')
        return

    coordinates = tuple(get_coordinates(sys.argv[1].split(",")))
    if not coordinates:
        return
    print(f'Parsing coordinates: "{sys.argv[1]}"')
    print(f"Parsed position: {coordinates}")
    return coordinates


def get_coordinates(imput: list[str]) -> list[int]:
    coordinates: list[int] = []

    i: int = 0
    for coord in imput:
        if i >= 3:
            print("Error: One coordinate tuple needed: "
                  'python3 ft_coordinate_system.py "x,y,z"\n')
            return []
        try:
            coordinates.append(int(coord))
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f'Error details - Type {type(e).__name__}, Args: {e.args}\n')
            return []
        i += 1
    if i < 3:
        print("Error: One coordinate tuple needed: "
              'python3 ft_coordinate_system.py "x,y,z"\n')
        return []
    return coordinates


def get_discance(p1: tuple[int], p2: tuple[int]) -> float:
    return float(math.sqrt((p1[0] - p2[0])**2 +
                           (p1[1] - p2[1])**2 +
                           (p1[2] - p2[2])**2))


def unpack_coordinates(coordinates: tuple[int]) -> None:
    print("Unpacking demonstration:")
    print(f"Player at x={coordinates[0]}, y={coordinates[1]},"
          f" z={coordinates[2]}")

    x: int
    y: int
    z: int
    (x, y, z) = coordinates

    print(f"Coordinates: X={x}, Y={y}, Z={z}\n")


def create_position() -> None:
    position = tuple([10, 20, 5])
    print(f"Position created: {position}")

    origin = tuple(get_coordinates("000"))
    distance = get_discance(origin, position)
    print(f"Distance between {origin} and {position}: {distance:.2f}\n")


def coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")

    create_position()

    coordinates: tuple[int] = parse_coordinates()

    origin = tuple(get_coordinates("000"))
    distance = get_discance(origin, coordinates)
    print(f"Distance between {origin} and {coordinates}: {distance:.2f}\n")

    unpack_coordinates(coordinates)


if __name__ == "__main__":
    coordinate_system()
