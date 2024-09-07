from flask import Flask, request, jsonify, url_for, render_template
import openai
import os
import base64
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

openai.api_key = os.getenv('OPENAI_API_KEY')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
@app.route('/')
def index():
    return render_template('index.html')  
@app.route('/describe', methods=['POST'])
def describe():
    context = request.form.get('context', '')
    images = request.files.getlist('images')  

    if not images:
        return jsonify({"error": "No images uploaded."}), 400

    base64_images = []
    for image in images:
        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)

        base64_images.append(f"data:image/jpeg;base64,{encode_image(filepath)}")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": context if context else "What are in these images? Is there any difference between them?"},
                        *[
                            {"type": "image_url", "image_url": {"url": image}}
                            for image in base64_images
                        ]
                    ]
                }
            ],
            max_tokens=300
        )
        return jsonify({"response": response['choices'][0]['message']['content']})
    except Exception as e:
        print(f"Error from OpenAI API: {e}")
        return jsonify({"error": f"Failed to get a response from OpenAI: {e}"}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return app.send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
