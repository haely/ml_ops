"""
For NLP, fetch top n most common words and see how that compares to the train text
"""

import re
from collections import Counter

def fetch_top_100_most_occurring_words(text):
  """Fetches the top 100 most occurring words from a text.

  Args:
    text: A string containing the text to be analyzed.

  Returns:
    A list of the top 100 most occurring words in the text, in order of
    decreasing frequency.
  """

  # Remove punctuation.
  text = re.sub(r'[^\w\s]', '', text)

  # Convert all characters to lowercase.
  text = text.lower()

  # Split the text into words.
  words = text.split()

  # Count the number of occurrences of each word.
  word_counts = Counter(words)

  # Get the top 100 most occurring words.
  top_100_words = word_counts.most_common(100)

  return top_100_words

# Example usage:

text = "This is a sample text with some words that are repeated more often than others."

top_100_words = fetch_top_100_most_occurring_words(text)

print(top_100_words)
