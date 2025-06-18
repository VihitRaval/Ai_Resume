
import openai
import os

# Set your OpenAI API key here or via environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_suggestions(resume_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer."},
                {"role": "user", "content": f"Here is my resume text:\n{resume_text}\n\nSuggest 3 ways I can improve it for better job prospects."}
            ]
        )
        suggestions = response['choices'][0]['message']['content']
        return suggestions
    except Exception as e:
        return "Could not generate suggestions at this time."
