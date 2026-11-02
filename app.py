import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompt_library import WRITING_TEMPLATES

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash"

def generate(task: str, user_input: str, temperature: float, output_format: str):
    template = WRITING_TEMPLATES[task]

    format_rules = {
        "markdown": "Use clean Markdown with headings, bullets, and bold key points.",
        "plain": "Use plain text only. Do not use Markdown symbols.",
        "json": "Return only valid JSON matching this schema: "
                '{"title": string, "content": string, "tags": [string]}',
        "table": "Return a Markdown table with columns: Section | Content.",
    }[output_format]

    system_prompt = f"""{template["system"]}

Formatting rules:
{format_rules}

Quality rules:
- Be clear, specific, and useful.
- Avoid filler and unsupported claims.
- Match the requested audience, tone, and length.
"""

    prompt = template["user"].format(input=user_input)

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=temperature,
            max_output_tokens=2500,
        ),
    )
    return response.text

def main():
    print("AI Writing Assistant")
    tasks = list(WRITING_TEMPLATES)

    while True:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.replace('_', ' ').title()}")

        choice = input("Choose task (1-4, q to quit): ").strip()
        if choice.lower() == "q":
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(tasks):
            print("Invalid choice.")
            continue

        task = tasks[int(choice) - 1]
        user_input = input("Enter your topic, draft, email details, or code:\n> ")

        try:
            temperature = float(input("Temperature 0.0-2.0 [default 0.7]: ") or 0.7)
        except ValueError:
            temperature = 0.7
        temperature = max(0.0, min(2.0, temperature))

        output_format = input("Format: markdown/plain/json/table [markdown]: ").strip() or "markdown"
        if output_format not in {"markdown", "plain", "json", "table"}:
            output_format = "markdown"

        print("\n--- OUTPUT ---\n")
        print(generate(task, user_input, temperature, output_format))

if __name__ == "__main__":
    main()
