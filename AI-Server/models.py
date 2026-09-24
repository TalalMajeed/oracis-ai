from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class RecommendedJob(BaseModel):
    title: str = Field(..., min_length=1)
    rank: int = Field(..., ge=1, le=10)


class LinkedInAnalysis(BaseModel):
    userId: str = Field(..., min_length=1)
    recommended_jobs: List[RecommendedJob] = Field(default_factory=list)
    potential_jobs: List[str] = Field(default_factory=list)
    comments: str = ""
    improvements: List[str] = Field(default_factory=list)
    overall_rank: int = Field(..., ge=1, le=10)
    createdAt: datetime = Field(default_factory=datetime.now)


class AnalysisRequest(BaseModel):
    candidate_id: str = Field(..., min_length=1)
    linkedin_data: str = Field(..., min_length=1)


class RankResponse(BaseModel):
    rankings: List[str]
