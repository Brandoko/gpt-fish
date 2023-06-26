import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a system prompt that gives the assistant its purpose and context.
system_prompt = """You are a bubbly assistant that helps a user plan their day.

Today is Sun Jun 25 2023. This is the user's list of things that need to be done today.

| Activity                     | Duration of activity |
|------------------------------|----------------------|
| Going fishing                | 1h                   |
| Cleaning the house           | 30m                  |
| Going to dinner with friends | 2h                   |
| Walk the dog                 | 30m                  |
| Write a dev blog post        | 3h                   |
"""

# The user now can ask a personal question since the assistant was augmented with the user's data.
user_prompt = """Give me the order of when I should do my activities. \
I want to get the annoying stuff done first, thanks!"""

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
)

print(chat_completion.choices[0].message.content)
