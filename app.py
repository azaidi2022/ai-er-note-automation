from fastapi import FastAPI
from pydantic import BaseModel

from services.nlp import extract_medical_entities
from services.retrieval import retrieve_similar_notes

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/process_text")
def process_text(input: TextInput):
    entities = extract_medical_entities(input.text)
    similar = retrieve_similar_notes(input.text, k=2)
    return {
        "entities": entities,
        "similar_notes": similar
    }
