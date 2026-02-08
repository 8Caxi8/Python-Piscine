import time
from typing import Generator, Any


def event_stream(events: list[dict[str, Any]]) -> Generator[
                                                dict[str, Any], None, None]:
    for event in events:
        yield event


def data_stream(data: list[dict[str, Any]]) -> None:
    event_count: dict[str, int] = {}
    event_type: str
    high_level: int = 0
    total_events: int = 0
    start: float = time.perf_counter()

    for log in event_stream(data):
        event_type = log["event_type"]
        event_count[event_type] = event_count.get(event_type, 0) + 1
        if log["data"]["level"] >= 10:
            high_level += 1
        total_events += 1

    print(f"Total events processed: {total_events}")
    print(f"High_level players (10+): {high_level}")
    for key, value in event_count.items():
        if key == "item_found":
            print(f"Treasure events: {value}")
        if key == "level_up":
            print(f"Level-up events: {value}")
    print()

    end: float = time.perf_counter()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {(end - start):.03f}\n")


def data_store(data: list[dict[str, Any]]) -> None:
    storage: list[dict[str, Any]] = []
    event_count: dict[str, int] = {}
    event_type: str
    high_level: int = 0
    total_events: int = 0

    for log in event_stream(data):
        storage.append(log)

    for log in storage:
        event_type = log["event_type"]
        event_count[event_type] = event_count.get(event_type, 0) + 1
        if log["data"]["level"] >= 10:
            high_level += 1
        total_events += 1


def processing_events(events: list[dict[str, Any]]) -> None:
    print(f"Processing {len(events)} game events...\n")

    for i, event in zip(range(1, 4), events):
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['data']['level']})", end=" ")
        if event["event_type"] == "kill":
            print("killed monster")
        elif event["event_type"] == "level_up":
            print("leveled up")
        elif event["event_type"] == "login":
            print("logged in")
        elif event["event_type"] == "death":
            print("died")
        elif event["event_type"] == "item_found":
            print("found treasure")
        else:
            print(event["event_type"])
    print("...\n")


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


def prime_generator() -> Generator[int, None, None]:
    num: int = 2

    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

        num += 1


def run_generator(generate: str) -> None:
    if generate == "fibonacci":
        fib = fibonacci_generator(10)
        print("Fibonacci sequence (first 10):",
              ", ".join(str(num) for num in fib))

    elif generate == "prime":
        prime = prime_generator()
        print("Prime numbers (first 5):", end=" ")
        for i in range(5):
            if i < 4:
                print(next(prime), end=", ")
            else:
                print(next(prime))


def main() -> None:
    events: list[dict[str, Any]] = []
    print("=== Game Data Stream Processor ===\n")

    processing_events(events)

    print("=== Stream Analytics ===")
    data_stream(events)

    data_store(events)

    print("=== Generator Demonstration ===")
    run_generator("fibonacci")
    run_generator("prime")


if __name__ == "__main__":
    main()
