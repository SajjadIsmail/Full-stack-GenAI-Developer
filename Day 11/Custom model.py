# Use a pipeline as a high-level helper
from transformers import pipeline
#pip install sentencepiece

generator = pipeline("translation", model="Hemanth-thunder/english-tamil-mt")
result = generator("My name is Sajjad Ismail", src_lang="en", tgt_lang="ta")
print(result)