# 📊 Sentiment Analysis & Visualization Web App

A Flask-based web application that performs **sentiment analysis on CSV files** containing text comments and presents the results through **interactive visualizations** such as bar charts, pie charts, word clouds, and an optional **text summary**.

This project uses **state-of-the-art NLP models from Hugging Face Transformers** and is designed to be lightweight, GitHub-safe, and easy to deploy.

---

## 🚀 Features

- 📁 Upload CSV files with raw text data
- 🤖 Sentiment analysis using a pre-trained RoBERTa model
- 📊 Visualizations:
  - Sentiment distribution (Bar Chart)
  - Sentiment share (Pie Chart)
  - Word Cloud of frequent terms
- 🧠 Optional text summarization using BART
- 🖥️ Clean, modern UI (HTML + CSS)
- ⚡ Automatic model downloading & caching (no large files in repo)

---

## 🧠 Models Used

| Task | Model |
|----|----|
| Sentiment Analysis | `cardiffnlp/twitter-roberta-base-sentiment` |
| Text Summarization | `facebook/bart-large-cnn` |

> Models are automatically downloaded from Hugging Face and cached locally.  
> They are **not stored in this repository**.

---

## 📂 Project Structure

