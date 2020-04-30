import json
import argparse
from spacy.lang.id import Indonesian
from twtgen.utils import read_wikidump
from pathlib import Path

parser = argparse.ArgumentParser(description="Testing pipeline for predicting gender based on face")
parser.add_argument('-i', '--input', type=str, required=True)

args = parser.parse_args()



for txt in Path(args.input).rglob('*'):
    data = read_wikidump(txt)
    nlp = Indonesian(data)   


import pdb; pdb.set_trace()
