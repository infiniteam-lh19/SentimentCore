# SentimentCore
Core Runtime for infiniteam-lh19 LauzHack project

## Install
pip install -r requirements.txt
python3 main.py

python console
'import nltk
nltk.download()'

install wordnet, punkt tokenizer

## Install sentiment analyzer library
cd SentimentCore
git clone https://github.com/xiaohan2012/twitter-sent-dnn sentdnn
cd sentdnn
git fetch origin pull/6/head:python3
git checkout python3
