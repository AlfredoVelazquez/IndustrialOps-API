from pydantic import BaseModel
from datetime import datetime


class MachineBase(BaseModel):
    code: str
    name: str
    area: str
    is_active: bool = True


class MachineCreate(MachineBase):
    pass


class MachineResponse(MachineBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True