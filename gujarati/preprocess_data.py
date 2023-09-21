import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

def preprocess_gujarati_text(text, custom_stop_words=None):
  """Preprocesses Gujarati text for NLP tasks.

  Args:
    text: A string containing the Gujarati text to be preprocessed.
    custom_stop_words: A list of strings containing custom stop words to be removed from the text.

  Returns:
    A string containing the preprocessed Gujarati text.
  """

  # Remove punctuation.
  text = re.sub(r'[^\w\s]', '', text)

  # Convert all characters to lowercase.
  text = text.lower()

  # Remove stop words.
  stop_words = set(["એ", "છે", "જે", "કે", "પણ", "પર", "થી", "માં", "મેં", "તે", "હું", "આ", "જો", "પણ", "પર", "થી", "માં", "મેં", "તે", "હું"])
  if custom_stop_words is not None:
    stop_words.update(custom_stop_words)

  text = ' '.join([word for word in text.split() if word not in stop_words])

  return text

# Example usage:

text = "આ એક ઉદાહરણ છે કેવી રીતે ગુજરાતી ટેક્સ્ટને NLP કાર્યો માટે પ્રીપ્રોસેસ કરવો."

custom_stop_words = ["કેવી", "રીતે", "NLP"]

preprocessed_text = preprocess_gujarati_text(text, custom_stop_words)

print(preprocessed_text)


# Tokenization (sentence and word)
sentences = sent_tokenize(preprocessed_text)
words = [word_tokenize(sentence) for sentence in sentences]

# Text Normalization
normalizer_factory = IndicNormalizerFactory()
normalizer = normalizer_factory.get_normalizer("gu")
normalized_text = normalizer.normalize(preprocessed_text)

# Transliteration to Roman script (for readability)
transliterated_text = UnicodeIndicTransliterator.transliterate(normalized_text, "gu", "itrans")

# print
print("\nTokenized sentences:")
for sentence in sentences:
    print(sentence)
print("\nTokenized words:")
for sentence_words in words:
    print(sentence_words)

print("\nTransliterated text")
print(transliterated_text)
