import google.generativeai as genai
import os
import json


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def suggest_task_priority(title: str, description: str) -> dict:
   
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""
    You are a task management assistant. Analyze the following task:
    Task: {title}
    Details: {description}
    
    Respond ONLY with a JSON object. It must have exactly these keys: 
    "priority" (low/medium/high), "reason" (one sentence), and "next_step" (one action).
    """
    
    # Enforce strict JSON output so it never crashes the React frontend
    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )
    
    return json.loads(response.text)