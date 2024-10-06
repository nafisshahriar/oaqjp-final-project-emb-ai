' ' 'Flask app that uses API to detec emotion in text' ' '
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detect():
    ' ' 'Detects emotion' ' '
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dom_emo = response['dominant_emotion']

    text=""
    if anger is None:
        text += "Invalid text! Please try again!"
    else:
        text = f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        text += f"'sadness': {sadness}. The dominant emotion is {dom_emo}"
    return text

@app.route("/")
def render_index_page():
    ' ' 'Renders HTML ans JS' ' '
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
