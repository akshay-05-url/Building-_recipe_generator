from transformers import pipeline

# Load a local NLP pipeline
nlp = pipeline("sentiment-analysis")  # Can also do summarization, question-answering, etc.

# Test the model
result = nlp("I love using Hugging Face models locally!")
print(result)

