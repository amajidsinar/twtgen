import re
from collections import defaultdict
from spacy.lang.id import Indonesian
import string

def read_wikidump(txt_file: str):
    dicts = defaultdict(str)
    with open(txt_file, 'r') as reader:
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


def count_vocab(text, stopwords):
    nlp = Indonesian()
    indonesian = nlp(text)
    vocab = defaultdict(int)
    for token in indonesian:
        if token.text not in stopwords and token.text not in string.punctuation:
            vocab[token.text.lower()] += 1
    return vocab