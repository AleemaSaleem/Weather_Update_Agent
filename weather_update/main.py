
import os
from dotenv import load_dotenv
from tavily import TavilyClient

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    function_tool,
    set_tracing_disabled,
)

# 🌿 Load environment variables
load_dotenv()

# 🔐 API keys
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 🚫 Disable tracing/logging
set_tracing_disabled(True)

# 🌐 Gemini OpenAI-compatible client
gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 🧠 Gemini model setup
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client,
)

# 🔍 Tavily client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# 🛠️ Tool: Fetch today's weather via Tavily
@function_tool
def get_weather(location: str = "Lahore") -> str:
    """Searches the web for today's weather in the specified location."""
    query = f"today's weather in {location}"
    result = tavily_client.search(query)
    if result and result.get("results"):
        return result["results"][0]["content"]
    return "Sorry, I couldn't find the weather."

# 🤖 Agent setup
agent = Agent(
    name="WeatherAgent",
    instructions="You are a friendly assistant. Always use the tool to get today's weather.",
    model=model,
    tools=[get_weather],
)

# 🧪 Main entry point
if __name__ == "__main__":
    from asyncio import run

    async def main():
        result = await Runner.run(
            agent,
            "What's the weather in Lahore today?",
        )
        print("\n🌤️ Agent Output:\n")
        print(result.final_output)

    run(main())

