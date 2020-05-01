import json
from twtgen.utils import read_wikidump, count_vocab
from spacy.lang.id import stop_words

def test_read_wikidump_medium():
    wikidump=read_wikidump(wikidump_path='tests/assets/wikidump/medium')
    titles = ["Asam deoksiribonukleat", "Anwar Sadat", "Azhar Mansor"]
    for (idx, (k, _)) in enumerate(wikidump.items()):
        assert titles[idx] == k

def test_read_wikidump_small_1():
    wikidump=read_wikidump(wikidump_path='tests/assets/wikidump/small_1')
    assert wikidump['Boy']=='Namaku "Boy". Aku adalah anak tunggal'
    assert wikidump['BIN']=="kijang satu, kijang dua, ganti !!!"
    assert list(wikidump.keys()) == ['Boy', 'BIN']

def test_read_wikidump_small_2():
    wikidump=read_wikidump(wikidump_path='tests/assets/wikidump/small_2')
    assert wikidump['Peradaban']=="""Lagu Peradaban jauh lebih keras dari lagu metal apapun yang pernah kami dengar, geramnya sampai kebas."""
    assert wikidump['pergijauh vs wordfangs']=="""Kalo lu denger rock terus bertahun-tahun lo akan bosen gitu. Sekarang anak-anak udah gak denger rock lagiGue masih denger sih"""
    assert list(wikidump.keys()) == ['Peradaban', 'pergijauh vs wordfangs']


def test_join_wikidump_small():
    wikidump = {}
    wikidump_paths = ['tests/assets/wikidump/small_1', 'tests/assets/wikidump/small_2']
    for wikidum_path in wikidump_paths:
        wikidump.update(read_wikidump(wikidump_path=wikidum_path))
    assert wikidump['Boy']=='Namaku "Boy". Aku adalah anak tunggal'
    assert wikidump['BIN']=="kijang satu, kijang dua, ganti !!!"
    assert wikidump['Peradaban']=="""Lagu Peradaban jauh lebih keras dari lagu metal apapun yang pernah kami dengar, geramnya sampai kebas."""
    assert wikidump['pergijauh vs wordfangs']=="""Kalo lu denger rock terus bertahun-tahun lo akan bosen gitu. Sekarang anak-anak udah gak denger rock lagiGue masih denger sih"""


def test_count_vocab_1():
    text = """Namaku Boy. Aku adalah anak tunggal."""
    sw = stop_words.STOP_WORDS
    result = count_vocab(text, sw)
    assert list(result.keys()) == ['namaku', 'boy', 'anak', 'tunggal']
    assert result['namaku']==1
    assert result['boy']==1
    assert result['anak']==1
    assert result['tunggal']==1
    


def test_count_vocab_2():
    text = """kijang satu, kijang dua, ganti !!!"""
    sw = stop_words.STOP_WORDS
    result = count_vocab(text, sw)
    
    assert list(result.keys()) == ['kijang', 'ganti']
    assert result['kijang']==2
    assert result['ganti']==1