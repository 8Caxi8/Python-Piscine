from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Protocol


class NexusManager:
    pipelines: List[ProcessingPipeline]
    def add_pipeline():
        pass

    def process_data():
        pass


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        for stage in self.stages:
            data: Any = stage_process(data)
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    def process(self, data: Any) -> str:
        print("Processing JSON data through pipeline...")
        print(f"Input: {data}")

        try:
            processed: str = self.run_stages(data)
            print()


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
