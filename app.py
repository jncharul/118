from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)

@app.route('/')
def home():
    entries = show_entry()
    return render_template('index.html',entries = entries)
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
    input_text = request.json.get("text")  
    
    if not input_text:
        # Response to send if the input_text is undefined
        response = {
                    "status": "error",
                    "message": "Please enter some text to predict emotion!"
                  }
        return jsonify(response)
    else:  
        predicted_emotion,predicted_emotion_img_url = predict(input_text)
        
        # Response to send if the input_text is not undefined
        response = {
                    "status": "success",
                    "data": {
                            "predicted_emotion": predicted_emotion,
                            "predicted_emotion_img_url": predicted_emotion_img_url
                            }  
                   }

        # Send Response         
        return jsonify(response)

@app.route("/save-entry", methods=["POST"])
def save_entry():
    date = request.json.get("date")
    save_text = request.json.get("text")
    emotion = request.json.get("emotion")

    entry = date + "," + save_text + "," + emotion
    file_handler = open('/Users/charuljain/Desktop/116/static/assets/data_files/data_entry.csv','a')
    file_handler.write(entry + '\n')

    return jsonify("Success")

   
app.run(debug=True)



    