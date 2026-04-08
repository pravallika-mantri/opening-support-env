from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def run_env():
    result = subprocess.run(
        ["python", "inference.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output = result.stdout if result.stdout else result.stderr

    # Make it look like terminal output
    return f"""
    <html>
    <head>
        <title>OpenEnv Output</title>
    </head>
    <body style="background-color:black; color:#00FF00; font-family:monospace; padding:20px;">
        <h2>OpenEnv Execution Output</h2>
        <pre>{output}</pre>
    </body>
    </html>
    """