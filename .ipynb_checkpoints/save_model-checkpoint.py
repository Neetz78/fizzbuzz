#%% import required libraries
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

model_path = '/Users/neethug/Desktop/Neethu/flask_gunicorn_nginx_docker/models/transformers/' # will be created automatically if not exists


classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
classifier.save_pretrained(model_path)
#%% test if it works
classifier(["good"]) 

#%% load model from local directory if it works
model = TFAutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
print("-----------  model loaded from local dir ------------")
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
print("-----------  tokenizer loaded from local dir ------------")
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

classifier(["I'm reading a lot of reviews saying that this is the best 'game soundtrack' and I figured that I'd write a review to disagree a bit. This in my opinino is Yasunori Mitsuda's ultimate masterpiece. The music is timeless and I'm been listening to it for years now and its beauty simply refuses to fade.The price tag on this is pretty staggering I must say, but if you are going to buy any cd for this much money, this is the only one that I feel would be worth every penny."]) 

# %%