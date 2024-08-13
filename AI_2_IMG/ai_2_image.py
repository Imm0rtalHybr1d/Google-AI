# %markdown
"""
This program main function is to let user:
insert image > contact google cloud > explain image
It uses the google.generativeai module to contact google AI API
It uses Tinker to open the file explorer so that the user can select their Image
and uses PIL module to load images 

Key points:

Using tkinter module:
The tkinter.Tk() object is created and withdrawn to prevent a visible window from appearing.
The filedialog.askopenfilename() function opens a file selection dialog with specified file types.
The selected file path is stored in the Image_path variable.
You can then use the Image_path to open the image or perform other operations.
This code provides a simple and effective way to let the user select an image file using the standard file explorer dialog.

Using google generative AI:
Import google.generativeai as genai to get access to the ai 
We use .configure(api_key=API_KEY) is used to configure it to work with our API key 
and we select the ai model with model = genai.GenerativeModel('gemini-1.5-pro-latest')
We also create a prompt - basically telling google generative ai what to do with our image
"""


# %%
import google.generativeai as genai
import PIL.Image
import os #used to view, make and list directories
import tkinter as tk
from tkinter import filedialog


#  %%
#accesses api key
#configuring google ai
API_KEY: str = 'AIzaSyBB7-NFo2xh4RlNH7CU4sX3a4CW2zdeHSE'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest',generation_config=genai.GenerationConfig(temperature=0.5,))


# %% 
# """load image"""
root = tk.Tk()
root.withdraw()

# Get the file path from the dialog
Image_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
if Image_path:
    print("Selected image:", Image_path)

#opens the image in python and stores it in img  
img = PIL.Image.open(Image_path)
img


# %%
prompt = """Given the picture, describe the picture as thoroughly as possible based on what you
see in the image, making sure to note all of the features. Return output in markdown format with headings and subheadings."""


ai_response = model.generate_content([prompt, img])

print(ai_response.text)
root.mainloop()  

