#%%
import google.generativeai as genai
import tkinter as tk
from tkinter import filedialog
from genAI import Gen_AI

#%% """Initialize instance of Gen_ai class"""
myAI: Gen_AI = Gen_AI()

#%%
try:
# %% """load file via file explorer using tkinter module"""
# - asks user to select file to upload
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("*all files", "*.*")])
    file_name= file_path.split('/')[-1]
    print(f'this is the file name >> {file_name}')
    print(f'{''}')

    #%% """Prepare file to upload to GenAI File API"""
    display_name = "tesdst"
    name = 'test'
    file_response = genai.upload_file(path=file_path, name=name, display_name=display_name) 
    print(f"Uploaded file {file_response.display_name} as: {file_response.name}")

    #%% """Verify the file is uploaded to the API"""
    print('Checking if file has been uploaded properly...')
    get_file = genai.get_file(name=name) 
    print(f"Retrieved file {get_file.display_name} as: {get_file.uri}")

    # %% 
    # Make Gemini 1.5 API LLM call
    print(f'{''}')
    print('Make Gemini 1.5 API LLM call...')
    prompt = "describe the file as thoroughly as possible based on what you see in the file, making sure to note all of the main points and give a brief discription of that poin. Return output in markdown format with headings and subheadings"
    response = myAI.model.generate_content([prompt, file_response])
    response_text: str = response.text
    print(response.text)
    print(f'{''}')
    
    #%%
    # """Calling a function that saves the prompt and response"""
    myAI.save_response(response_text, prompt)

    #%%
    #this function list all the files in that hasnt been deleted after being uploaded
    files = list(genai.list_files()) #gets a list of all the files
    print('All files: ', [file.name for file in files]) #retreives filenames from within the list of files
    print(f'{''}')
    
#%%
    # Delete the file after use
    if len(files) != 0:
        genai.delete_file(name=name)
        print(f'Deleted {name} after use ')
    else:
        print("No files to delete")

    root.mainloop()  

# %%
except Exception as e:
    print('exception caught', e)