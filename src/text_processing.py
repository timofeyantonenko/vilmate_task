import math
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ENGLISH_STOPWORDS = set(stopwords.words('english'))


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


class ImportantWordsExtractor:
    def __init__(self, text):
        self.tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        self.document = text
        # self.document = tb(text)

    def remove_stopwords(self):
        word_tokens = word_tokenize(self.document)

        filtered_sentence = []

        for w in word_tokens:
            if w.lower() not in ENGLISH_STOPWORDS:
                filtered_sentence.append(w)

        return " ".join(filtered_sentence)

    def get_top(self, n=20):
        tfidf_matrix = self.tf.fit_transform([self.document])
        feature_names = self.tf.get_feature_names()
        dense = tfidf_matrix.todense()
        episode = dense[0].tolist()[0]
        phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]
        top = sorted(phrase_scores, key=lambda t: t[1] * -1)[:n]
        return [feature_names[top[i][0]] for i in range(len(top))]


    # def get_top(self, n=20):
    #     cleaned_text = self.remove_stopwords()
    #     self.document = tb(cleaned_text)
    #     bloblist = [self.document]
    #     scores = {word: tfidf(word, self.document, bloblist=bloblist) for word in self.document.words}
    #     sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    #     # return sorted_words
    #     for word, score in sorted_words[:n]:
    #         print("\tWord: {}, TF-IDF: {}".format(word, round(score, n)))