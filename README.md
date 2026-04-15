# 3D Word Cloud Project

## Overview
This project is a full-stack application that visualizes topics from a news/article URL as a 3D word cloud.

Users enter a URL, and the system:
- Scrapes article content
- Extracts keywords using TF-IDF
- Sends data to frontend
- Displays interactive 3D word cloud

---

## Tech Stack

Frontend:
- React (TypeScript)
- React Three Fiber
- Three.js

Backend:
- FastAPI
- Python
- BeautifulSoup (web scraping)
- Scikit-learn (TF-IDF)

---

## How to Run

### Backend
cd backend  
pip install -r requirements.txt  
uvicorn main:app --reload  

### Frontend
cd frontend  
npm install  
npm start  

---

## API Endpoint

POST /analyze

Request:
{
  "url": "https://example.com"
}

Response:
[
  { "word": "data", "weight": 0.8 }
]

---

## Features
- URL input system
- Web scraping
- TF-IDF keyword extraction
- 3D rotating visualization
- Full-stack integration

---

## Author
Ahmed Unissa