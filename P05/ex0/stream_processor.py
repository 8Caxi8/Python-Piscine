from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return "Output:"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if isinstance(data, list):
            numbers: List[float] = [float(x) for x in data]
        else:
            numbers: List[float] = [float(data)]

        no: int = len(numbers)
        total: float = sum(numbers)
        avg: float = total / no if no > 0 else 0
        return f"Processed {no} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, list):
                for value in data:
                    float(value)
            else:
                float(data)
        except (ValueError, TypeError):
            return False

        print("Validation: Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return f"{super().format_output(result)} {result}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        characters: int = len(str(data))
        words: int = len(str(data).split())
        return f"Processed text: {characters} characters, {words} words."

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False

    def format_output(self, result: str) -> str:
        return f"{super().format_output(result)} {result}"


class LogProcessor(DataProcessor):
    levels: set[str] = {
            "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL",
        }

    def process(self, data: Any) -> str:
        parts: List[str] = data.split(":", 1)
        level: str = parts[0].strip().upper()
        message: str = parts[1].strip()

        if level in {"WARNINR", "ERROR", "CRITICAL"}:
            level_type: str = "ALERT"
        else:
            level_type = level

        return f"[{level_type}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        try:
            parts: List = data.split(":", 1)
            level = parts[0].strip().upper()
            if level not in self.levels:
                return False
        except (ValueError, IndexError):
            return False

        print("Validation: Log entry verified")
        return True

    def format_output(self, result: str) -> str:
        base = super().format_output(result)
        return f"{base} {result}"


def run(processor: DataProcessor, data: Any) -> None:
    print(f"Processing data: {data}")
    print(processor.format_output(processor.process(data)))
    print()


def polymorphic_demo() -> None:
    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    inputs: List[Any] = [
        [1, 2, 3],
        "System ready",
        "INFO: System ready",
    ]

    for i, (p, d) in enumerate(zip(processors, inputs), 1):
        print(f"Result {i}: {p.process(d)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
    print()


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_data: list[int] = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    if NumericProcessor().validate(num_data):
        run(NumericProcessor(), num_data)

    txt_data: str = "Hello Nexus World"
    print("Initializing Text Processor...")
    if TextProcessor().validate(txt_data):
        run(TextProcessor(), txt_data)

    log_data: str = "ERROR: Connection timeout"
    print("Initializing Log Processor...")
    if LogProcessor().validate(log_data):
        run(LogProcessor(), log_data)

    print("=== Polymorphic Processing Demo ===")
    polymorphic_demo()


if __name__ == "__main__":
    main()
