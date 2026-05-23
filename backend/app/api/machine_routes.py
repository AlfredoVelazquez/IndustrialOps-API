from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.machine_schema import (
    MachineCreate,
    MachineUpdate,
    MachineResponse,
    MachinePaginatedResponse,
)

from app.services.machine_service import (
    create_machine,
    get_machines,
    get_machine_by_id,
    update_machine,
    delete_machine,
)

router = APIRouter(
    prefix="/api/machines",
    tags=["Machines"],
)


@router.post(
    "",
    response_model=MachineResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_machine(
    machine: MachineCreate,
    db: Session = Depends(get_db),
):
    created_machine = create_machine(db, machine)

    if not created_machine:
        raise HTTPException(
            status_code=400,
            detail="Machine code already exists",
        )

    return created_machine


@router.get(
    "",
    response_model=MachinePaginatedResponse,
)
def read_machines(
    search: str | None = None,
    is_active: bool | None = None,
    order_by: str = "id",
    order_direction: str = "asc",
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return get_machines(
        db=db,
        search=search,
        is_active=is_active,
        order_by=order_by,
        order_direction=order_direction,
        limit=limit,
        offset=offset,
    )


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


@router.put(
    "/{machine_id}",
    response_model=MachineResponse,
)
def update_existing_machine(
    machine_id: int,
    machine: MachineUpdate,
    db: Session = Depends(get_db),
):
    updated_machine = update_machine(
        db,
        machine_id,
        machine,
    )

    if not updated_machine:
        raise HTTPException(
            status_code=404,
            detail="Machine not found",
        )

    if updated_machine == "duplicate_code":
        raise HTTPException(
            status_code=400,
            detail="Machine code already exists",
        )

    return updated_machine


@router.delete(
    "/{machine_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_existing_machine(
    machine_id: int,
    db: Session = Depends(get_db),
):
    deleted_machine = delete_machine(db, machine_id)

    if not deleted_machine:
        raise HTTPException(
            status_code=404,
            detail="Machine not found",
        )

    return