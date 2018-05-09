import nltk
from nltk.tag.stanford import StanfordPOSTagger
from flask import Flask, jsonify, request, render_template
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

stopwords = set(stopwords.words('arabic') + list(punctuation))

def compute_frequencies(word_sent):

    freq = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in stopwords:
          freq[word] += 1

    return freq

def summarize(text, n):
    sents = sent_tokenize(text)

    if n >= len(sents):
        print('number of sentences must be greater than of the target')


    word_sent = [word_tokenize(s.lower()) for s in sents]

    freq = compute_frequencies(word_sent)

    ranking = defaultdict(int)

    for i, sent in enumerate(word_sent):
        for w in sent:
            if w in freq:
                ranking[i] += freq[w]


    sents_idx = rank(ranking, n)
    return [sents[j] for j in sents_idx]



def rank(ranking, n):

    rank = {}
    sorted_dict = sorted(zip(ranking.values(), ranking.keys()))
    for i in range(n):
        rank.update({sorted_dict[(len(sorted_dict) - 1) - i][1]: sorted_dict[(len(sorted_dict) - 1) - i][0]})

    return rank


app = Flask(__name__)

@app.route('/')
def static_page():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def response():
    # text = open('text.txt').read()
    text = request.form['text']
    result = summarize(text, 2)

    new = ''
    for n in result:
        new += n

    open('summary.txt', 'a+').write(new)

    return jsonify({'summary': new})

if __name__ == '__main__':
    app.run()
