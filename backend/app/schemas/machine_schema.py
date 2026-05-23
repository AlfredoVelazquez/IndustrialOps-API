from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import List


class MachineBase(BaseModel):
    code: str = Field(..., min_length=2, max_length=20)
    name: str = Field(..., min_length=3, max_length=100)
    area: str = Field(..., min_length=2, max_length=80)
    is_active: bool = True

    @field_validator("code")
    @classmethod
    def normalize_code(cls, value: str) -> str:
        value = value.strip().upper()

        if not value:
            raise ValueError("Code cannot be empty")

        return value

    @field_validator("name", "area")
    @classmethod
    def validate_not_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty")

        return value


class MachineCreate(MachineBase):
    pass


class MachineUpdate(MachineBase):
    pass


class MachineResponse(MachineBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class MachinePaginatedResponse(BaseModel):
    total: int
    limit: int
    offset: int
    data: List[MachineResponse]

