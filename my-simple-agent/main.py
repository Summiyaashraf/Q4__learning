from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

# step 01
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

# step 02

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client= external_client
)

# step 03

config = RunConfig(
    model= model,
    model_provider=external_client,
    tracing_disabled=True
)

# step 04

agent = Agent(
    name= "python expert",
    instructions="You are a Python Programmer.."
)

# step 05
result= Runner.run_sync(
    agent,
    input="Hello, how are you?",
    run_config=config
)
# step 06

print(result.final_output)

