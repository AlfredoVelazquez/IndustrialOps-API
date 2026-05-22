from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.machine_schema import (
    MachineCreate,
    MachineResponse,
)
from app.services.machine_service import (
    create_machine,
    get_machines,
    get_machine_by_id,
)

router = APIRouter(
    prefix="/api/machines",
    tags=["Machines"],
)


@router.post(
    "",
    response_model=MachineResponse,
)
def create_new_machine(
    machine: MachineCreate,
    db: Session = Depends(get_db),
):
    return create_machine(db, machine)


@router.get(
    "",
    response_model=list[MachineResponse],
)
def read_machines(
    db: Session = Depends(get_db),
):
    return get_machines(db)


@router.get(
    "/{machine_id}",
    response_model=MachineResponse,
)
def read_machine_by_id(
    machine_id: int,
    db: Session = Depends(get_db),
):
    machine = get_machine_by_id(db, machine_id)

    if not machine:
        raise HTTPException(
            status_code=404,
            detail="Machine not found",
        )

    return machine