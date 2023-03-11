from pydantic import BaseModel
from pydantic import Field

from app.utils.base import CompanySector

class Company(BaseModel):
    name: str = Field(..., example="Banco W")
    sector: CompanySector = Field(..., example=CompanySector.services)
    phone: int = Field()
    email: str = Field(..., example="pepito@hismail.co")
    skills = list[str] = Field(...)