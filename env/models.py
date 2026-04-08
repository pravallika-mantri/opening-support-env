from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    ticket_id: int
    message: str
    status: str

class Action(BaseModel):
    action_type: str   # classify / reply / escalate
    content: Optional[str] = None

class Reward(BaseModel):
    score: float