from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def run_env():
    result = subprocess.run(
        ["python", "inference.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output = result.stdout if result.stdout else result.stderr

    return {"output": output}