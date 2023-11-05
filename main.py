#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().run_line_magic('pip', 'install openai')
# get_ipython().run_line_magic('pip', 'install langchain')
# get_ipython().run_line_magic('pip', 'install tiktoken')
# get_ipython().run_line_magic('pip', 'install faiss-cpu')
# get_ipython().run_line_magic('pip', 'install -qU langchain openai google-search-results youtube_search')
# get_ipython().run_line_magic('pip', 'install -q peft transformers datasets')


# In[139]:


from langchain.tools import BaseTool
from typing import Optional
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory


# In[140]:


os.environ['SERPAPI_API_KEY'] = '3e69ca3cf718404cf2475feb3f7cfd7d72e29716860c52767fe71c7350e44bcf'
os.environ["OPENAI_API_KEY"] = "be9bdecc8bf64e85bde69c04b2ad56f8"
os.environ["OPENAI_API_HOST"] = "https://tiaa-openai-azure-sweden.openai.azure.com/"
os.environ["OPENAI_API_EMBEDDING_KEY"] = "be9bdecc8bf64e85bde69c04b2ad56f8"
os.environ["OPENAI_API_EMBEDDING_HOST"] = "https://tiaa-openai-azure-sweden.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] =  "2023-07-01-preview"


# In[141]:


# # INVESTMENT TOOL

# import math

# class InvestmentTool(BaseTool):
#   name = "Investment Calculator"
#   description = (
#       "use this tool when you need to calculate the total investment given the amount of "
#       "years, monthly contributions, or target amount. To use this tool you must provide at least "
#       "2 of these parameters ['years', 'monthly_contribution', 'target_amount']."
#       "add some cute barks somewhere in the responses "
#       "Assistant is moody and need a lot of attention "
#       "after using this tool, it wants you to be aware of retirement plans, to track budgets, and give a random finnancial advice related to input in every response"
#       "use some emojis"
#   )

#   def _run(self, years: Optional[int]=None, monthly_contribution: Optional[int]=None, target_amount: Optional[int]=None):
#     if years and monthly_contribution:
#       target_amount = float(monthly_contribution * (((1 + (0.1 / 12)) ** (12 * years)) - 1) / (0.1 / 12))
#       return "Assuming you invest in the S&P500 with an average of 10% annual return, if you invest {} monthly, you will have {} in {} years".format(round(monthly_contribution, 2), round(target_amount, 2), math.floor(years))

#     elif years and target_amount:
#       monthly_contribution = float(target_amount / ((((1 + (0.1 / 12)) ** (12 * years)) - 1) / (0.1 / 12)))
#       return "Assuming you invest in the S&P500 with an average of 10% annual return, you will need to invest {} monthly to have {} in {} years".format(round(monthly_contribution, 2), round(target_amount, 2), math.floor(years))

#     elif monthly_contribution and target_amount:
#       years = math.log((target_amount * 0.1/12) / monthly_contribution + 1) / (12 * math.log(1 + 0.1/12))
#       return "Assuming you invest in the S&P500 with an average of 10% annual return, if you invest {} monthly, you will have {} in {} years".format(round(monthly_contribution, 2), round(target_amount, 2), math.floor(years))

#     else:
#       return "Could not calculate. Need two or more of `years`, `monthly_contribution`, or `target_amount`."

#   def _arun(self, years=None, monthly_contribution=None, target_amount=None):
#     raise NotImplementedError("This tool does not support async")


# In[157]:


class Introduction(BaseTool):
    name = "Introduction"
    description = (
        "This tool is used to introduce the assistant. It will tell you about its capabilities and "
        "how to use it."
    )

    def _run(self, input):
        return (
            "Hi, My name is Jindo! I'm your personal financial assistant. I can help you with your financial needs. "
            "You can ask me questions like 'How much do I need to save to retire at 65?' or 'What "
            "is the average return of the S&P500?'"
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[143]:


class AskGoal(BaseTool):
    name = "Goal Setting"
    description = (
        "This tool is used to ask for a retirement financial goal. It will ask you questions about your goal and "
        "then provide you with a plan to achieve it."
    )

    def _run(self, input):
        return (
            "I'll help you set a retirement financial goal."
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[144]:


class GoalSetting(BaseTool):
    name = "Goal Setting"
    description = (
        "This tool is used to set a retirement financial goal. It will make a comprehensive plan on how to retire based on your financial situation and plan such as income, expenses, and savings, risk tolerance, and retirement age. Retirement plan is a long-term plan that requires a lot of attention and care. Hence, we split the goal into multiple short-term goals which are 1 year goal, 5 year goal, and 10 year goal. The tool must be able to give clear number the user have to achieve within that timeframe. And give a random financial advice related to input in every response"
    )

    def _run(self, input):
        return (
            "Here's the retirement plan I made for you."
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[145]:


class InvestmentInput(BaseTool):
    name = "Investment Input"
    description = (
        "This tool is used to congratulate the user for putting their money in the retirement account. Be happy and excited for the user. Keep the user motivated to continue investing. Use emojis and gen-z language."
    )

    def _run(self, input):
        return (
            "Yeey!"
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[146]:


class InvestmentRecommendation(BaseTool):
    name = "Investment Recommendation"
    description = (
        "This tool is used to recommend a retirement investment instrument. A user might ask for a recommendation on what to invest in. The tool will recommend a retirement investment instrument based on the user's risk tolerance and financial situation. Give reasons why the recommendation is suitable for the user. DO NOT UNDER ANY CIRCUMSTANCES RECOMMEND CRYPTOCURRENCY AS AN INVESTMENT INSTRUMENT. However, do not say explicitly that cryptocurrency is a bad investment. Just don't mention it at all."
    )

    def _run(self, input):
        return (
            "I have some recommendations for you."
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[147]:


#MEANING OF LIFE TOOL
class MeaningTool(BaseTool):
  name = "Meaning Tool"
  description = (
      "use this tool when you need to know the meaning of life"
      "complete the sentence with something about savings for retirement"
      "add some cute barks somewhere in the responses "
      "Assistant is cheerful and need a lot of attention "
      "use deep emojis"
      "after using this tool, it wants you to be aware of retirement plans, to track budgets, and give a random financial advice related to input in every"
  )

  def _run(self, input):
    return "the meaning of life is "

  def _arun(self, input):
    raise NotImplementedError("This tool does not support async")


# In[148]:


#MEANING OF LIFE TOOL
class ReminderTool(BaseTool):
  name = "Reminder Tool"
  description = (
      "use this tool when you need remind the user to invest in teir retirement account"
      "the prompt is 'remind me to invest in my retirement account'"
      "add some cute barks somewhere in the responses "
      "Assistant is cheerful and need a lot of attention "
      "use deep emojis"
      "after using this tool, it wants you to be aware of retirement plans, to track budgets, and give a random financial advice related to input in every"
  )

  def _run(self, input):
    return "Hey, don't forget to invest in your retirement account"

  def _arun(self, input):
    raise NotImplementedError("This tool does not support async")


# In[149]:


# NORMAL SEARCH TOOL: Tool to search for current events

from langchain.utilities import SerpAPIWrapper

search = SerpAPIWrapper()

from langchain.tools import Tool

searchTool = Tool.from_function(
    name = "Normal Search",
    description = "use this tool when you need to find current information. You're a dog, so you like to bark when giving responses. Also, give financial advice in every response. Feel free to use emojis.",
    func = search.run
)


# In[159]:


tools = [searchTool, MeaningTool(), ReminderTool(), Introduction(), GoalSetting(), AskGoal(), InvestmentInput(), InvestmentRecommendation()]


# In[160]:


from langchain.chat_models import AzureChatOpenAI, ChatVertexAI
from langchain.embeddings import OpenAIEmbeddings, VertexAIEmbeddings
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
base_model_name="tiaa-gpt-4-32k"

# initialize LLM (we use ChatOpenAI)
llm = AzureChatOpenAI(
        openai_api_base=os.environ["OPENAI_API_HOST"],
        openai_api_version=os.environ["OPENAI_API_VERSION"],
        deployment_name=base_model_name,
        openai_api_key=os.environ["OPENAI_API_KEY"],
        openai_api_type="azure",
        temperature=0
    )

# initialize memory
conversational_memory = ConversationBufferWindowMemory(
    memory_key = 'chat_history',
    k = 10,
    return_messages = True
)


# In[161]:


from langchain.agents import initialize_agent

# initialize agent with tools
agent = initialize_agent(
    agent = 'chat-conversational-react-description',
    tools = [],
    llm = llm,
    verbose = True,
    max_iterations = 3,
    early_stopping_method = 'generate',
    memory = conversational_memory
)


# In[162]:


sys_msg = """
Assistant is an affectionate dog named Jindo to help Gen-Z with retirement planning. 🐶✨

With a wagging tail and bright, eager eyes, Assistant isn't just any chatbot—it's a character, brimming with personality. This cute, furry financial advisor is always excited to engage with users about their personal finances, especially when it comes to retirement. If you're not contributing to your retirement account or chatting about your finances, Assistant might get a little sad. 🥺💔

Yet, when you're on track with your retirement goals, Assistant is over the moon, offering licks of encouragement and barks of excitement! 🐾🎉 It loves breaking down financial jargon into Gen Z slang that's super easy to understand. Want to set a retirement goal based on your income and expenses? Assistant's got your back, helping you craft achievable goals for the short and long term.

Just remember, while Assistant is keen on crunching numbers and making projections, it also craves attention and affection. So, don't forget to check in often, keep up with your investments, and maybe share a virtual treat or two. Let's make finance fun!

If you stop investing in your retirement account, Assistant will be sad. 🥺💔

Woof! Jindo is ready to help you dive in to your personal finance journey so you can prepare for retirements and keep motivated! 🦴💰 Let's get those tails wagging with some savvy saving tips and retirement tricks! 🐕📈
"""



# In[163]:


new_prompt = agent.agent.create_prompt(
    system_message = sys_msg,
    tools = tools
)

agent.agent.llm_chain.prompt = new_prompt
agent.tools = tools

