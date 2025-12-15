# AI ER Note Automation System

This project is a FastAPI-based AI backend designed to assist with emergency room (ER) clinical documentation by extracting key medical information from free-text input and retrieving similar past cases.

---

## Features

- FastAPI web server exposing REST API endpoints
- Rule-based medical entity extraction (symptoms, diseases, medications)
- Semantic retrieval of similar clinical notes using TF-IDF and cosine similarity
- Modular, production-style project structure suitable for extension

---

## Architecture

### High-level pipeline

User Input (Text)  
→ Medical Entity Extraction (NLP)  
→ Semantic Similarity Retrieval  
→ Structured JSON Response  

---

## Tech Stack

- **Python**
- **FastAPI** – API framework and web server
- **scikit-learn** – TF-IDF vectorization and cosine similarity
- **Git & GitHub** – version control and project hosting

---

## Example API Usage

### Endpoint

`POST /process_text`

### Request Body

```json
{
  "text": "Patient presents with fever and cough."
}

### Response
{
  "entities": [
    { "text": "fever", "label": "SYMPTOM" },
    { "text": "cough", "label": "SYMPTOM" }
  ],
  "similar_notes": [
    "Patient with fever and cough treated with paracetamol."
  ]
}

## Future Improvements

- Add speech-to-text support using Whisper for audio-based input
- Replace rule-based NLP with machine learning–based named entity recognition (NER)
- Upgrade semantic retrieval to transformer-based embeddings
- Integrate large language model (LLM)–based note generation using a full RAG pipeline

## Motivation

This project explores how natural language processing (NLP) and retrieval-based reasoning techniques can be applied to support clinical documentation and decision-making in high-pressure emergency care environments.
