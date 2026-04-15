from fastapi import FastAPI
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str


#web scraping
def extract_text(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

        return text.strip()

    except Exception as e:
        print("Error fetching URL:", e)
        return ""


@app.post("/analyze")
def analyze(req: URLRequest):
    text = extract_text(req.url)

    # prevent crash from empty text
    if not text:
        return {"error": "Could not extract text from URL"}

    vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
    X = vectorizer.fit_transform([text])

    words = vectorizer.get_feature_names_out()
    scores = X.toarray()[0]

    result = [
        {"word": w, "weight": float(s)}
        for w, s in zip(words, scores)
        if s > 0
    ]

    return result