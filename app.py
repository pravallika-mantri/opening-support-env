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

    formatted = output.replace("\n", "<br>")

    return f"""
    <html>
        <body style="background:black;color:lime;font-family:monospace;padding:20px;">
            <h2>OpenEnv Output</h2>
            <div>{formatted}</div>
        </body>
    </html>
    """