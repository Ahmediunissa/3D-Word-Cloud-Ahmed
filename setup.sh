#!/bin/bash

echo "Installing backend dependencies..."
cd backend
pip install -r requirements.txt

echo "Starting backend..."
uvicorn main:app --reload &

echo "Installing frontend dependencies..."
cd ../frontend
npm install

echo "Starting frontend..."
npm start