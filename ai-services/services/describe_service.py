import os
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_prompt_template() -> str:
    template_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "prompts",
        "describe_prompt.txt"
    )
    with open(template_path, "r") as f:
        return f.read()


def generate_description(text: str) -> dict:
    try:
        template = load_prompt_template()
        prompt = template.replace("{input}", text)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )

        result = response.choices[0].message.content

        return {
            "description": result,
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": False
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "description": "Unable to generate description.",
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": True
        }