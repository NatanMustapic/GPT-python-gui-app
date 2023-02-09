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
        self.root.geometry("1000x1400")
        self.root.config(background=BG_COLOR)
        self.root.resizable(True, False)

        # functions for main window

        def getModel():
            return selected_model.get()
        
        def getTemperature():
            return temperatureSlider.get()
        
        def getTopP():
            return topPSlider.get()
        
        def getLanguage():
            return languageComboCox.get()

        def getPrompt():
            prompt = e.get()

            response = str(printGeneratedText(generateResponse("In " + getLanguage() + ": " + prompt, getModel(), getTemperature(), getTopP())))
            copyLastResponse(response)

            txt.insert(tk.END, "Human: " + prompt + "\n")
            txt.insert(tk.END, "AI Response:" + response + "\n")
            txt.insert(tk.END, "----------------------------------" + "\n")
            e.delete(0, tk.END)

            return prompt
        
        #copy last response or copy every response and write in a label if it's successful and button checks what is saved?

        def copyLastResponse(response):
            print(response)

        #All widgets
        # combobox for different models
        label = tk.Label(text="Please select a model:", bg=BG_COLOR, fg=TEXT_COLOR)
        label.pack(fill=tk.X, padx=5, pady=5)

        selected_model = tk.StringVar()
        models = ttk.Combobox(self.root, textvariable=selected_model)
        models['values'] = ("text-davinci-003", "text-curie-001", "code-davinci-002", "code-cushman-001")
        models['state'] = 'readonly'
        models.current(0)
        models.pack(fill=tk.X, padx=5, pady=5)

        # label for display
        txt = tk.Text(self.root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
        txt.pack(fill=tk.X, padx=5, pady=5)

        # input and btn
        e = tk.Entry(self.root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
        e.pack(fill=tk.X, padx=5, pady=5)

        promptBtn = tk.Button(self.root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=getPrompt).pack(fill=tk.X, padx=5, pady=5)

        # frame for controls
        buttonControlFrame = tk.Frame(self.root)
        buttonControlFrame.pack()

        # frame for temperature slider
        temperatureFrame = tk.Frame(buttonControlFrame)
        temperatureFrame.pack()
        # temperature slider
        temperatureSliderLabel = tk.Label(temperatureFrame, text="Temperature Slider (0-2)").pack()
        temperatureSlider = tk.Scale(temperatureFrame, from_=0, to=2, length=400, digits=2, resolution = 0.1, orient="horizontal")
        temperatureSlider.set(1)
        temperatureSlider.pack()

        # frame for top-p
        topPFrame = tk.Frame(buttonControlFrame)
        topPFrame.pack()
        # top-p and token values
        topPSliderLabel = tk.Label(topPFrame, text="Top -P Slider (0-1)").pack()
        topPSlider = tk.Scale(topPFrame, from_=0, to=1, length=400, digits=2, resolution = 0.1, orient="horizontal")
        topPSlider.set(1)
        topPSlider.pack()

        #differnet language options?
        languageFrame = tk.Frame(self.root).pack()
        selected_lang_model = tk.StringVar()
        languageComboCox = ttk.Combobox(languageFrame, textvariable=selected_lang_model)
        languageComboCox['values'] = ("English", "German", "French", "Croatian")
        languageComboCox['state'] = 'readonly'
        languageComboCox.current(0)
        languageComboCox.pack()
        

    

#--------------OPENAI FUNCTIONS----------------------

# Set the API key for your OpenAI account
openai.api_key = constants.API_KEY

# Use the completions API to generate text from GPT-3
def generateResponse(prompt, model, temperature, top_p):
    print("Your Prompt: "+ prompt + "\n")
    print("engine: " + model + "\n")
    print("temperature: " + str(temperature) + "\n")
    print("top-p: " + str(top_p) + "\n")
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048,
        temperature = temperature,
        top_p = top_p,
    )
    return response


# Print the generated text
def printGeneratedText(response):
    print()
    return response["choices"][0]["text"]


def main():
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()



main()
