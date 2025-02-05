import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "How to stop the ollama service from my MacOS?",
        },
    ],
)

response_content = response["message"]["content"]
# print(response)

# Write the response to the file in Markdown format
with open("./_tmp/_out_ai/_current.md", "w") as file:
    file.write(f"### Response\n\n{response_content}")
