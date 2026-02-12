from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union, Set


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self._stream_id: str = stream_id
        self._batch_size: int = 0

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

    @abstractmethod
    def format_output(self) -> str:
        pass


class SensorStream(DataStream):
    # _stats: List[str] = ["temp", "humidity", "pressure"]
    _filters: Set[str] = {"low_temp"}

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._type: str = "Sensor data"
        self._data: list[tuple[str, float]] = []

        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self._stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self._batch_size = len(data_batch)

        try:
            for item in data_batch:
                key, value = item.split(":")
                self._data.append((key, float(value)))
        except ValueError as e:
            raise ValueError(f"Invalid data format: {e}\n")

        self._result = ", ".join(
            f"{key}:{value:g}" for key, value in self._data
        )

        self._stats = self.get_stats()
        return self.format_output()

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
                raise ValueError(f"Invalid data format: {e}\n")

        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()

        temps = [value for key, value in self._data if key == "temp"]
        stats["avg_temp"] = sum(temps) / len(temps) if temps else 0.0

        return stats

    def format_output(self) -> str:
        return (
            f"Processing sensor batch: [{self._result}]\n"
            f"Sensor analysis: {self._stats["size"]} readings processed, "
            f"avg temp: {self._stats["avg_temp"]}ºC\n"
        )


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self._type: str = "Transaction data"
        self._data: list[tuple[str, int]] = []

        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self._stream_id}, type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self._batch_size = len(data_batch)

        try:
            for item in data_batch:
                key, value = item.split(":")
                self._data.append((key, int(value)))
        except ValueError as e:
            raise ValueError(f"Invalid data format: {e}\n")

        self._result = ", ".join(
            f"{key}:{value:g}" for key, value in self._data
        )

        self._stats = self.get_stats()
        return self.format_output()

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch

        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()

        income = [value for key, value in self._data if key == "buy"]
        outcome = [value for key, value in self._data if key == "sell"]

        stats["net_flow"] = sum(income) - sum(outcome)

        return stats

    def format_output(self) -> str:
        return (
            f"Processing transaction batch: [{self._result}]\n"
            f"Transaction analysis: {self._stats["size"]}"
            " operations processed, "
            f"net flow: {self._stats["net_flow"]:+d} units\n"
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self._type: str = "Event data"
        self._data: list[str] = []

        print("Initializing Event Stream...")
        print(f"Stream ID: {self._stream_id}, type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        self._batch_size = len(data_batch)
        events: Set[str] = {"login", "error", "warning", "logout"}

        try:
            for item in data_batch:
                if item in events:
                    self._data.append(item)
                else:
                    raise ValueError(f"'{item}' is not a possible event.\n")
        except ValueError as e:
            raise ValueError(f"Invalid data format: {e}\n")

        self._result: str = ", ".join(
            f"{value}" for value in self._data
        )

        self._stats = self.get_stats()
        return self.format_output()

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch

        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()

        errors: List = [value for value in self._data if value == "error"]

        stats["error"] = len(errors)

        return stats

    def format_output(self) -> str:
        return (
            f"Processing event batch: [{self._result}]\n"
            f"Event analysis: {self._stats["size"]} events processed, "
            f"{self._stats["error"]} error detected\n"
        )


class StreamProcessor:
    def __init__(self, batch_streams: List[DataStream]) -> None:
        self._batch_streams: List[DataStream] = batch_streams
        print("Processing mixed stream types through unified interface...\n")

    def batch_process(self) -> None:
        for stream in self._batch_streams:
            operations = stream.get_stats()
            print(f"{stream.format_output()} {operations['size']}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor: SensorStream = SensorStream("SENSOR_001")
    try:
        print(sensor.process_batch(
            ["temp:22.5", "humidity:65", "pressure:1013"]))
    except ValueError as e:
        print(e)

    trans: TransactionStream = TransactionStream("TRANS_001")
    try:
        print(trans.process_batch(["buy:100", "sell:150", "buy:75"]))
    except ValueError as e:
        print(e)

    event: EventStream = EventStream("EVENT_001")
    try:
        print(event.process_batch(["login", "error", "logout"]))
    except ValueError as e:
        print(e)

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
