from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o"),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
# Output:
# Running:                                                                                                                                                                                                                                                                         ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃  • transfer_task_to_finance_agent(task_description=Summarize analyst recommendations for NVDA, expected_output=A summary of analyst recommendations, additional_information=NVDA analyst recommendations)                                                                        ┃
# ┃  • transfer_task_to_web_agent(task_description=Get the latest news for NVDA, expected_output=A summary of the latest news, additional_information=NVDA latest news)                                                                                                              ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃                                                                                                                         Analyst Recommendations for NVDA                                                                                                                         ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃ To provide a summary of analyst recommendations for NVDA, I will need to retrieve the data.                                                                                                                                                                                      ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃ Running:                                                                                                                                                                                                                                                                         ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃  • get_analyst_recommendations(symbol=NVDA)                                                                                                                                                                                                                                      ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃                                                                                                                     Analyst Recommendations Summary for NVDA                                                                                                                     ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃ The following table displays the analyst recommendations for NVDA:                                                                                                                                                                                                               ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃   Period   Strong Buy   Buy   Hold   Sell   Strong Sell                                                                                                                                                                                                                          ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                                                                                                                                                         ┃
# ┃   0m       12           47    4      0      0                                                                                                                                                                                                                                    ┃
# ┃   -1m      12           48    4      0      0                                                                                                                                                                                                                                    ┃
# ┃   -2m      12           48    4      0      0                                                                                                                                                                                                                                    ┃
# ┃   -3m      11           48    3      0      1                                                                                                                                                                                                                                    ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃ The data indicates that the majority of analysts recommend buying NVDA, with 47-48 analysts giving a "buy" recommendation and 12 analysts giving a "strong buy" recommendation across the different time periods. There are no "sell" or "strong sell" recommendations. The      ┃
# ┃ number of "hold" recommendations remains consistent at 3-4 across the different periods.                                                                                                                                                                                         ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃                                                                                                                               Latest News for NVDA                                                                                                                               ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃ NVIDIA Corporation (NVDA) recently reported a 33% quarter-over-quarter (QoQ) EPS growth in Q3 2024, driven by exceptional profitability and AI innovation. However, the company's stock tanked on Monday, falling more than 17% and losing nearly $600 billion off its market    ┃
# ┃ cap due to the growing popularity of a new cost-effective artificial intelligence model from the Chinese startup DeepSeek. Despite the negative financial impact, Nvidia praised DeepSeek's breakthrough, calling it an "excellent A.I. advancement and a perfect example of     ┃
# ┃ test time scaling." Additionally, Nvidia stock extended its losses after a report of potential additional curbs on China sales.                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃                                                                                                                                     Sources:                                                                                                                                     ┃
# ┃                                                                                                                                                                                                                                                                                  ┃
# ┃  • Insider Monkey on MSN.com                                                                                                                                                                                                                                                     ┃
# ┃  • AOL                                                                                                                                                                                                                                                                           ┃
# ┃  • Observer                                                                                                                                                                                                                                                                      ┃
# ┃  • AOL         
