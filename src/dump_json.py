import json
import re
from collections import defaultdict
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Testing pipeline for predicting gender based on face")
parser.add_argument('-i', '--input', type=str, required=True)
parser.add_argument('-o', '--output', type=str, default='dumping')

args = parser.parse_args()



# for file in Path(args.input).rglob('*'):
#     if file.is_file():
#         dicts
        

print(f'Dumping {args.output}')
with open(f'{args.output}', 'w') as writer:
    json.dump(dicts, writer)




