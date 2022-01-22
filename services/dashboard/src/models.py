from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from beanie import Document


class Measurement(BaseModel):
    key: str
    value: float


class Device(Document):
    name: str
    make: Optional[str]
    model: Optional[str]
    description: Optional[str]
    date_added: datetime
    date_updated: datetime


class Telemetry(Document):
    device: Device
    timestamp: datetime
    measurements: List[Measurement]
