#%%
import google.generativeai as genai
import datetime

class Gen_AI:
    API_KEY: str = 'AIzaSyBB7-NFo2xh4RlNH7CU4sX3a4CW2zdeHSE'
    def __init__(self ) -> str:
        genai.configure(api_key=self.API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest',
                              generation_config=genai.GenerationConfig(temperature=0.5,))
        
    
    def get_ai_response(self, prompt:str) -> str:
        try:
            ai_response = self.model.generate_content(prompt)
        except Exception as e:
            print(e)
        return ai_response.text
    
#%%
    @staticmethod
    def save_response(ai_response:str, user_prompt:str) -> None:
        now = datetime.datetime.now()
        today = now.date() # Get the date component
        time = now.time() #get the time component

        #Creates a markdown file and writes the response to it 
        with open(fr"C:\Users\01465307\OneDrive - University of Cape Town\Desktop\Google-AI\Text_2_AI\output.md", "a") as file:
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

# %%