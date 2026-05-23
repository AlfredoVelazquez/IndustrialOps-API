from sqlalchemy.orm import Session

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


def get_machines(db: Session):
    return db.query(Machine).all()


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