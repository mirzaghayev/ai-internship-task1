import os
import time
from dotenv import load_dotenv
#groqdan errorucun lazim olanlari elave edirik
from groq import APIConnectionError, APIError, Groq, RateLimitError


load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def run_with_retry(max_retries=3, delay=2):
  
  
  system_prompt = (
      "You are an expert AI Physics Tutor. Explain physics concepts simply."
  )
  user_prompt = "What is the conservation of energy?"

  for attempt in range(1, max_retries + 1):
    
    try:
      
      print(
          f"Attempt {attempt} of {max_retries}: Sending request to Groq API..."
      )

      # api ucun yoxlama
      completion = client.chat.completions.create(
          model="llama-3.3-70b-versatile",
          messages=[
              {"role": "system", "content": system_prompt},
              {"role": "user", "content": user_prompt},
          ],
          temperature=0.3,
          max_tokens=200,
      )

      print("\n--- Success! AI Response ---")
      print(completion.choices[0].message.content)
      return  

    except RateLimitError as e:
      print(
          f"[Rate Limit Error] Hit rate limit. Waiting {delay} seconds before"
          f" retrying... Details: {e}"
      )
      time.sleep(delay)
      delay *= 2 

    except APIConnectionError as e:
      print(
          f"[Connection Error] Failed to connect to server. Retrying in"
          f" {delay} seconds... Details: {e}"
      )
      time.sleep(delay)

    except APIError as e:
      print(f"[Groq API Error] Status Code {e.status_code}: {e.message}")
      break 

    except Exception as e:
      print(f"[Unexpected Error] An unexpected error occurred: {e}")
      break


if __name__ == "__main__":
  run_with_retry()