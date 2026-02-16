from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class defining the interface for all data processors.

    Subclasses must implement validate and process
    for specific data types.
    """
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate whether the provided data is suitable
        for this processor.
        """
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the provided data and return a result string.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the processed result for display
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor specialized for numeric data.

    Handles single numeric values or lists of numbers and computs
    summary statistics.
    """
    def process(self, data: Any) -> str:
        """
        Calculate count, sum, and average of numeric data
        """
        if isinstance(data, list):
            numbers = [float(x) for x in data]
        else:
            numbers = [float(data)]

        no: int = len(numbers)
        total: float = sum(numbers)
        avg: float = total / no if no > 0 else 0
        return f"Processed {no} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        """
        Ensure data can be converted to float values
        """
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
        return f"{super().format_output(result)}"


class TextProcessor(DataProcessor):
    """
    Processor specialized for text data.

    Computes characters and word statistics.
    """
    def process(self, data: Any) -> str:
        """
        Count characters and words in text.
        """
        characters: int = len(str(data))
        words: int = len(str(data).split())
        return f"Processed text: {characters} characters, {words} words."

    def validate(self, data: Any) -> bool:
        """
        Validate that data is a string.
        """
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False

    def format_output(self, result: str) -> str:
        return f"{super().format_output(result)}"


class LogProcessor(DataProcessor):
    """
    Processor specialized for structured log entries.

    Expects log format: 'Level: message'
    """
    levels: set[str] = {
            "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL",
        }

    def process(self, data: Any) -> str:
        """
        Extract log level and message and categorize severity.
        """
        parts: List[str] = data.split(":", 1)
        level: str = parts[0].strip().upper()
        message: str = parts[1].strip()

        if level in {"WARNING", "ERROR", "CRITICAL"}:
            level_type: str = "ALERT"
        else:
            level_type = level

        return f"[{level_type}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        """
        Validate that log entry contains a recognized log level.
        """
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
        return f"{super().format_output(result)}"


def run(processor: DataProcessor, data: Any) -> None:
    """
    Execute validation, processing, and formatting.
    for a given processor instance.
    """
    print(f"Processing data: {data}")
    print(processor.format_output(processor.process(data)))
    print()


def polymorphic_demo() -> None:
    """
    Demonstrate polymorphic behavior by processing
    different data types through the same interface.
    """
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
        result = p.process(d)
        print(f"Result {i}: {p.format_output(result)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


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
