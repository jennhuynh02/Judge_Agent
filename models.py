from pydantic import BaseModel, Field
from typing import Literal, List

class ViralityScore(BaseModel):
    emotional_trigger: int = Field(ge=0, le=25)
    hook_quality: int = Field(ge=0, le=25)
    novelty: int = Field(ge=0, le=25)
    compression: int = Field(ge=0, le=25)
    total: int = Field(ge=0, le=100)

class JudgeResult(BaseModel):
    origin: Literal["human", "ai", "ai-assisted"]
    origin_confidence: float = Field(ge=0, le=1)
    virality: ViralityScore
    distribution: List[str] = Field(max_length=3)
    explanation: str
