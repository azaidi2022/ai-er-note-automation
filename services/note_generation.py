def generate_structured_note(text, similar_notes):
    return {
        "History": text,
        "Physical Exam": "Vitals stable. No acute distress.",
        "Medical Decision Making": f"Similar case: {similar_notes[0]}",
        "Procedure": "None"
    }
