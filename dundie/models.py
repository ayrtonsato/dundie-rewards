"""Models"""
from pydantic import BaseModel, validator, Field
from decimal import Decimal
from datetime import datetime
from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    """Model class person"""
    pk: str  # noqa
    name: str
    dept: str
    role: str

    @validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise InvalidEmailError(
                f"Invalid email for {v!r}"
            )
        return v

    def __str__(self) -> str:
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    @validator("value", pre=True)
    def value_logic(cls, v):
        return Decimal(v) * 2

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal


class User(BaseModel):
    person: Person
    password: str = Field(default_factory=generate_simple_password)

    class Config:
        json_encoders = {Person: lambda p: p.pk}


if __name__ == "__main__":
    p = Person(pk="bruno@g.com", name="Bruno", dept="Sales", role="NA")
    print(p)
    print(p.json())

    b = Balance(person=p, value=100)
    print(b.json(models_as_dict=False))

    m = Movement(person=p, date=datetime.now(), actor="sys", value=10)
    print(m.json(models_as_dict=False))

    u = User(person=p)
    print(u.json(models_as_dict=False))
