from typing import Tuple, List
from env.models import Observation, Action
from env.graders import grade_classification, grade_response, grade_resolution
import random
from env.data import TICKETS


class SupportEnv:
    def __init__(self):
        self.current_step = 0
        self.done = False
        self.ticket = None
        self.history: List[dict] = []
        
    def reset(self):
        self.current_step = 0
        self.done = False
        self.history = []
        self.ticket = random.choice(TICKETS)

    return Observation(
        ticket_id=self.ticket["id"],
        message=self.ticket["message"],
        status="open"
    )

    def step(self, action: Action) -> Tuple[Observation, float, bool, dict]:
        reward = 0.0


        if action.action_type == "classify":
            reward += grade_classification(self.ticket["label"], action.content) * 0.4


        elif action.action_type == "reply":
            reward += grade_response(action.content or "") * 0.3


        elif action.action_type == "resolve":
            reward += grade_resolution(action.content or "") * 0.3


        if self.history and self.history[-1]["action_type"] == action.action_type:
            reward -= 0.3

        self.history.append({
            "action_type": action.action_type,
            "content": action.content
        })

        self.current_step += 1


        if self.history and self.history[-1]["action_type"] == action.action_type:
            reward -= 0.3

        return Observation(**self.ticket), round(reward, 2), self.done, info

    def state(self):
        return {
            "ticket": self.ticket,
            "history": self.history,
            "step": self.current_step
        }