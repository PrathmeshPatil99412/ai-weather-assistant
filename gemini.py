import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
from validator import validate_response, format_response

#Configure the API
genai.configure(api_key=GEMINI_API_KEY)

#Initialize the model
model = genai.GenerativeModel(GEMINI_MODEL)


def build_prompt(weather_data):
    return f"""
You are a structured AI weather analysis system.

Follow the exact format below:

1. Weather Analysis
- Provide a clear summary of current conditions

2. Recommendations
- Suggest clothing, items, and precautions

3. Travel Suggestions
- Suggest activities and travel advice based on conditions

4. Risk Alerts
- Highlight any risks or warnings
- If none, explicitly state: "No significant risks"

RULES:
- Use ONLY the provided weather data
- Do NOT skip any section
- Do NOT add extra sections
- Follow the exact structure
- Keep responses concise and structured
- Use bullet points where appropriate
- Use simple and clear language

Weather Data:
{weather_data}
"""


def analyze_weather(weather_data):
    try:
        #Generate the prompt
        prompt = build_prompt(weather_data)

        #Call Gemini API
        response = model.generate_content(prompt)

        if not response or not response.text:
            return "Error: Empty response from model."

        text = response.text

        #Validate the response
        is_valid, result = validate_response(text)

        if not is_valid:
            return result  # validation error message

        # Format final output
        return format_response(result)

    except Exception as e:
        return f"Error: {str(e)}"