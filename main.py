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
    parser.add_argument("user_prompt", type=str, help="type your prompt here")
    args = parser.parse_args()

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt
            }
        ],
    )

    # input and output tokens
    if response.usage != None:
        print(f"Prompt tokens: {response.usage.prompt_tokens} \nResponse tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("Failed API request, model response is empty,")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
