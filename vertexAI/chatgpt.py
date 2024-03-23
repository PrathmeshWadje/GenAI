import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY") # enter a api
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    message=[
        {"role": "user", "content": "Provide 5 test data in tabular format which includes ID, Name and City"}
    ]
)
print(completion.choices[0].message['content'])