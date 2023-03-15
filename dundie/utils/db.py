from typing import Optional

from sqlmodel import Session, select

from dundie.models import Balance, Movement, Person, User
from dundie.settings import EMAIL_FROM
from dundie.utils.email import send_email


def add_person(session: Session, instance: Person):
    """Saves person data to database
    - Email is unique (resolved by dictionary hash table)
    - If exists, update, else create
    - Set initial balance (managers = 100, others = 500)
    - Email is valid
    - Generate password if user is new and send_email
    """
    existing = session.exec(
        select(Person).where(Person.email == instance.email)
    ).first()
    created = existing is None
    if created:
        session.add(instance)
        set_initial_balance(session, instance)
        password = set_initial_password(session, instance)
        # TODO: usar sistema de filas
        send_email(
            EMAIL_FROM, instance.email, "Your dundie password", password
        )
        return instance, created
    else:
        existing.dept = instance.dept
        existing.role = instance.role
        session.add(existing)
        return instance, created


def set_initial_password(session: Session, instance: Person) -> str:
    """Generated and save password"""
    user = User(person=instance)
    session.add(user)
    return user.password


def set_initial_balance(session: Session, person: Person):
    """Add movement and set initial balance."""
    print(person)
    value = 100 if person.role == "Manager" else 500
    add_movement(session, person, value)


def add_movement(
    session: Session,
    person: Person,
    value: int,
    actor: Optional[str] = "system",
):
    """Adds movement to user account.

    Example::

        add_movement(db, "me@me.com", 100, "me")

    """
    movement = Movement(person=person, value=value, actor=actor)
    session.add(movement)

    movements = session.exec(select(Movement).where(Movement.person == person))

    total = sum([mov.value for mov in movements])

    existing_balance = session.exec(
        select(Balance).where(Balance.person == person)
    ).first()

    if existing_balance:
        existing_balance.value = total
        session.add(existing_balance)
    else:
        session.add(Balance(person=person, value=total))
