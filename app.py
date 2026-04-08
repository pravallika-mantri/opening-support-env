from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import subprocess

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def run_env():
    result = subprocess.run(
        ["python", "inference.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output = result.stdout if result.stdout else result.stderr

    return output