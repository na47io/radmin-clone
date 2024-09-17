from dataclasses import dataclass
from datetime import datetime

@dataclass
class Plan:
    source_env: str
    target_env: str
    created_at: datetime

    # let the resource definitions change in the future, represent them as a list of dictionaries
    # these dicts can be Schedules, Reports, Templates or AWS Quicksight Batch Import objects
    delete: list[dict]
    update: list[dict]
    create: list[dict]