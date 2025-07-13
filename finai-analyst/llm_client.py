import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()

if PROVIDER == "openai":
    from openai import OpenAI
    client = OpenAI()
elif PROVIDER == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    client = genai
else:
    print("LLM CLIENT PROVIDER=", PROVIDER)
    raise ValueError("Unsupported LLM_PROVIDER. Use 'openai' or 'gemini'.")
