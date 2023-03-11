from pydantic import BaseModel
from pydantic import Field

class Course(BaseModel):
    name: str = Field(..., example="Banco W")
    skills = list[str] = Field(...)