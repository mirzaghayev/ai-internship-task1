import json
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def run_output_parsing_demo():
  #json formatinda isteyen input
  system_prompt = (
      "You are an expert AI Physics Tutor. You must respond ONLY with a valid "
      "JSON object containing three keys: 'core_concept', 'real_world_example', "
      "and 'summary'. Do not include any markdown formatting blocks like "
      "```json or extra text outside the JSON object."
  )

  user_prompt = "Explain what inertia is."

  print("Sending request with JSON response formatting requirement...\n")

  try:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,  # temperaturu asagi saldim
        max_tokens=250,
    )

    raw_response = completion.choices[0].message.content.strip()
    print(f"Raw Model Response:\n{raw_response}\n")

    #
    try:
      parsed_data = json.loads(raw_response)
      print("Successfully Parsed JSON Data:")
      print(f"Core Concept: {parsed_data.get('core_concept')}")
      print(f"Real-World Example: {parsed_data.get('real_world_example')}")
      print(f"Summary: {parsed_data.get('summary')}")

    except json.JSONDecodeError as jde:
      print(
          "[Validation Error] Failed to parse model output as JSON."
          f" Details: {jde}"
      )
      print("Handling corrupted/malformed response fallback...")

  except Exception as e:
    print(f"[API Error] An error occurred during the request: {e}")


if __name__ == "__main__":
  run_output_parsing_demo()