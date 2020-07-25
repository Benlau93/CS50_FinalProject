import json
import re

import tensorflow as tf
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing import sequence


BASE_DIR = "./model/"

def preprocess_text(sen):
    # Removing html tags
    sentence = remove_tags(sen)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence
  

def remove_tags(text):
	TAG_RE = re.compile(r'<[^>]+>')
	return TAG_RE.sub('', text)

def tokenize(text):
	# load tokenizer
	max_len = 128

	with open(BASE_DIR+"tokenizer.json") as json_file:
		tok_json = json.load(json_file)

	tok = tokenizer_from_json(tok_json)

	# tokenize 
	sequences = tok.texts_to_sequences([text])
	return sequence.pad_sequences(sequences,maxlen=max_len)

def predict(test):
	# load model
	model = tf.keras.models.load_model(BASE_DIR)

	# predict
	y_pred = model.predict(test)

	# format as dictionary
	label = ["toxic","severe_toxic","obscene","threat","insult","identity_hate"]
	return {label[i]:int(round(y_pred[0][i]*100,0)) for i in range(6)}