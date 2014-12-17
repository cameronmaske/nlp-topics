from flask import Flask, request, jsonify
from gensim import models, utils
from operator import itemgetter
from training import corpus


app = Flask(__name__)
mallet_path = '/temp/mallet/bin/mallet'
model = models.LdaMallet(
    mallet_path,
    corpus=corpus,
    id2word=corpus.dictionary,
    num_topics=400)


def average(l):
    return sum(l) / len(l)


@app.route("/api/analyze/", methods=['POST'])
def analyze():
    """
    Resources
    http://stackoverflow.com/questions/20984841/topic-distribution-how-do-we-see-which-document-belong-to-which-topic-after-doi
    """
    text = request.json['text']
    bow = corpus.dictionary.doc2bow(utils.simple_preprocess(text))
    topics = model[bow]
    sorted_topics = sorted(topics, key=itemgetter(1), reverse=True)
    top_topics = []
    for topic_id, topic_score in sorted_topics[0:3]:
        top_topics.append({
            "topic": model.show_topic(topic_id)[0][1],
            "score": topic_score
        })

    return jsonify(data=top_topics)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


