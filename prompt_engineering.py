import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def run_physics_tutor_demo():
    #persone yaratmaq ucun sistem promptu
  system_prompt = (
      "You are an expert AI Physics Tutor. Explain physics concepts simply "
      "and clearly. Always format your response using this exact structure:\n"
      "1. Core Concept: (A simple sentence explaining the idea)\n"
      "2. Real-World Example: (A brief everyday example)\n"
      "3. Summary: (A short final takeaway)"
  )

  # ai ucun vereceyi sual ve cavab ucun numune
  few_shot_messages = [
      {
          "role": "user",
          "content": "What is friction?",
      },
      {
          "role": "assistant",
          "content": (
              "1. Core Concept: Friction is a force that opposes the motion "
              "of two objects sliding past each other.\n"
              "2. Real-World Example: Rubbing your hands together to generate "
              "heat on a cold day.\n"
              "3. Summary: Friction slows things down and creates heat."
          ),
      },
  ]

  # sual
  target_user_prompt = "What is event horizon?"

  messages = [{"role": "system", "content": system_prompt}]
  messages.extend(few_shot_messages)
  messages.append({"role": "user", "content": target_user_prompt})

  print("Asking the AI Physics Tutor...\n")

  completion = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=messages,
      temperature=0.3,
      max_tokens=300,
  )

  print("--- AI Physics Tutor Response ---")
  print(completion.choices[0].message.content)


if __name__ == "__main__":
  run_physics_tutor_demo()