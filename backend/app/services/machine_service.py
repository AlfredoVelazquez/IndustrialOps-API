from sqlalchemy.orm import Session

from app.models.machine import Machine
from app.schemas.machine_schema import MachineCreate


def create_machine(db: Session, machine_data: MachineCreate):
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
