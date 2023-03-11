from pydantic import BaseModel
from pydantic import Field

from app.utils.base import SkillType

class Skill(BaseModel):
    name: str = Field(..., example="Banco W")
    sector: SkillType = Field(..., example=SkillType.technical)