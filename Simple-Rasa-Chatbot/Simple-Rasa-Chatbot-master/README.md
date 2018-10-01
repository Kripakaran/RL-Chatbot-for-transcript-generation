# Simple-Rasa-Chatbot
Simple Chatbot

Navigate to AI-Train Folder
then run this command:

python -m rasa_nlu.train \
    --config sample_configs/config_spacy.yml \
    --data data/examples/rasa/demo-rasa.json \
    --path projects

Now you will have a model in projects folder that would have been created.

Next run this command : 

python -m rasa_nlu.server --path projects

Your NLU will be listening on port 5000

To test open : http://localhost:5000  

Now navigate to the UI folder 

Using Python 2.7 run : 

python app1.py

YOU CAN OPEN http://127.0.0.1:8000/ to see the UI and chat with it.

You can make changes to the model and re run the whole process to develop your own chatbot.

