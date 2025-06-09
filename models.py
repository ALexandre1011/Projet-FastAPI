from pydantic import BaseModel
from typing import Optional,List,Dict
from datetime import datetime

class Temperature(BaseModel):
    value: float
    quality: str

class WindDirection(BaseModel):
    angle: int
    quality: str
    type: Optional[str]


class WindSpeed(BaseModel):
    rate: float
    quality: str

class Wind(BaseModel):
    direction: WindDirection
    speed: WindSpeed

class PrecipitationEstimatedObservation(BaseModel):
    discrepancy: str
    estimatedWaterDepth: int

class SeaSurfaceTemperature(BaseModel):
    value: float
    quality: str

class WeatherObservation(BaseModel):
    ts: datetime
    st: str
    airTemperature: Optional[Temperature]
    wind: Optional[Wind]
    precipitationEstimatedObservation: Optional[PrecipitationEstimatedObservation]
    seaSurfaceTemperature: Optional[SeaSurfaceTemperature]
    is_deleted: Optional[bool] = False
    deleted_at: Optional[datetime] = None