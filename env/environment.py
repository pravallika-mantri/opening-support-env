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
        info = {"error": None}


        if action.action_type == "classify":
            if action.content == self.ticket["label"]:
                reward += 0.4
        else:
            reward -= 0.2

        elif action.action_type == "reply":
            if "sorry" in (action.content or "").lower():
                reward += 0.2

        elif action.action_type == "resolve":
            if "resolved" in (action.content or "").lower():
            reward += 0.4

        self.history.append({
            "action_type": action.action_type,
            "content": action.content
        })

        self.current_step += 1


        if self.current_step >= 3:
            final_score = grade_resolution(self.history)
            reward += final_score * 0.5
            self.done = True

        return Observation(**self.ticket), round(reward, 2), self.done, info

    def state(self):
        return {
            "ticket": self.ticket,
            "history": self.history,
            "step": self.current_step
        }