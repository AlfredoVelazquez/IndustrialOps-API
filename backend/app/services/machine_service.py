from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.machine import Machine
from app.schemas.machine_schema import MachineCreate, MachineUpdate


def get_machine_by_code(db: Session, code: str):
    return db.query(Machine).filter(Machine.code == code).first()


def create_machine(db: Session, machine_data: MachineCreate):
    existing_machine = get_machine_by_code(db, machine_data.code)

    if existing_machine:
        return None

    new_machine = Machine(
        code=machine_data.code,
        name=machine_data.name,
        area=machine_data.area,
        is_active=machine_data.is_active,
    )

    db.add(new_machine)
    db.commit()
    db.refresh(new_machine)

    return new_machine


def get_machines(
    db: Session,
    search: str | None = None,
    is_active: bool | None = None,
    order_by: str = "id",
    order_direction: str = "asc",
    limit: int = 100,
    offset: int = 0,
):
    query = db.query(Machine)

    if search:
        search_value = f"%{search.strip()}%"

        query = query.filter(
            or_(
                Machine.code.like(search_value),
                Machine.name.like(search_value),
                Machine.area.like(search_value),
            )
        )

    if is_active is not None:
        query = query.filter(Machine.is_active == is_active)

    allowed_order_fields = {
        "id": Machine.id,
        "code": Machine.code,
        "name": Machine.name,
        "area": Machine.area,
        "created_at": Machine.created_at,
    }

    order_column = allowed_order_fields.get(order_by, Machine.id)

    if order_direction.lower() == "desc":
        query = query.order_by(order_column.desc())
    else:
        query = query.order_by(order_column.asc())

    return query.offset(offset).limit(limit).all()

def get_machine_by_id(db: Session, machine_id: int):
    return db.query(Machine).filter(Machine.id == machine_id).first()


def update_machine(
    db: Session,
    machine_id: int,
    machine_data: MachineUpdate
):
    machine = get_machine_by_id(db, machine_id)

    if not machine:
        return None

    existing_machine = get_machine_by_code(db, machine_data.code)

    if existing_machine and existing_machine.id != machine_id:
        return "duplicate_code"

    machine.code = machine_data.code
    machine.name = machine_data.name
    machine.area = machine_data.area
    machine.is_active = machine_data.is_active

    db.commit()
    db.refresh(machine)

    return machine


def delete_machine(db: Session, machine_id: int):
    machine = get_machine_by_id(db, machine_id)

    if not machine:
        return None

    db.delete(machine)
    db.commit()

    return machine