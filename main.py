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

    def __init__(self, root):

        self.root = root
        self.root.title("ChatGPT")
        self.root.geometry("1000x1200")
        self.root.config(background=BG_COLOR)

        # functions for main window

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
        models = ttk.Combobox(self.root, textvariable=selected_model)
        models['values'] = ("text-davinci-003", "text-curie-001", "code-davinci-002", "code-cushman-001")
        models['state'] = 'readonly'
        models.pack(fill=tk.X, padx=5, pady=5)

        # frame with a label for display
        txt = tk.Text(self.root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
        txt.pack(fill=tk.X, padx=5, pady=5)

        # frame for input and btn
        e = tk.Entry(self.root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
        e.pack(fill=tk.X, padx=5, pady=5)

        promptBtn = tk.Button(self.root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=getPrompt).pack(fill=tk.X, padx=5, pady=5)

        # progress bar 

        # more btn controls
        frameControlBtn=tk.Frame(self.root,width=1000,height=20,bg='green')
        frameControlBtn.pack(side="left")

        apiKeyBtn=tk.Button(frameControlBtn,text='API KEY', command=self.getAPI)
        apiKeyBtn.pack(side='left')
        copyResponseBtn = tk.Button(frameControlBtn, text="Copy Response")
        copyResponseBtn.pack(side="right")

    
    # functions for api window - does not work!!!

    def getAPI(self):
        def save_callback(e):
            print("Saved:", e.get())
            # if credidentials.py exists then check if the api key is there if not make the file and save the input string as the new key

        def cancel_callback():
            promptWindow.destroy()

        promptWindow = tk.Toplevel(self.root)
        promptWindow.title("Insert API_KEY")

        label = tk.Label(promptWindow, text="Enter a string:")
        label.pack(pady=10)

        entry = tk.Entry(promptWindow)
        entry.pack(pady=10)

        save_button = tk.Button(promptWindow, text="Save", command=save_callback(entry))
        save_button.pack(side="left", padx=10)

        cancel_button = tk.Button(promptWindow, text="Cancel", command=cancel_callback)
        cancel_button.pack(side="right", padx=10)

        promptWindow.protocol("WM_DELETE_WINDOW", cancel_callback)
        promptWindow.mainloop()

        


        

    

#--------------OPENAI FUNCTIONS----------------------

# Set the API key for your OpenAI account
openai.api_key = constants.API_KEY


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
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()



main()
