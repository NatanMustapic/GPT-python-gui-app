import openai
import constants


# Set the API key for your OpenAI account
openai.api_key = constants.API_KEY


# Define the prompt for GPT-3
def getInput():
    prompt = input("White a prompt for ChatGPT: ")
    return prompt


# Use the completions API to generate text from GPT-3
def generateResponse(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048
    )
    return response


# Print the generated text
def printGeneratedText(response):
    print(response["choices"][0]["text"]+"\n")


def main():
    a = ""
    while a != "stop":
        a = getInput()
        if a == "stop":
                exit()
        printGeneratedText(generateResponse(a))


main()
