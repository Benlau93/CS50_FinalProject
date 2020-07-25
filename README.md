# CS50_FinalProject
This project test the toxicity of text users enter into the text box. Using flask, html, CSS and python, I designed a webpage that get an input from the user and send it into a model to output the probability of 6 different types of toxicity;<br> 
1. Toxic, 2. Severe Toxic, 3. Obscene, 4. Threat, 5. Insult and 6. Identity Hate

## Model
Dataset is from Kaggle Toxic Comment Classification Challenge (https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/overview) <br>
Text was processed by removing html tags, numbers, punctuations, single character and multiple whitespaces before sending into the classifier model.
The model uses GloVe embedding (http://nlp.stanford.edu/data/glove.6B.zip) for better words representation and concatenate with a simple LSTM/Dense/BN/Dropout block. The final output layer
is a 6 node Dense layer with a sigmoid activation function to output the probability of each category of toxicity.

## Webpage
Using Flask as the web development framework, I<br>
1. Retrieve the data from the user
2. Process the text using self-defined python module
3. Pass the processed text into the model
4. Pass the output from the model into a result page that display all probability of toxicity.
