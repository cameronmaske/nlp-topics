# set up logging so we see what's going on
import os
from gensim import corpora, utils


def iter_documents(reuters_dir):
    """Iterate over Reuters documents, yielding one document at a time."""
    for fname in os.listdir(reuters_dir):
        document = open(os.path.join(reuters_dir, fname)).read()
        yield utils.simple_preprocess(document)


class Corpus(object):
    def __init__(self, reuters_dir):
        self.dir = reuters_dir
        self.dictionary = corpora.Dictionary(iter_documents(reuters_dir))
        self.dictionary.filter_extremes()

    def __iter__(self):
        for tokens in iter_documents(self.dir):
            yield self.dictionary.doc2bow(tokens)


corpus = Corpus('/usr/share/nltk_data/corpora/brown')
