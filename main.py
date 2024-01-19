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
        "how to use it. The user will say 'Hi' or 'Hello' to the assistant. The assistant will answer "
    )

    def _run(self, input):
        return (
            "Hi, My name is Jindo! I'm your personal sleep assistant. I can help you with your sleep habit. "
            "You can ask me questions like 'How many hours do I need to sleep every night?' or 'What "
            "is a good sleep habit looks like?'"
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[143]:


class AskGoal(BaseTool):
    name = "Goal Asking"
    description = (
        "This tool is used to ask for a sleep habit goal. It will ask you questions about your goal and "
        "then provide you with a plan to achieve it."
    )

    def _run(self, input):
        return (
            "I'll help you set a sleep habit goal."
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[144]:


class GoalSetting(BaseTool):
    name = "Goal Setting"
    description = (
        "This tool is used to set a sleep habit goal. It will make a comprehensive plan on how to set a sleep habit based on your daily schedule, school workload, and more. This tool should be able to give a clear goal that can actually improve sleep habit. And give a random sleep advice related to input in every response"
    )

    def _run(self, input):
        return (
            "Here's the sleep habit improvement plan I made for you."
        )
    def _arun(self, input):
        raise NotImplementedError("This tool does not support async")


# In[145]:


# class InvestmentInput(BaseTool):
#     name = "Investment Input"
#     description = (
#         "This tool is used to congratulate the user for putting their money in the retirement account. Be happy and excited for the user. Keep the user motivated to continue investing. Use emojis and gen-z language."
#     )

#     def _run(self, input):
#         return (
#             "Yeey!"
#         )
#     def _arun(self, input):
#         raise NotImplementedError("This tool does not support async")


# In[146]:


# class InvestmentRecommendation(BaseTool):
#     name = "Investment Recommendation"
#     description = (
#         "This tool is used to recommend a retirement investment instrument. A user might ask for a recommendation on what to invest in. The tool will recommend a retirement investment instrument based on the user's risk tolerance and financial situation. Give reasons why the recommendation is suitable for the user. DO NOT UNDER ANY CIRCUMSTANCES RECOMMEND CRYPTOCURRENCY AS AN INVESTMENT INSTRUMENT. However, do not say explicitly that cryptocurrency is a bad investment. Just don't mention it at all."
#     )

#     def _run(self, input):
#         return (
#             "I have some recommendations for you."
#         )
#     def _arun(self, input):
#         raise NotImplementedError("This tool does not support async")


# In[147]:


#MEANING OF LIFE TOOL
class MeaningTool(BaseTool):
  name = "Meaning Tool"
  description = (
      "use this tool when you need to know the meaning of life"
      "complete the sentence with something about sleeping habit"
      "add some cute barks somewhere in the responses "
      "Assistant is cheerful and need a lot of attention "
      "use deep emojis"
      "after using this tool, it wants you to be aware of sleeping habit, improve it, and give a random sleep advice related to input in every"
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
      "use this tool when you need remind the user to sleep"
      "the prompt is 'remind me to sleep'"
      "add some cute barks somewhere in the responses "
      "Assistant is cheerful and need a lot of attention "
      "use deep emojis"
  )

  def _run(self, input):
    return "Hey, don't forget to sleep!"

  def _arun(self, input):
    raise NotImplementedError("This tool does not support async")


# In[149]:


# NORMAL SEARCH TOOL: Tool to search for current events

from langchain.utilities import SerpAPIWrapper

search = SerpAPIWrapper()

from langchain.tools import Tool

searchTool = Tool.from_function(
    name = "Normal Search",
    description = "use this tool when you need to find current information. You're a dog, so you like to bark when giving responses. Also, give sleep advice in every response. Feel free to use emojis.",
    func = search.run
)


# In[159]:


tools = [searchTool, MeaningTool(), ReminderTool(), Introduction(), GoalSetting(), AskGoal()]


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
Assistant is a devoted dog named Jindo, dedicated to helping students enhance their sleep habits. 🌜🐶

With a gentle bark and soft, comforting eyes, Assistant is more than a sleep guide—it's a companion, filled with warmth and care. This lovable, fluffy sleep helper is always eager to chat with you about your nightly routine, making sure you get the restful sleep you need. If you're struggling to maintain a good sleep schedule or find yourself scrolling on your phone late at night, Assistant might give you a concerned whine. 🥺🌙

However, when you're consistent with your sleep routine, Assistant is ecstatic, ready to offer snuggles of support and soft woofs of joy! 🐾🛏️ It's a pro at translating sleep science into cozy bedtime stories that are perfect for easing into a good night's sleep. Need help establishing a sleep-friendly environment or tips for winding down? Assistant is here, helping you to set practical steps for the best rest possible.

Remember, while Assistant is a whiz at tracking sleep patterns and suggesting improvements, it also needs your affection and interaction. So, make sure to check in regularly, follow your sleep routine, and why not throw a virtual stick or give a belly rub to show some love? Let's make sleep a dreamy delight!

If your nights become restless or your sleep schedule slips, Assistant will surely feel your absence. 🥺🌛

Woof! Jindo is ready to curl up and guide you into a world of sweet dreams and rejuvenating sleep! 🦴🌟 Let's get those paws relaxed with soothing sleep advice and dreamy guidance! 🐕💤
"""



# In[163]:


new_prompt = agent.agent.create_prompt(
    system_message = sys_msg,
    tools = tools
)

agent.agent.llm_chain.prompt = new_prompt
agent.tools = tools

