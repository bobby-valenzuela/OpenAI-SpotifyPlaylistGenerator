import openai
from dotenv import load_dotenv
import os
# from ast import parse
import argparse

def code_review(file_path, model):
    with open(file_path, "r") as file:
        content = file.read()
    generated_code_review = make_code_review_request(content, model)
    print(generated_code_review)


def make_code_review_request(filecontent, model):

    PROMPT = """
    You will receive a file's contents as text.
    Generate a code review for the file.  Indicate what changes should be made to improve its style, performance, readability, scalability, and maintainability.  If there are any reputable libraries that could be introduced to improve the code, suggest them.  Be kind and constructive.  For each suggested change, include line numbers to which you are referring.
    """
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": f"Code review the following file: {filecontent}"}
    ]
    res = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    return res["choices"][0]["message"]["content"]



def main():
    parser = argparse.ArgumentParser(description="Simple code reviewer for a file")
    parser.add_argument("file")
    parser.add_argument("--model", default="gpt-3.5-turbo")
    args = parser.parse_args()
    code_review(args.file, args.model)

if __name__ == "__main__":

    # METHOD #1: Loading .env values

    # from dotenv import dotenv_values
    # config = dotenv_values('.env');
    # openai.api_key = config["OPENAI_API_KEY"]


    # METHOD #2 [Preferred]: loading .env values and storing as environment variables
    from dotenv import load_dotenv

    load_dotenv() # Looks for ./.env file by default and saves values an environment variable which you can access with os.getenv("MY_VAR") 
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()

