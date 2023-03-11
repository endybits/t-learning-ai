import enum


class CompanySector(enum.Enum):
    agro= 'agro'
    industry = 'industry'
    services = 'services'


class SkillType(enum.Enum):
    soft = 'soft'
    technical = 'technical'
    corporate = 'corporate'