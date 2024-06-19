from openai import OpenAI
client = OpenAI()

import os
import subprocess
import json

def get_dream_story_and_interpretation(dream_text):
    # 꿈을 스토리로 작성
    response_story = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈의 스토리가 짧고 부족한데, 좀 더 풍부하면서도 오리지널에서 벗어나지 않게 한 문단으로 반말로 작성해줘: {dream_text}"}
        ]
    )
    story = response_story.choices[0].message.content

    # 꿈의 의미 풀이
    response_interpretation = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈의 의미를 뻔하지 않고 재미있게 한 문단으로 존댓말로 해석해줘: {dream_text}"}
        ]
    )
    interpretation = response_interpretation.choices[0].message.content

    return story, interpretation

if __name__ == "__main__":
    dream_text = input("꿈 내용을 입력하세요: ")

    story, interpretation = get_dream_story_and_interpretation(dream_text)

    print("\n--- 꿈 이야기 ---")
    print(story)
    print("\n--- 꿈 풀이 ---")
    print(interpretation)

def get_user_input(prompt):
    """ Function to get user input """
    return input(prompt)

def main():
    # Fetch the API key from the system environment
    api_key = os.environ.get('OPENAI_API_KEY')

    if not api_key:
        print("API key not found in environment. Please set OPENAI_API_KEY.")
        return

    while True:
        print(f"Authorization Header: Bearer {api_key}")
        print(f"Prompt: {dream_text}")

        # JSON data for the API request
        data = json.dumps({
            "model": "dall-e-3",          # Specifies the model to be used
            "prompt": dream_text,        # The user-provided prompt
            "n": 1,                       # Number of images to generate
            "size": "1024x1024",          # Size of the generated images
            "quality": "hd",              # Optional: double cost for finer details & greater consistency
            "response_format": "url"      # Optional: url is default but b64_json is another option
        })

        # Constructing the cURL command for the API request
        curl_command = [
            "curl", "-X", "POST", "https://api.openai.com/v1/images/generations",
            "-H", "Content-Type: application/json",
            "-H", f"Authorization: Bearer {api_key}",
            "-d", data
        ]

        # Print the command for validation/debugging
        print("cURL Command:", " ".join(curl_command))
        
        # Executing the cURL command and capturing the response
        try:
            response = subprocess.run(curl_command, capture_output=True, text=True, check=True)
            print("Response:\n", response.stdout)
        except subprocess.CalledProcessError as e:
            # Handling errors during the API request
            print("Error occurred:")
            print(e.stderr)
        break

if __name__ == "__main__":
    main()