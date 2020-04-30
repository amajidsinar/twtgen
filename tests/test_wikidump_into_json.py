import json
from twtgen.utils import read_wikidump

def test_combine_dump_txt():
    wikidump=read_wikidump(txt_file='tests/assets/test')
    titles = ["Asam deoksiribonukleat", "Anwar Sadat", "Azhar Mansor"]
    for (idx, (k, _)) in enumerate(wikidump.items()):
        assert titles[idx] == k

def test_combine_dump_json():
    wikidump=read_wikidump(txt_file='tests/assets/test')
    wikidump_json = json.dumps(wikidump)
    titles = ["Asam deoksiribonukleat", "Anwar Sadat", "Azhar Mansor"]
    wikidump_json=json.loads(wikidump_json)
    for (idx, (k, _)) in enumerate(wikidump_json.items()):
        assert titles[idx] == k


        

