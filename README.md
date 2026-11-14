# ELI-X (Explain Like I'm X)

[Link](https://vkpfkoosocw83vatqswyyz.streamlit.app/about)

ELI-X is a web application designed to simplify complex topics by explaining them at various levels of complexity, from elementary school to PhD level. It is powered by Google's Gemini AI.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features
- **Adjustable Complexity:** Choose from multiple levels of explanation (Elementary School to PhD).
- **Interactive Interface:** Easy-to-use input form with dynamic suggestions.
- **Powered by AI:** Leverages the latest Gemini AI models for accurate and clear explanations.

## Technologies Used
- [Streamlit](https://streamlit.io/): For building the interactive web interface.
- [Google Gemini API](https://ai.google.dev/): For generating intelligent explanations.
- [Python-dotenv](https://github.com/theskumar/python-dotenv): For managing environment variables.

## Prerequisites
- Python 3.9 or higher
- A Google Gemini API Key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ELI-X
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory and add your Google Gemini API Key:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

## Usage

Run the application using Streamlit:

```bash
streamlit run streamlit_app.py
```

This will launch the application in your default web browser, usually at `http://localhost:8501`.

## Project Structure
- `app.py`: The main application logic and UI.
- `streamlit_app.py`: The entry point for the Streamlit multi-page navigation.
- `AIModel.py`: Wrapper class for interacting with the Gemini AI model.
- `about.py`: The 'About' page content.
- `requirements.txt`: Project dependencies.
- `.env`: Environment variables (API Key).

---
Made by [bruzz-bruzz](https://github.com/bruzz-bruzz)

