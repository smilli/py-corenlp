from distutils.core import setup
setup(
  name = 'pycorenlp',
  packages = ['pycorenlp'],
  version = '0.2.0',
  description = 'Python wrapper for Stanford CoreNLP',
  author = 'Smitha Milli',
  author_email = 'smitha.milli@gmail.com',
  url = 'https://github.com/smilli/py-corenlp',
  download_url = 'https://github.com/smilli/py-corenlp/tarball/0.2',
  keywords = ['nlp'],
  classifiers = [],
  install_requires = [
    'requests'
  ]
)
