from ollama import generate

def get_script_from_llm(prompt: str) -> str:
    full_prompt = (
    "Convert the following natural language command into a complete, executable Playwright script in JavaScript. "
    "Use ESM (import { chromium } from 'playwright'), include the async function wrapper, and declare all required variables. "
    "Ensure the output runs as a standalone script. Only return the code. No explanation. No markdown formatting.\n"
    "Log each major step using console.log(). "
    f"Command: {prompt}"
    )
    


    try:
        response = generate(model="mistral:7b-instruct", prompt=full_prompt)
        code = extract_code(response['response'])  # extract only JS code
        return code
    except Exception as e:
        return f"// LLM Error: {e}"


def extract_code(text: str) -> str:
    import re
    match = re.search(r"```(?:javascript)?\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()

