from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class SkillLanguage(BaseModel):
    language: Optional[str] = None
    proficiency: Optional[str] = None

    model_config = ConfigDict(extra="forbid")


class Skills(BaseModel):
    technical_skills: List[str] = Field(default_factory=list)
    soft_skills: List[str] = Field(default_factory=list)
    languages: List[SkillLanguage] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid")


class WorkExperienceItem(BaseModel):
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    technologies: List[str] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid")


class EducationItem(BaseModel):
    school_name: Optional[str] = None
    degree: Optional[str] = None
    major: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    gpa: Optional[str] = None

    model_config = ConfigDict(extra="forbid")


class ProjectItem(BaseModel):
    project_name: Optional[str] = None
    role: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    technologies: List[str] = Field(default_factory=list)
    project_url: Optional[str] = None

    model_config = ConfigDict(extra="forbid")


class CertificationItem(BaseModel):
    name: Optional[str] = None
    issuer: Optional[str] = None
    date: Optional[str] = None

    model_config = ConfigDict(extra="forbid")


class AwardItem(BaseModel):
    name: Optional[str] = None
    issuer: Optional[str] = None
    date: Optional[str] = None

    model_config = ConfigDict(extra="forbid")


class ActivityItem(BaseModel):
    organization: Optional[str] = None
    role: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None

    model_config = ConfigDict(extra="forbid")


class PersonalInfo(BaseModel):
    full_name: Optional[str] = None
    job_title: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None

    model_config = ConfigDict(extra="forbid")


class CVSchema(BaseModel):
    personal_info: PersonalInfo = Field(default_factory=PersonalInfo)
    summary: Optional[str] = None
    skills: Skills = Field(default_factory=Skills)
    work_experience: List[WorkExperienceItem] = Field(default_factory=list)
    education: List[EducationItem] = Field(default_factory=list)
    projects: List[ProjectItem] = Field(default_factory=list)
    certifications: List[CertificationItem] = Field(default_factory=list)
    awards: List[AwardItem] = Field(default_factory=list)
    activities: List[ActivityItem] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid")
