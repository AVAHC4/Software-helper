import os
import sys

import httpx
from google import genai
from google.genai import errors

MODEL = "gemini-3.8-flash"


def main() -> int:
    try:
        question = input("What is your question? ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nNo question provided.")
        return 1

    if not question:
        print("Please ask a valid question.")
        return 1
    if not os.environ.get("GEMINI_API_KEY"):
        print("Set the GEMINI_API_KEY environment variable first.", file=sys.stderr)
        return 1

    try:
        with genai.Client() as client:
            response = client.interactions.create(model=MODEL, input=question)
    except errors.APIError as error:
        print(f"Gemini request failed (HTTP {error.code}). Check your key, model access, and quota.", file=sys.stderr)
        return 1
    except httpx.RequestError:
        print("Could not connect to Gemini. Check your network connection.", file=sys.stderr)
        return 1

    if not response.output_text:
        print("Gemini returned no text response.", file=sys.stderr)
        return 1
    print(response.output_text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
