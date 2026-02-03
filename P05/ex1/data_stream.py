from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union, Set


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self._stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        filtered: List[Any] = []

        if not criteria:
            return data_batch

        for item in data_batch:
            if ":" in str(item):
                key, value = item.split(":")
                if criteria == key:
                    filtered.append(item)

            else:
                if criteria == item:
                    filtered.append(item)

        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"size": str(self._batch_size)}


class SensorStream(DataStream):
    _stats: List[str] = ["temp", "humidity", "pressure"]
    _filters: Set[str] = ["low_temp"]

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._type: str = "Enviromental Data"
        self._data: list[tuple[str, float]] = []
        self._stats: Dict[str, Union[str, float]] = {}

        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self._stream_id}, Type: {self._type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        self._batch_size: int = len(data_batch)

        try:
            for item in data_batch:
                key, value = item.split(":")
                self._data.append((key, float(value)))
        except ValueError as e:
            return ValueError(f"Invalid data format: {e}")

        result = ", ".join(
            f"{key}:{value:g}" for key, value in self._data
        )

        self._stats = self.get_stats()
        return (
            f"Processing sensor batch: [{result}]\n"
            f"Sensor analysis: {self._stats["size"]}, "
            f"avg temp: {self._stats["avg_temp"]}ºC\n"
        )

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        filtered: List[Any] = []
        if criteria is None:
            return data_batch

        filtered = super().filter_data(data_batch, criteria)

        if criteria in self._filters:
            try:
                for item in data_batch:
                    key, value = item.split(":")
                    value_float: float = float(value)

                    if (
                        criteria == "low_temp"
                        and key == "temp"
                        and float(value) < 10
                    ):
                        filtered.append((key, value_float))

            except ValueError as e:
                raise ValueError(f"Invalid data format: {e}")

        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["size"] += " readings processed"

        temps = [value for key, value in self._data if key == "temp"]
        stats["avg_temp"] = sum(temps) / len(temps) if temps else 0.0

        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: int):
        super().__init__(stream_id)
        self._type: str = "Financial Data"
        self._data: list[tuple[str, int]] = []
        self._stats: Dict[str, Union[str, int]] = {}

        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self._stream_id}, type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self._batch_size: int = len(data_batch)

        try:
            for item in data_batch:
                key, value = item.split(":")
                self._data.append((key, int(value)))
        except ValueError as e:
            return ValueError(f"Invalid data format: {e}")

        result = ", ".join(
            f"{key}:{value:g}" for key, value in self._data
        )

        self._stats = self.get_stats()
        return (
            f"Processing transaction batch: [{result}]\n"
            f"Transaction analysis: {self._stats["size"]}, "
            f"net flow: {self._stats["net_flow"]:+d} units\n"
        )

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch

        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["size"] += " operations processed"

        income = [value for key, value in self._data if key == "buy"]
        outcome = [value for key, value in self._data if key == "sell"]

        stats["net_flow"] = sum(income) - sum(outcome)

        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: int):
        super().__init__(stream_id)
        self._type: str = "Financial Data"
        self._data: list[str] = []
        self._stats: Dict[str, Union[str, int]] = {}

        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self._stream_id}, type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        self._batch_size: int = len(data_batch)
        events: Set[str] = {"login", "error", "warning", "logout"}

        try:
            for item in data_batch:
                if item in events:
                    self._data.append(item)
                else:
                    raise ValueError(f"'{item}' is not a possible event.")
        except ValueError as e:
            return ValueError(f"Invalid data format: {e}")

        result: str = ", ".join(
            f"{value}" for value in self._data
        )

        self._stats = self.get_stats()
        return (
            f"Processing event batch: [{result}]\n"
            f"Event analysis: {self._stats["size"]}, "
            f"{self._stats["error"]} error detected\n"
        )

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch

        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[int, str]] = super().get_stats()
        stats["size"] += " events processed"

        errors: List = [value for value in self._data if value == "error"]

        stats["error"] = len(errors)

        return stats


class StreamProcessor:
    def __init__(self, batch_streams: List[DataStream]) -> None:
        self._batch_streams: List[DataStream] = batch_streams
        print("Processing mixed stream types through unified interface...\n")

    def batch_process(self) -> None:
        for stream in self._batch_streams:
            operations = stream.get_stats()
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {operations['size']}")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {operations['size']}")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {operations['size']}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor: SensorStream = SensorStream("SENSOR_001")
    print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))

    trans: TransactionStream = TransactionStream("TRANS_001")
    print(trans.process_batch(["buy:100", "sell:150", "buy:75"]))

    event: EventStream = EventStream("EVENT_001")
    print(event.process_batch(["login", "error", "logout"]))

    print("=== Polymorphic Stream Processing ===")
    processor: StreamProcessor = StreamProcessor([sensor, trans, event])
    print("Batch 1 Results:")
    processor.batch_process()

    print()
    print("Stream filtering active: High-priority data only")
    sensor_filtered: List[Any] = sensor.filter_data(
        ["temp:5", "humidity: 70", "temp: 25", "temp: 2"],
        "low_temp",
        )
    trans_filtered: List[Any] = trans.filter_data(
        ["buy:100", "sell:150", "buy:75"],
        "sell",
    )
    print("Filtered results: ",
          f"{len(sensor_filtered)} critical sensor alerts ",
          f"{len(trans_filtered)} large transaction\n",
          )

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
