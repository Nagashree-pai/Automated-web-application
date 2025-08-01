from fastapi import FastAPI, Request
from pydantic import BaseModel
from .runner import run_script
from .llm_handler import get_script_from_llm

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/execute")
async def execute(request: PromptRequest):
    js_code = get_script_from_llm(request.prompt)
    success, log = run_script(js_code)
    return {
        "success": success,
        "log": log,
        "code": js_code
    }
