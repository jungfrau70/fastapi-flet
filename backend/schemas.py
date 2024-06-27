from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class OHLC(BaseModel):
    timestamp: str
    open: float
    high: float
    low: float
    close: float

class OHLCResponse(BaseModel):
    data: List[OHLC]
