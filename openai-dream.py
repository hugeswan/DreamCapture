# # from openai import OpenAI
# import openai

# import os
# import subprocess
# import json

# from flask import Flask, request, render_template_string, render_template
# from dotenv import load_dotenv

# # .env 파일에서 환경 변수 불러오기
# load_dotenv()
# openai.api_key = os.getenv('OPENAI_API_KEY')
# app = Flask(__name__)
# # client = OpenAI()
# client = openai

# def get_dream_story_and_interpretation(dream_text):
#     # 꿈을 스토리로 작성
#     response_story = client.chat.completions.create(
#         # model="gpt-3.5-turbo",
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"다음 꿈의 스토리가 짧고 부족한데, 좀 더 풍부하면서도 오리지널에서 벗어나지 않게 한 문단으로 반말로 작성해줘: {dream_text}"}
#         ]
#     )
#     story = response_story.choices[0].message.content

#     # 꿈의 의미 풀이
#     response_interpretation = client.chat.completions.create(
#         # model="gpt-3.5-turbo",
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"다음 꿈에 무슨 의미가 담겨있는지, 내가 무슨 감정을 느끼고 어떤 상태인지 한 문단으로 존댓말로 해석해줘: {dream_text}"}
#         ]
#     )
#     interpretation = response_interpretation.choices[0].message.content

#     return story, interpretation

# def generate_dream_image(dream_text):
#     api_key = os.getenv('OPENAI_API_KEY')
    
#     # JSON data for the API request
#     data = json.dumps({
#         "model": "dall-e-3",
#         "prompt": dream_text,
#         "n": 1,
#         "size": "1024x1024",
#         "response_format": "url"
#     })

#     # Constructing the cURL command for the API request
#     curl_command = [
#         "curl", "-X", "POST", "https://api.openai.com/v1/images/generations",
#         "-H", "Content-Type: application/json",
#         "-H", f"Authorization: Bearer {api_key}",
#         "-d", data
#     ]

#     try:
#         response = subprocess.run(curl_command, capture_output=True, text=True, check=True)
#         response_json = json.loads(response.stdout)
#         image_url = response_json['data'][0]['url']
#     except subprocess.CalledProcessError as e:
#         print("Error occurred:")
#         print(e.stderr)
#         image_url = None

#     return image_url

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     story = ""
#     interpretation = ""
#     image_url = ""
#     if request.method == 'POST':
#         dream_text = request.form['dream']
#         story, interpretation = get_dream_story_and_interpretation(dream_text)
#         image_url = generate_dream_image(dream_text)
#         return render_template('result.html', story=story, interpretation=interpretation, image_url=image_url)

#     return render_template_string('''
#         <!doctype html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Dream Analysis</title>
#         </head>
#         <body>
#             <h1>Enter your dream</h1>
#             <form method=post>
#                 <textarea name=dream rows=10 cols=30></textarea><br><br>
#                 <input type=submit value=Analyze>
#             </form>
#         </body>
#         </html>
#     ''')

# if __name__ == "__main__":
#     app.run(debug=True)

import openai
import os
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
import subprocess
import json

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
client = openai

def get_dream_story_and_interpretation(dream_text):
    response_story = client.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈의 스토리가 짧고 부족한데, 좀 더 풍부하면서도 오리지널에서 벗어나지 않게 한 문단으로 반말로 작성해줘: {dream_text}"}
        ]
    )
    story = response_story.choices[0].message['content']

    response_interpretation = client.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈에 무슨 의미가 담겨있는지, 내가 무슨 감정을 느끼고 어떤 상태인지 한 문단으로 존댓말로 해석해줘: {dream_text}"}
        ]
    )
    interpretation = response_interpretation.choices[0].message['content']

    return story, interpretation

def generate_dream_image(dream_text):
    api_key = os.getenv('OPENAI_API_KEY')
    
    data = json.dumps({
        "model": "dall-e-3",
        "prompt": dream_text,
        "n": 1,
        "size": "1024x1024",
        "response_format": "url"
    })

    curl_command = [
        "curl", "-X", "POST", "https://api.openai.com/v1/images/generations",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {api_key}",
        "-d", data
    ]

    try:
        response = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        response_json = json.loads(response.stdout)
        image_url = response_json['data'][0]['url']
    except subprocess.CalledProcessError as e:
        print("Error occurred:")
        print(e.stderr)
        image_url = None

    return image_url

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    dream_text = request.form['dream']
    story, interpretation = get_dream_story_and_interpretation(dream_text)
    image_url = generate_dream_image(dream_text)
    # 결과를 정적 HTML 파일로 저장
    with open('result.html', 'w', encoding='utf-8') as f:
        f.write(render_template('result_template.html', story=story, interpretation=interpretation, image_url=image_url))
    return render_template('result_template.html', story=story, interpretation=interpretation, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
