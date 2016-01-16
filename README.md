# py-corenlp
Python wrapper for Stanford CoreNLP.  This simply wraps the API from the server included with CoreNLP 3.6.0.  See the CoreNLP server [API documentation](http://stanfordnlp.github.io/CoreNLP/corenlp-server.html#api-documentation) for details.

# Install
```
pip install pycorenlp
```

# Usage
First make sure you have the Stanford CoreNLP server running.  See [the instructions here](http://stanfordnlp.github.io/CoreNLP/corenlp-server.html#getting-started) for how to do that.

Then the setup just requires you to pass in the url of the server:
```
>>> from pycorenlp import StanfordCoreNLP
>>> nlp = StanfordCoreNLP('http://localhost:9000')
```

Supports annotation:
```
>>> text = (
  'Pusheen and Smitha walked along the beach. '
  'Pusheen wanted to surf, but fell off the surfboard.')
>>> output = nlp.annotate(text, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })
>>> print(output['sentences'][0]['parse'])
(ROOT
  (S
    (NP (NNP Pusheen)
      (CC and)
      (NNP Smitha))
    (VP (VBD walked)
      (PP (IN along)
        (NP (DT the) (NN beach))))
    (. .)))
```

And tokensregex + semgrex
```
>>> nlp.tokensregex(text, pattern='/Pusheen|Smitha/', filter=False)
{u'sentences': [
  {
    u'1': {u'text': u'Smitha', u'begin': 2, u'end': 3},
    u'0': {u'text': u'Pusheen', u'begin': 0, u'end': 1}, u'length': 2
  },
  {u'0': {u'text': u'Pusheen', u'begin': 0, u'end': 1}, u'length': 1}]}
>>> nlp.semgrex(text, pattern='{tag: VBD}', filter=False)
{u'sentences': [
  {u'0': {u'text': u'walked', u'begin': 3, u'end': 4}, u'length': 1},
  {
    u'1': {u'text': u'fell', u'begin': 6, u'end': 7},
    u'0': {u'text': u'wanted', u'begin': 1, u'end': 2}, u'length': 2
  }
]}
```

The code above is available in [example.py](example.py).
