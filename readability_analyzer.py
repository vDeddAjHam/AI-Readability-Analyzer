import textstat
import openai
import os
from dotenv import load_dotenv

# Load API key if GPT-4 suggestions are desired
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_readability(text):
    reading_ease = textstat.flesch_reading_ease(text)
    grade_level = textstat.flesch_kincaid_grade(text)
    return reading_ease, grade_level

def suggest_improvements(text):
    prompt = f"Analyze the following text for readability and suggest improvements:\n\n{text}\n\nSuggestions:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a writing coach."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    text = input("Enter text for readability analysis:\n")
    ease, grade = analyze_readability(text)
    print(f"Flesch Reading Ease: {ease:.2f}")
    print(f"Flesch-Kincaid Grade Level: {grade:.2f}")
    
    if os.getenv("OPENAI_API_KEY"):
        suggestions = suggest_improvements(text)
        print("\nImprovement Suggestions:\n", suggestions)
