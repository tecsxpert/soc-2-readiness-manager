import os
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv
from services.cache_service import get_from_cache, set_in_cache

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
    # Step 1 - Check cache first
    cached = get_from_cache("describe", text)
    if cached:
        return cached

    try:
        # Step 2 - Load prompt template
        template = load_prompt_template()
        prompt = template.replace("{input}", text)

        # Step 3 - Call Groq API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a SOC 2 compliance expert. Always respond in professional formal language."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1000,
            timeout=30
        )

        # Step 4 - Extract AI response
        description = response.choices[0].message.content

        # Step 5 - Build result
        result = {
            "input": text,
            "description": description,
            "word_count": len(description.split()),
            "generated_at": datetime.utcnow().isoformat(),
            "status": "success",
            "is_fallback": False,
            "cached": False
        }

        # Step 6 - Save to cache
        set_in_cache("describe", text, result)

        return result

    except FileNotFoundError:
        return {
            "input": text,
            "description": "Prompt template not found.",
            "word_count": 0,
            "generated_at": datetime.utcnow().isoformat(),
            "status": "failed",
            "is_fallback": True,
            "cached": False
        }

    except Exception as e:
        print(f"Error generating description: {e}")
        return {
            "input": text,
            "description": "Unable to generate description at this time.",
            "word_count": 0,
            "generated_at": datetime.utcnow().isoformat(),
            "status": "failed",
            "is_fallback": True,
            "cached": False
        }