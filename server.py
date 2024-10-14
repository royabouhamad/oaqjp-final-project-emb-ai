from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emot_detector():
    text_to_analyze = request.args.get('text_to_analyze')
    result = emotion_detector(text_to_analyze)
    stringResult = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    return stringResult

@app.route('/')
def render_index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)