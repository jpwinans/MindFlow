import chainlit as cl
from agent import Agent
from utils import save_file
from time import time


@cl.on_chat_start
async def start_chat():
    bot_agent = Agent("Athena", "athena")
    cl.user_session.set("bot_agent", bot_agent)
    await cl.Avatar(name="Athena", path="mindflow/assets/athena.png").send()
    response = await cl.AskUserMessage(
        author="Athena", content="Hello. To whom am I speaking? Please type your name."
    ).send()
    user_name = response["content"]
    user_agent = Agent(user_name, user_name.lower().replace(" ", "_"))
    cl.user_session.set("user_agent", user_agent)
    if user_agent.get_current_profile() is None:
        await cl.Message(
            author="Athena",
            content=f"Hello {user_name}. I am Athena. It doesn't look like we've met. I am here to help. What's on your mind?",
        ).send()
    else:
        await cl.Message(
            author="Athena",
            content=f"Hello {user_name}. It's nice to see you again. What's on your mind?",
        ).send()


@cl.on_message
async def message(message):
    user_agent = cl.user_session.get("user_agent")
    bot_agent = cl.user_session.get("bot_agent")
    handle_user_message(message, user_agent, bot_agent)
    update_system_message()
    await generate_bot_response(message, user_agent, bot_agent)


def handle_user_message(message, user_agent, bot_agent):
    user_agent.add_message(user_agent.agent_id, message)
    bot_agent.add_message(user_agent.agent_id, message)
    save_file(f"chat_logs/chat_{time()}_{user_agent.agent_id}.txt", message)
    # add message to main scratchpad - could get from messages?


def update_system_message():
    relevant_knowledge = "No relevant knowledge found."
    # check for any relevant knowledge to apply to recent conversation
    # system message = default bot prompt + relevant knowledge + user profile + full scratchpad
    # apply to bot_agent profile



async def generate_bot_response(message, user_agent, bot_agent):
    pass
