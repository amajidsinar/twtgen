import json
import argparse

parser = argparse.ArgumentParser(description="Testing pipeline for predicting gender based on face")
parser.add_argument('-i', '--input', type=str, required=True)

args = parser.parse_args()

with open(args.input, 'r') as reader:
    data=json.load(reader)

print(data)