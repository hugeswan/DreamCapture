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
#----------------------------





# from openai import OpenAI
# import os
# from flask import Flask, request, render_template, render_template_string
# from dotenv import load_dotenv
# import subprocess
# import json
# from datetime import datetime

# # .env 파일에서 환경 변수 불러오기
# load_dotenv()

# # OpenAI API 키 설정
# OpenAI.api_key = os.getenv('OPENAI_API_KEY')

# app = Flask(__name__)
# client = OpenAI()

# def get_dream_story_and_interpretation(dream_text):
#     response_story = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"다음 꿈의 스토리가 짧고 부족한데, 좀 더 풍부하면서도 오리지널에서 벗어나지 않게 한 문단으로 반말로 작성해줘: {dream_text}"}
#         ]
#     )
#     story = response_story.choices[0].message.content

#     response_interpretation = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"다음 꿈에 무슨 의미가 담겨있는지, 내가 무슨 감정을 느끼고 어떤 상태인지 논리적이고 공식적인 말투로 한 문단으로 해석해줘: {dream_text}"}
#         ]
#     )
#     interpretation = response_interpretation.choices[0].message.content

#     return story, interpretation

# def generate_dream_image(dream_text):
#     api_key = os.getenv('OPENAI_API_KEY')
    
#     data = json.dumps({
#         "model": "dall-e-3",
#         "prompt": dream_text+" 그리고 이미지에 텍스트가 없었으면 좋겠어.",
#         "n": 1,
#         "size": "1024x1024",
#         "response_format": "url"
#     })

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
#     if request.method == 'POST':
#         dream_text = request.form['dream']
#         story, interpretation = get_dream_story_and_interpretation(dream_text)
#         image_url = generate_dream_image(dream_text)
#         # 현재 날짜와 시간 가져오기
#         current_time = datetime.now().strftime("%Y/%m/%d %H:%M")
#         # 결과를 정적 HTML 파일로 저장
#         with open('templates/result.html', 'w', encoding='utf-8') as f:
#             f.write(render_template('result_template.html', story=story, interpretation=interpretation, image_url=image_url))
#         return render_template('result_template.html', story=story, interpretation=interpretation, image_url=image_url, current_time=current_time)

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
#     # time = datetime.now().strftime("%Y/%m/%d %H:%M")
#     app.run(debug=True, host='0.0.0.0', port=5001)





from openai import OpenAI
import os
from flask import Flask, request, render_template, render_template_string, redirect, url_for
from dotenv import load_dotenv
import subprocess
import json
from datetime import datetime

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# OpenAI API 키 설정
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
client = OpenAI()

def get_dream_story_and_interpretation(dream_text):
    response_story = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈의 스토리가 짧고 부족한데, 좀 더 풍부하면서도 오리지널에서 벗어나지 않게 한 문단으로 반말로 작성해줘: {dream_text}"}
        ]
    )
    story = response_story.choices[0].message.content

    response_interpretation = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 꿈에 무슨 의미가 담겨있는지, 내가 무슨 감정을 느끼고 어떤 상태인지 논리적이고 공식적인 말투로 한 문단으로 해석해줘: {dream_text}"}
        ]
    )
    interpretation = response_interpretation.choices[0].message.content

    return story, interpretation

def generate_dream_image(dream_text):
    api_key = os.getenv('OPENAI_API_KEY')
    
    data = json.dumps({
        "model": "dall-e-3",
        "prompt": dream_text+" No text in the generated image.",
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

def transcribe_audio(audio_file_path):
    # Whisper API를 사용하여 음성 파일을 텍스트로 변환합니다.
    audio_file = open(audio_file_path, "rb")
    response = client.audio.transcriptions.create("whisper-1", file=audio_file)
    return response['text']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        dream_text = request.form['dream']
        story, interpretation = get_dream_story_and_interpretation(dream_text)
        image_url = generate_dream_image(dream_text)
        # 현재 날짜와 시간 가져오기
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template('result_template.html', story=story, interpretation=interpretation, image_url=image_url, current_time=current_time)

    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dream Analysis</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {
                    background-color: #f8f9fa;
                    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                }
                .container {
                    margin-top: 50px;
                    max-width: 600px;
                }
                .card {
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    border-radius: 10px;
                    background: white;
                }
                textarea {
                    resize: none;
                    height: 200px;
                    border-radius: 5px;
                }
                .btn-primary {
                    background-color: #007bff;
                    border-color: #007bff;
                }
                .btn-primary:hover {
                    background-color: #0056b3;
                    border-color: #0056b3;
                }
                h1 {
                    margin-bottom: 20px;
                    font-size: 24px;
                }
                label {
                    font-size: 18px;
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="card">
                    <h1 class="text-center">Enter your dream</h1>
                    <div class="text-center">
                        <button class="btn btn-secondary" onclick="showTextInput()">Text Input</button>
                        <button class="btn btn-secondary" onclick="showVoiceInput()">Voice Input</button>
                    </div>
                    <form id="textForm" action="/" method="post" enctype="multipart/form-data" style="display: none;">
                        <div class="form-group">
                            <label for="dream">Describe your dream</label>
                            <textarea name="dream" id="dream" class="form-control" placeholder="Describe your dream..."></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary btn-block">Analyze</button>
                    </form>
                    <form id="voiceForm" action="/voice_input" method="post" enctype="multipart/form-data" style="display: none;">
                        <div class="form-group">
                            <label for="voice">Record your dream</label>
                            <input type="file" name="voice" id="voice" class="form-control" accept="audio/*" capture>
                        </div>
                        <button type="submit" class="btn btn-primary btn-block">Analyze</button>
                    </form>
                </div>
            </div>
            <script>
                function showTextInput() {
                    document.getElementById('textForm').style.display = 'block';
                    document.getElementById('voiceForm').style.display = 'none';
                }
                function showVoiceInput() {
                    document.getElementById('textForm').style.display = 'none';
                    document.getElementById('voiceForm').style.display = 'block';
                }
            </script>
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>
    ''')


@app.route('/voice_input', methods=['POST'])
def voice_input():
    if 'voice' not in request.files:
        return redirect(url_for('home'))
    voice = request.files['voice']
    if voice.filename == '':
        return redirect(url_for('home'))
    if voice:
        file_path = 'uploaded_voice.wav'
        voice.save(file_path)
        # 음성 파일을 텍스트로 변환합니다.
        dream_text = transcribe_audio(file_path)
        story, interpretation = get_dream_story_and_interpretation(dream_text)
        image_url = generate_dream_image(dream_text)
        # 현재 날짜와 시간 가져오기
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template('result_template.html', story=story, interpretation=interpretation, image_url=image_url, current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)