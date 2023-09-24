import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import jaccard_score

# Sample datasets for two different time periods
data1 = ["આ એક ગુજરાતી વાક્ય છે.", "ગુજરાતી ભાષા સુંદર છે.", "આ એક મિત્ર છે."]
data2 = ["આ એક ગુજરાતી વાક્ય છે.", "ગુજરાતી ભાષા સુંદર છે.", "આ એક સંબંધિત વિષય છે."]

# Convert the data to pandas DataFrames
df1 = pd.DataFrame(data1, columns=['text'])
df2 = pd.DataFrame(data2, columns=['text'])

# CountVectorizer for text representation
vectorizer = CountVectorizer()
X1 = vectorizer.fit_transform(df1['text'])
X2 = vectorizer.transform(df2['text'])

# Calculate Jaccard similarity score between the two datasets
jaccard_similarity = jaccard_score(X1.toarray().flatten(), X2.toarray().flatten())

# Set a threshold for detecting data drift
threshold = 0.2  # Adjust as needed

# Check if data drift is detected
if jaccard_similarity < threshold:
    print("Data drift detected! The data distribution has changed.")
else:
    print("No significant data drift detected.")


