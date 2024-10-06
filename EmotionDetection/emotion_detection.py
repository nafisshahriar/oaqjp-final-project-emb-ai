import requests  
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = myobj, headers=header) 
    formatted_response = json.loads(response.text)

    formatted_response = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = formatted_response['anger']
    disgust_score = formatted_response['disgust']
    fear_score = formatted_response['fear']
    joy_score = formatted_response['joy']
    sadness_score = formatted_response['sadness']
    output = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    dominant_emotion = max(zip(output.values(), output.keys()))[1]
    output['dominant_emotion'] = dominant_emotion

    return output