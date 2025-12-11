from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from Tools import expand_prompt_tool, generate_manga_tool

# Agent LLM must exist but does minimal work – tools do heavy work.
controller_llm = Ollama(model="llama3")

manga_agent = initialize_agent(
    tools=[expand_prompt_tool, generate_manga_tool],
    llm=controller_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
