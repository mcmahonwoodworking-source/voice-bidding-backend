from pydantic import BaseModel
from typing import List, Optional, Literal

JobType = Literal["SHOP", "CNC", "TIME_MATERIALS", "DESIGN"]

class CreateJobIn(BaseModel):
    title: str
    client_name: str
    address: str
    job_type: JobType

class StepHoursIn(BaseModel):h
    step_key: str
    hours: float
    include: bool = True
