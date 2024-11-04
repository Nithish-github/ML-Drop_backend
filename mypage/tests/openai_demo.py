import openai  # Correct import

# Set your OpenAI API key
openai.api_key = "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"

# Create a completion request using the OpenAI API
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use 'gpt-3.5-turbo' or 'gpt-4'
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ]
)

# Extract the response
response = completion['choices'][0]['message']['content']

# Print the response
print(response)
