import openai
from config import apikey  # Ensure you store the API key securely in config.py

openai.api_key = apikey

def fetch_info_from_openai(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
