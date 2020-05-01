import json
from twtgen.utils import read_wikidump, count_vocab
from spacy.lang.id import stop_words

def test_read_wikidump_medium():
    wikidump=read_wikidump(txt_file='tests/assets/dummy_medium')
    titles = ["Asam deoksiribonukleat", "Anwar Sadat", "Azhar Mansor"]
    for (idx, (k, _)) in enumerate(wikidump.items()):
        assert titles[idx] == k

def test_read_wikidump_small():
    wikidump=read_wikidump(txt_file='tests/assets/dummy_small_1')
    titles = ["Boy", "BIN"]
    for (idx, (k, _)) in enumerate(wikidump.items()):
        assert titles[idx] == k


def test_count_vocab_1():
    text = """Namaku Boy. Aku adalah anak tunggal."""
    sw = stop_words.STOP_WORDS
    result = count_vocab(text, sw)
    assert result['namaku']==1
    assert result['boy']==1
    assert result['aku']==1
    assert result['anak']==1
    assert result['tunggal']==1


def test_count_vocab_2():
    text = """kijang satu, kijang dua, ganti !!!"""
    sw = stop_words.STOP_WORDS
    result = count_vocab(text, sw)
    assert result['kijang']==2
    assert result['ganti']==1