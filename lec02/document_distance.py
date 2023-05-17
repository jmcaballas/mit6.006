import math
import re


def splitDocumentIntoWords(document):
    return re.findall(r"\b\w+\b", document.lower())


def countWordFrequencies(words):
    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


def dotProduct(vector1, vector2):
    product = 0.0
    combined = set(list(vector1.keys()) + list(vector2.keys()))
    for i in combined:
        product += vector1.get(i, 0) * vector2.get(i, 0)
    return product


def findDocumentDistance(document1, document2):
    document1_text = open(document1, "r").read()
    document2_text = open(document2, "r").read()
    words1 = splitDocumentIntoWords(document1_text)
    word_freq1 = countWordFrequencies(words1)
    words2 = splitDocumentIntoWords(document2_text)
    word_freq2 = countWordFrequencies(words2)

    product = dotProduct(word_freq1, word_freq2)
    normalized = product / (len(words1) * len(words2))
    return math.acos(normalized)


print(findDocumentDistance("document1.txt", "document2.txt"))
print(findDocumentDistance("document3.txt", "document4.txt"))
