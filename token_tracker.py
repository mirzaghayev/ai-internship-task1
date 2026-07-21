import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def run_token_tracking_demo():
  system_prompt = (
      "You are an expert AI Physics Tutor. Explain physics concepts simply."
  )
  user_prompt = "What is momentum?"

  print("Sending request and capturing token usage metrics...\n")

  completion = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": user_prompt},
      ],
      temperature=0.3,
      max_tokens=200,
  )

  
  usage = completion.usage

  if usage:
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    #burada input ve output token costlarini hesablamaq olar cost lambda model ucun gotulub
    
    input_cost = (prompt_tokens / 1_000_000) * 0.59
    output_cost = (completion_tokens / 1_000_000) * 0.79
    total_estimated_cost = input_cost + output_cost

    print("--- Token Usage & Cost Analytics ---")
    print(f"Prompt Tokens: {prompt_tokens}")
    print(f"Completion Tokens: {completion_tokens}")
    print(f"Total Tokens Used: {total_tokens}")
    print(f"Estimated Request Cost: ${total_estimated_cost:.6f}")
  else:
    print("[Warning] Usage metadata not found in the completion response.")

  print("\n--- AI Response ---")
  print(completion.choices[0].message.content)


if __name__ == "__main__":
  run_token_tracking_demo()