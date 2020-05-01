import re
from collections import defaultdict
from spacy.lang.id import Indonesian
import string
from typing import Union, List

def read_wikidump(wikidump_path: str):
    dicts = defaultdict(str)
    with open(wikidump_path, 'r') as reader:
        for line in reader:
            if re.search("^<doc.id=", line):
                title_start_idx = re.search(".title=", line).end() + 1
                title = line[title_start_idx:-3]
                print(f'Start processing {title}')
            elif re.search("^</doc>", line):
                continue
            elif line.rstrip()==title:
                print(f'End processing {title}')
                continue
            elif line=='\n':
                continue
            else:
                dicts[title] += line.rstrip()
    return dicts


def count_vocab(text: Union[str, List[str]], stopwords: set):
    nlp = Indonesian()
    if isinstance(text, str):
        text = [text]
    vocab = defaultdict(int)
    for _text in text:
        indonesian = nlp(_text)
        for token in indonesian:
            token_lowercase = token.text.lower()
            if  token_lowercase not in stopwords and re.search(token_lowercase, string.punctuation) is None:
                vocab[token.text.lower()] += 1
    return vocab