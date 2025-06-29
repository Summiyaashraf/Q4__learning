from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI , function_tool
import requests
import os 
import chainlit as cl
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key=os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Step 1: External_Client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Step 2: Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Step 3: Config define at run level
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# function tool
@function_tool
def crypto_price(nameid: str ) -> str:
    """
    Fetch the USD price of a cryptocurrency using CoinGecko API.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={nameid}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if nameid in data:
        return f"The price of {nameid} is ${data[nameid]['usd']}."
    else:
        return "Cryptocurrency not found."

    
# Step 4: Agent
crypto_agent = Agent(
    name="Crypto AI Assistant",
    instructions="You are a helpful assistant that provides cryptocurrency prices.",
    tools=[crypto_price]
)

@cl.on_chat_start
async def handle_chat_start():
    """Initialize chat session when a user connects."""
    # Initialize empty chat history
    cl.user_session.set("chat_history", [])
    await cl.Message(content="Hello! I'm Summiya Ashraf. How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("chat_history")
    history.append({"role": "user", "content": message.content})
    result = await Runner.run(
        crypto_agent, 
        input=history,
        run_config=config
    )
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("chat_history", history)
    await cl.Message(content=result.final_output).send()




