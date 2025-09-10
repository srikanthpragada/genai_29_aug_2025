from transformers import pipeline

# Load the pipeline with the Whisper model
pipe = pipeline("automatic-speech-recognition",
                 model="openai/whisper-base", return_timestamps=True)

# Path to your audio file (.wav or .mp3)
audio_path = "mlk_clip.mp3"   

# Transcribe the audio
result = pipe(audio_path)

# Print the transcription
#print("Transcription:", result["text"] )

context = result["text"]

ner = pipeline("ner", model="dslim/bert-base-NER") 

entities = ner(context)  

# Display results
for entity in entities:
    print(f"{entity['word']} - ({entity['score']:.2f})")

