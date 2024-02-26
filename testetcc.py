from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["SERPAPI_API_KEY"] = "YOUR_SERP_API_KEY" # get your Serp API key here: https://serpapi.com/

OpenAI.api_key = "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"
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("How much energy did wind turbines produce worldwide in 2022?")

