from flask import Flask, render_template, request, jsonify
from translator.translator import translate_french_to_english, translate_english_to_french

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate/french-to-english', methods=['POST'])
def translate_french_to_english_route():
    french_text = request.form['french_text']
    english_translation = translate_french_to_english(french_text)
    return jsonify({'translation': english_translation})

@app.route('/translate/english-to-french', methods=['POST'])
def translate_english_to_french_route():
    english_text = request.form['english_text']
    french_translation = translate_english_to_french(english_text)
    return jsonify({'translation': french_translation})

if __name__ == '__main__':
    app.run(debug=True)
