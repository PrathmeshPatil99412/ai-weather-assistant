import re

REQUIRED_SECTIONS = [
    "Weather Analysis",
    "Recommendations",
    "Travel Suggestions",
    "Risk Alerts"
]


def validate_response(response_text):
    """
    Validates and cleans Gemini response.
    Returns: (is_valid, cleaned_or_error_response)
    """

    # Step 1: Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in response_text:
            return False, f"Missing section: {section}"

    # Step 2: Check if sections have content
    for section in REQUIRED_SECTIONS:
        pattern = rf"{section}(.+?)(?=\n\d\.|\Z)"
        match = re.search(pattern, response_text, re.DOTALL)

        if not match or len(match.group(1).strip()) < 10:
            return False, f" Section '{section}' is empty or too short"

    # Step 3: Basic cleanup
    cleaned_response = response_text.strip()

    return True, cleaned_response


def format_response(response_text):
    """
    Optional: clean formatting (remove excessive spaces)
    """
    response_text = re.sub(r"\n{3,}", "\n\n", response_text)
    return response_text.strip()