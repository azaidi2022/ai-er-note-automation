SYMPTOMS = {
    "fever", "cough", "shortness of breath", "chest pain",
    "abdominal pain", "vomiting", "diarrhea", "confusion"
}

DISEASES = {
    "asthma", "stroke", "heart failure", "gastroenteritis"
}

MEDICATIONS = {
    "paracetamol", "ibuprofen", "aspirin", "tpa"
}

def extract_medical_entities(text: str):
    text = text.lower()
    entities = []

    for s in SYMPTOMS:
        if s in text:
            entities.append({"text": s, "label": "SYMPTOM"})

    for d in DISEASES:
        if d in text:
            entities.append({"text": d, "label": "DISEASE"})

    for m in MEDICATIONS:
        if m in text:
            entities.append({"text": m, "label": "MEDICATION"})

    return entities
