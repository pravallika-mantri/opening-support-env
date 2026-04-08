from typing import Tuple, List
from env.models import Observation, Action
from env.graders import grade_classification, grade_response, grade_resolution


class SupportEnv:
    def __init__(self):
        self.current_step = 0
        self.done = False
        self.ticket = None
        self.history: List[dict] = []

    def reset(self) -> Observation:
        self.current_step = 0
        self.done = False
        self.history = []

        self.ticket = {
            "ticket_id": 1,
            "message": "I was charged twice for my order",
            "status": "open"
        }

        return Observation(**self.ticket)

    def step(self, action: Action) -> Tuple[Observation, float, bool, dict]:
        reward = 0.0
        info = {"error": None}

        # Prevent infinite loop penalty
        if self.history and self.history[-1]["action_type"] == action.action_type:
            reward -= 0.2

        # Classification
        if action.action_type == "classify":
            score = grade_classification(self.ticket["message"], action.content)
            reward += score * 0.5

        # Response
        elif action.action_type == "reply":
            score = grade_response(action.content or "")
            reward += score * 0.5

        # Invalid action penalty
        else:
            reward -= 0.1
            info["error"] = "Invalid action"

        self.history.append({
            "action_type": action.action_type,
            "content": action.content
        })

        self.current_step += 1

        # Final resolution scoring
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