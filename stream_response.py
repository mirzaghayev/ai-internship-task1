import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def run_streaming_demo():
    #suali define edirik
  system_prompt = (
      "You are an expert AI Physics Tutor. Explain physics concepts simply"
      " and clearly."
  )
  user_prompt = "Explain what is buoyancy?."

  print("Streaming response from AI:\n")

  #streaming teleb edirik
  stream = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": user_prompt},
      ],
      
      
      temperature=0.3,
      max_tokens=300,
      stream=True,  # stream mode on
  )

  for chunk in stream:
    
    content = chunk.choices[0].delta.content
    if content:
      print(content, end="", flush=True)

  print("\n\nstream bitdi.")


if __name__ == "__main__":
  run_streaming_demo()