from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Protocol


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = []

        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def add_stage(self, stage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    def process(self, data: Any) -> str:
        print("Processing JSON data through pipeline...")
        print(f"Input: {data}")

        return self.run_stages(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        pass

    def process(self, data: List[Any]) -> Dict[str, Union[str, float]]:
        pass


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        pass

    def process(self, data: List[Any]) -> Dict[str, Union[str, float]]:
        pass


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Dict:
        pass


class TransformStage:
    def process(self, data: Any) -> Dict:
        pass


class OutputStage:
    def process(self, data: Any) -> str:
        pass


class NexusManager:
    pipelines = []

    @classmethod
    def add_pipeline(cls, pipeline: ProcessingPipeline):
        cls.pipelines.append(pipeline)

    @classmethod
    def process_data(cls):
        for pip in cls.pipelines:
            pip.process()


def main() -> None:
    diferent_types_of_data = [
        {"sensor": "temp", "value": 23.5, "unit": "C"},
        "user_001,LOGIN,2025-02-10",
        [21.9, 22.5, 22.0, 21.7, 22.4]
    ]

    adapters = [JSONAdapter, CSVAdapter, StreamAdapter]
    pipeline = []

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    for data, adapter in zip(diferent_types_of_data, adapters):
        pipeline.append(adapter(data))

    nexus = NexusManager()
    for pip in pipeline:
        nexus.add_pipeline(pip)

    nexus.process_data()


if __name__ == "__main__":
    main()
