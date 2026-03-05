# Made by Sovf!

from openai import OpenAI, OpenAIError

API_Key = input("ChatGPT API Key: ")

OpenAIClient = OpenAI(api_key = API_Key)

print("Welcome to Grammarly!\n")

while True:
    Input = str(input("String: "))

    try:
        OpenAIAnswer = OpenAIClient.responses.create(
            model = "gpt-5.2",
            instructions = "You are a grammarly.",
            input = Input,
        )

        print("Grammared Text:", OpenAIAnswer.output_text, "\n")
    except OpenAIError as Reason:
        print("Err:", Reason.code.upper())
