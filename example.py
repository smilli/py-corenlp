from pycorenlp import StanfordCoreNLP

if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    text = (
        'Pusheen and Smitha walked along the beach. Pusheen wanted to surf,'
        'but fell off the surfboard.')
    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    print(output['sentences'][0]['parse'])
    output = nlp.tokensregex(text, pattern='/Pusheen|Smitha/', filter=False)
    print(output)
    output = nlp.semgrex(text, pattern='{tag: VBD}', filter=False)
    print(output)
