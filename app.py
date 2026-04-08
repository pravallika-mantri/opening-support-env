from fastapi import FastAPI
from env.environment import SupportEnv

app = FastAPI()

env = SupportEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    from env.models import Action
    action_obj = Action(**action)
    obs, reward, done, info = env.step(action_obj)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()
