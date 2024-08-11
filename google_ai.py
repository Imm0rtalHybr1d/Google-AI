import google.generativeai as genai
import os
import datetime
# Replace YOUR_API_KEY with your actual API key that you can get from https://cloud.google.com/
API_KEY: str = "AIzaSyBB7-NFo2xh4RlNH7CU4sX3a4CW2zdeHSE"
genai.configure(api_key=API_KEY)
model: genai.GenerativeModel = genai.GenerativeModel('gemini-1.5-flash')

previous_prompt = ""

"""This function gives the user a brief on how to create a prompt 
   and then asks use to create their prompt """
def get_topic() -> str:
    prompt_file_path: str = f'prompt_tips.txt'
    with open(prompt_file_path, mode='r') as file:
        for line in file:
            print(f'{line}',end="")

    print('')
    print('')
    
    while True:
        user_prompt: str = input(f"Done reading > type 'yes' to continue:")
        if user_prompt.lower() == 'yes':
            os.system(r'cls')
            user_prompt: str = input(f"Ask me anything ... \n")
            return user_prompt
        else:
            continue
    

"""Gets the dafualt prompt, this is the base prompt that tells the AI how we want our answer"""
def read_prompt() -> str: 
    default_prompt: str
    with open (fr'C:/Users/Hano/Desktop/Google AI/prompt_creation.md', mode='r') as file:
        for line in file:
            default_prompt = line
    return default_prompt

"""Writes user's prompt to a txt file
    Simply writes the user prompt, time and date"""
def log_user_prompt(user_prompt:str) -> None:    
    # Get the current date and time
    now = datetime.datetime.now()

    today = now.date() # Get the date component
    time = now.time() #get thge time component
    
    with open('C:/Users/Hano/Desktop/Google AI/users_prompt.txt', mode='a') as file:
        file.write(f"User's prompt: {user_prompt} | Date:{str(today)} | Time: {str(time.strftime("%H:%M"))} \n")
        

"""This functions takes a prompt (optionally) or allows user to enter a prompt"""
def get_prompt(full_prompt:str|None = None) -> None:
    global previous_prompt
    
    while True:
        if full_prompt is None:
            print(f"Ask me anything (or type 'exit' to quit): \n") #tell user to give us a prompt
            user_prompt: str = input() #get user's request
            print(f'{'':_^30}')

            if user_prompt == 'exit'.lower():
                print('Exiting...')
                break

            print(f'{''}')
            default_prompt: str = read_prompt() #get the basic propmt which tells our ai how to provide the information to the user
            full_prompt = default_prompt+". User prompt: "+user_prompt
            
            #sends the full prompt to google ai
            response: genai.Response = model.generate_content(full_prompt)
            ai_response: str = response.text
            print(ai_response)  #output google response                  
            
            # log_user_prompt(user_prompt) #logs user prompt to a txt file with data and time, for analytics

            save_response(ai_response, user_prompt) #calls function that save's AI response to a markdown file for later 
        else:
            response: genai.Response = model.generate_content(full_prompt)
            ai_response: str = response.text
            print(ai_response)  #output google response                  
            
            # log_user_prompt(full_prompt)
            save_response(ai_response, full_prompt) #calls function that save's AI response to a markdown file for later 
        full_prompt = None
        continue
    
         
def save_response(ai_response:str, user_prompt:str) -> None:
    now = datetime.datetime.now()
    today = now.date() # Get the date component
    time = now.time() #get the time component

    #Creates a markdown file and writes the response to it 
    with open("output.md", "a") as file:
        file.write(f"User's prompt: {user_prompt} | Date:{str(today)} | Time: {str(time.strftime("%H:%M"))} \n")
        print(f'{'':_^30}')
        print('')
        file.write(f"{'**AI response:**'}\n")
        for line in ai_response.splitlines():
            
            file.write(f"{line}\n")
        file.write(f"{'':_^30}\n")    
        print('Info saved to output.md')
        print(f'{'':_^70}')
        print('')



def main():
    os.system(r'cls')
    want_ptompt: str = input("Would you like to be assisted with creating a promt: y/n ")
    if want_ptompt.lower() == 'y':
        user_promt: str = get_topic()
        get_prompt(user_promt)      
    else:
        get_prompt()
    

if __name__ == "__main__":
    main()
