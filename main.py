def main():
    import os
    import argparse
    from openai import OpenAI
    from dotenv import load_dotenv

    print("Hello from code-agent!")

    # load environment variables
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    # check for environment variable errors
    if api_key == None:
        raise RuntimeError('Invalid Api Key')

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    # arguments parsing for user prompts
    parser = argparse.ArgumentParser(description="coding_agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages=[
            {
                "role": "user",
                "content": args.user_prompt
            }
        ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )

    # input and output tokens
    if response.usage != None:
        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("Failed API request, model response is empty,")
    print(f"Response: \n{response.choices[0].message.content}")

if __name__ == "__main__":
    main()
