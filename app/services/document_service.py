import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def generate_ai_reply(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return (
            "Gemini API key is not configured. Fallback mode is active. "
            "Your request was: " + prompt + ". "
            "You can add GEMINI_API_KEY to your .env file and restart the server to use live AI responses."
        )

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return (
            "The AI service encountered an issue. Please check the Gemini API key and request format. "
            "Here is a safe fallback response for your prompt: " + prompt
        )
