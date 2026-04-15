# 3D Word Cloud Project

## Overview

This is a full-stack project that takes a news or article URL and converts its content into a 3D word cloud visualization.

The idea is simple: you enter a URL, the system reads the content from the page, extracts the most important words, and displays them in an interactive 3D space.

## Tech Stack

Frontend:
- React (TypeScript)
- React Three Fiber
- Three.js

Backend:
- FastAPI (Python)
- BeautifulSoup (for web scraping)
- Scikit-learn (TF-IDF keyword extraction)

## How It Works

1. User enters a URL in the frontend
2. Backend fetches and extracts article content
3. TF-IDF is used to find important keywords
4. Backend sends words and their weights to the frontend
5. Frontend displays them as a rotating 3D word cloud

## API Endpoint

POST /analyze

Request:
{
  "url": "https://example.com"
}

Response:
[
  {
    "word": "avoid",
    "weight": 0.2886751345948129
  },
  {
    "word": "documentation",
    "weight": 0.2886751345948129
  },
]

## Features

- URL input system
- Web scraping from article pages
- TF-IDF keyword extraction
- Interactive 3D word cloud visualization
- Full-stack integration between React and FastAPI

## How to Run

Backend:
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Frontend:
cd frontend
npm install
npm start

## Sample Test URLs (For Quick Testing)

You can use the following URLs to test the application:

- https://en.wikipedia.org/wiki/Artificial_intelligence
- https://en.wikipedia.org/wiki/Machine_learning
- https://www.bbc.com/news

These are good examples because they contain enough text for keyword extraction and visualization.

## Author

Ahmedunissa
