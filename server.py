'''Server file'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emot_detector():
    '''Handle emotion detection requests'''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    dominant_emotion = result['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    string_result = f"""For the given statement, the system response is 'anger':
    {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}
    and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."""
    return string_result

@app.route('/')
def render_index():
    '''Render the index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
