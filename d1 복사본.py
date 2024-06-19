from flask import Flask, send_from_directory, render_template_string
import openai
import qrcode
from datetime import datetime

app = Flask(__name__, static_folder='static')

# OpenAI API Key 설정
openai.api_key = 'sk-proj-QVjNOm0wiMvKvJiCHexST3BlbkFJXnKsLO7gg37TKBPLI7Mg'

# GPT-3를 이용한 텍스트 다듬기 함수
def refine_text_with_gpt(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please refine the following text to make it smooth and coherent:\n\n{text}",
        max_tokens=500
    )
    refined_text = response.choices[0].text.strip()
    return refined_text

# GPT-3를 이용한 꿈 해석 함수
def interpret_dream_with_gpt(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Interpret the following dream:\n\n{text}",
        max_tokens=500
    )
    interpretation = response.choices[0].text.strip()
    return interpretation

# DALL-E를 이용한 이미지 생성 함수
def generate_dream_image(text):
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

# QR 코드 생성 함수
def generate_qr_code(url, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)

@app.route('/webpage1')
def webpage1():
    dream_content = "I had a dream about flying over a city."
    refined_text = refine_text_with_gpt(dream_content)
    interpretation = interpret_dream_with_gpt(refined_text)
    image_url = generate_dream_image(refined_text)
    
    html_content = f'''
    <html>
    <head>
        <title>Dream Interpretation</title>
    </head>
    <body>
        <h1>Dream Content</h1>
        <p>{refined_text}</p>
        <h1>Dream Interpretation</h1>
        <p>{interpretation}</p>
        <h1>Dream Image</h1>
        <img src="{image_url}" alt="Dream Image">
    </body>
    </html>
    '''
    return html_content

@app.route('/webpage2')
def webpage2():
    webpage1_url = "http://192.168.0.103:5000/webpage1"
    generate_qr_code(webpage1_url, 'static/qr_code.png')
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    dream_title = "Flying Over a City"
    
    html_content = f'''
    <html>
    <head>
        <title>Dream Summary</title>
    </head>
    <body>
        <h1>Dream Summary</h1>
        <p>Date: {current_date}</p>
        <p>Title: {dream_title}</p>
        <h1>QR Code</h1>
        <img src="/static/qr_code.png" alt="QR Code">
        <p><a href="{webpage1_url}">Link to Dream Interpretation</a></p>
    </body>
    </html>
    '''
    return html_content

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
