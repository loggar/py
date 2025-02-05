from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    # required but ignored
    api_key="ollama",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="deepseek-r1:8b",
)

print(chat_completion)
