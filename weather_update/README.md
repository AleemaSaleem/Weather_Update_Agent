# 🌤️ WeatherAgent

**WeatherAgent** is a simple AI assistant that fetches the current weather for any location using the [Tavily Web Search API](https://docs.tavily.com/) and [Gemini](https://deepmind.google/technologies/gemini/) models via an OpenAI-compatible interface.

## 🚀 Features

- 🔍 Real-time weather information using Tavily
- 🤖 Natural language interaction powered by Gemini 2.0 Flash
- 🛠️ Tool-calling agent architecture (function-calling AI)
- 🌐 Async-ready, clean, and minimal code

## 📁 Project Structure

weather_agent/
├── main.py # Main script for WeatherAgent
├── agents/ # Agents framework (assumed from context)
├── .env # Contains API keys (not tracked by Git)
└── README.md # Project documentation

## 🔧 Setup Instructions
### 1. Clone the repo

git clone (Github url)
### 2. Create a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

### 3. Create a .env file

TAVILY_API_KEY=your_tavily_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
### ▶️ Running the Agent
uv run main.py
Or simply:

Example Output:

🌤️ Agent Output:

Today's weather in Lahore is 34°C, mostly sunny with light winds.
🧠 How It Works
The agent is initialized with a Gemini model via the OpenAI-compatible AsyncOpenAI client.

A tool called get_weather() is registered that uses Tavily to search for weather information.

When prompted, the agent automatically uses this tool to fetch and return accurate weather details.

### 📘 Dependencies
openai-agents

tavily-python

python-dotenv


🙋‍♂️ Author
Developed by ** Aleema Saleem **

🌐 Related Links
Tavily API Docs

Gemini by Google DeepMind
