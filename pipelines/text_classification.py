from transformers import pipeline

classifier = pipeline("zero-shot-classification", 
                       model = "facebook/bart-large-mnli" )
output = classifier(
    "Trump is working on cease fire bewteen Iran and Israel",
    candidate_labels = ["education", "politics", "business"],
)
print(output)