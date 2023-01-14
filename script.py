import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if w not in stop_words]
word_matches = [{"value": value, "index": index} for index, value in enumerate(word_tokens, start=0) if value in filtered_sentence]

ussyfy = "([aeiou]$|[aeiou]{2}[^aeiou]$|[aeiou][^aeiou]$|[c][aeiou]$|[s]$)"
def ussyfire(word):
    if re.match("[^aeiou][aeiou]", word["value"]):
        word["value"] = re.sub(ussyfy, "ussy", word["value"])
        return word

ussy_words = [ ussyfire(word) for word in word_matches if ussyfire(word)]

for ussy in ussy_words:
    word_tokens[ussy["index"]] = ussy["value"]

print(' '.join(word_tokens))
