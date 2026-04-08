from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess

app = FastAPI()


result = subprocess.run(
    ["python", "inference.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

output = result.stdout if result.stdout else result.stderr


@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <html>
    <body style="background:black;color:lime;font-family:monospace;padding:20px;">
    <h2>OpenEnv Output</h2>
    <pre>{output}</pre>
    </body>
    </html>
    """