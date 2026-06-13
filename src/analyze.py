import pandas as pd
from src.sentiment import label  # Import your function

# 1. Load the data
df = pd.read_csv('data/movie_review.csv')

results = df['text'].apply(lambda x: label(x))

df[['sentiment', 'score']] = pd.DataFrame(results.tolist(), index=df.index)
df.to_csv('data/results.csv', index=False)

print("Batch processing complete! Saved to data/results.csv")