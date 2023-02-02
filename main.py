import openai
import constants

#Importing tkinter
import tkinter as tk
from tkinter import ttk


#Default Theme
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

#--------------TKINTER FUNCTIONS----------------------

#Create a tkinter class

class MyGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ChatGPT")
        self.window.geometry("1000x1100")
        self.window.config(background=BG_COLOR)

        def getModel():
            return selected_model.get()

        def getPrompt():
            prompt = e.get()
            print(prompt)

            
            txt.insert(tk.END, "Human: " + prompt + "\n")
            txt.insert(tk.END, "AI Response:" + str(printGeneratedText(generateResponse(prompt, getModel()))) + "\n")
            txt.insert(tk.END, "----------------------------------" + "\n")
            e.delete(0, tk.END)

            return prompt

        #All widgets
        
        # label
        label = tk.Label(text="Please select a model:", bg=BG_COLOR, fg=TEXT_COLOR)
        label.pack(fill=tk.X, padx=5, pady=5)

        # combobox
        selected_model = tk.StringVar()
        models = ttk.Combobox(self.window, textvariable=selected_model)
        models['values'] = ("text-davinci-003", "text-curie-001", "code-davinci-002", "code-cushman-001")
        models['state'] = 'readonly'
        models.pack(fill=tk.X, padx=5, pady=5)

        # frame with a label for display
        txt = tk.Text(self.window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
        txt.pack(fill=tk.X, padx=5, pady=5)

        # frame for input and btn
        e = tk.Entry(self.window, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
        e.pack(fill=tk.X, padx=5, pady=5)

        promptBtn = tk.Button(self.window, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=getPrompt).pack(fill=tk.X, padx=5, pady=5)

        # progress bar 

        # more btn controls
        
        self.window.mainloop()

        

    
    


#--------------OPENAI FUNCTIONS----------------------

# Set the API key for your OpenAI account
openai.api_key = constants.API_KEY


# Define the prompt for GPT-3
def getInput():
    prompt = input("White a prompt for ChatGPT: ")
    return prompt


# Use the completions API to generate text from GPT-3
def generateResponse(prompt, model):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048
    )
    return response


# Print the generated text
def printGeneratedText(response):
    print(response["choices"][0]["text"]+"\n")
    return response["choices"][0]["text"]


def main():
    MyGUI()


    a = ""
    while a != "stop":
        a = getInput()
        if a == "stop":
                exit()
        printGeneratedText(generateResponse(a))


main()
