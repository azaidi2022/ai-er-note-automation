from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

past_notes = [
    "Patient with fever and cough treated with paracetamol.",
    "Shortness of breath due to asthma exacerbation.",
    "Chest pain with ST elevation, immediate PCI."
]

_vectorizer = None
_tfidf_matrix = None

def _load():
    global _vectorizer, _tfidf_matrix
    if _vectorizer is None:
        _vectorizer = TfidfVectorizer(stop_words="english")
        _tfidf_matrix = _vectorizer.fit_transform(past_notes)

def retrieve_similar_notes(text: str, k=2):
    _load()
    query_vec = _vectorizer.transform([text])
    scores = cosine_similarity(query_vec, _tfidf_matrix)[0]
    top_indices = scores.argsort()[-k:][::-1]
    return [past_notes[i] for i in top_indices]

