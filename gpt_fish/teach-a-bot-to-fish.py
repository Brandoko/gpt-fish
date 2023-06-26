from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv
from langchain.agents.agent_toolkits import GmailToolkit

load_dotenv()

llm = OpenAI(temperature=0)

toolkit = GmailToolkit()
tools = load_tools(["serpapi", "llm-math"], llm=llm) + toolkit.get_tools()

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run(
    "lookup the runtime of avatar 2. Convert that to number to seconds and send the result to kocurbrandon@gmail.com"
)
