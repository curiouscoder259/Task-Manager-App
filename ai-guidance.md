# AI Guidance & Architecture Document

This document outlines the architectural decisions, prompt engineering strategies, and integration flow for the Generative AI feature within the AI-Powered Task Manager.

## 1. Feature Overview
The application utilizes a Large Language Model (LLM) to act as an automated productivity assistant. When a user creates a task, they can request an AI analysis. The system evaluates the task's title and description to automatically determine its priority level (Low, Medium, High), provide a logical justification, and suggest an actionable next step.

## 2. Model Selection: Gemini 2.5 Flash
During development, the AI integration was migrated to Google's **Gemini 2.5 Flash** model using the `google-generativeai` SDK. 

**Key reasons for this architectural choice:**
* **Speed & Latency:** The "Flash" class of models is optimized for high-frequency, low-latency tasks, making it ideal for a real-time web application where users expect instant UI feedback.
* **Native Structured Output:** Unlike older models that require fragile regular expressions (Regex) or string manipulation to parse markdown responses, Gemini 2.5 Flash supports strict JSON enforcement via the `response_mime_type="application/json"` configuration. This guarantees type-safety for the React frontend.
* **Cost-Efficiency:** The model provides a highly generous free tier, making it optimal for development, testing, and portfolio demonstration.

## 3. Prompt Engineering Strategy
The system utilizes a "Zero-Shot" prompt with strict persona and output constraints. 

**The Prompt Template:**
```text
You are a task management assistant. Analyze the following task:
Task: {title}
Details: {description}

Respond ONLY with a JSON object. It must have exactly these keys: 
"priority" (low/medium/high), "reason" (one sentence), and "next_step" (one action).