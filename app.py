from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style="background:black;color:lime;font-family:monospace;padding:20px;">
        <h2>OpenEnv Environment</h2>
        <p>Click below to run the environment:</p>
        <a href="/run" style="color:cyan;">Run Simulation</a>
    </body>
    </html>
    """

@app.get("/run", response_class=HTMLResponse)
def run_env():
    try:
        result = subprocess.run(
            ["python", "inference.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10   
        )

        output = result.stdout.strip() if result.stdout else result.stderr.strip()

    except Exception as e:
        output = str(e)

    return f"""
    <html>
    <body style="background:black;color:lime;font-family:monospace;padding:20px;">
        <h2>Execution Output</h2>
        <pre>{output}</pre>
        <br><a href="/">⬅ Back</a>
    </body>
    </html>
    """