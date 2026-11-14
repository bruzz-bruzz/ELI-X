# ELI-X (Explain Like I'm X)

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Gemini-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=-H4ITjDqc5Y)
[![Devpost](https://img.shields.io/badge/Devpost-003E54?style=flat&logo=devpost&logoColor=white)](https://devpost.com/software/eli-x-explain-like-i-m-x)

### [🚀 Live Demo](https://vkpfkoosocw83vatqswyyz.streamlit.app/about)

ELI-X is a web application designed to simplify complex topics by explaining them at various levels of complexity, from elementary school to PhD level. It is powered by Google's Gemini AI.

## Table of Contents
- [Hackathon Project Story](HACKATHON_ABOUT.md)
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
- **Powered by AI:** Leverages Gemini AI models for accurate and clear explanations.

## Technologies Used
- [Streamlit](https://streamlit.io/): For building the interactive web interface.
- [Google Gemini API](https://ai.google.dev/): For generating intelligent explanations.

## Prerequisites
- Python 3.9 or higher
- A Google Gemini API Key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bruzz-bruzz/ELI-X.git
   cd ELI-X
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory and add your Google Gemini API Key:

```env
GEMINI_API_KEY=your_actual_api_key_here
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


## License
This project is licensed under the MIT License.

---
Made by [bruzz-bruzz](https://github.com/bruzz-bruzz)

