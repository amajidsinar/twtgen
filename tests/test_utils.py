import json
from twtgen.utils import read_wikidump, count_vocab
from spacy.lang.id import stop_words
from collections import defaultdict


def test_read_wikidump_medium():
    wikidump = read_wikidump(wikidump_path="tests/assets/wikidump/medium")
    titles = ["Asam deoksiribonukleat", "Anwar Sadat", "Azhar Mansor"]
    for (idx, (k, _)) in enumerate(wikidump.items()):
        assert titles[idx] == k


def test_read_wikidump_small_1():
    wikidump = read_wikidump(wikidump_path="tests/assets/wikidump/small_1")
    assert (
        wikidump["Peradaban"]
        == """Lagu Peradaban jauh lebih keras dari lagu metal apapun yang pernah kami dengar, geramnya sampai kebas."""
    )
    assert (
        wikidump["pergijauh vs wordfangs"]
        == """Kalo lu denger rock terus bertahun-tahun lo akan bosen gitu. Sekarang anak-anak udah gak denger rock lagiGue masih denger sih"""
    )
    assert (
        wikidump["No debat"] == """Peradaban adalah musik tersangar di bumi. no debat"""
    )
    assert (
        wikidump["ngabuburit"]
        == """Ngabuburit nunggu sore Jam 5 sambil dengerin PeradabanBtw pecinta metal wajib denger lagu ini"""
    )
    assert list(wikidump.keys()) == [
        "Peradaban",
        "pergijauh vs wordfangs",
        "No debat",
        "ngabuburit",
    ]


def test_read_wikidump_small_2():
    wikidump = read_wikidump(wikidump_path="tests/assets/wikidump/small_2")
    assert wikidump["Hafal peradaban"] == """hafal peradaban doesn't make him stay"""
    assert wikidump["Peradaban III"] == """Peradaban vs everybody"""
    assert (
        wikidump["Peradaban IV"]
        == """Bayi ngomong peradaban jauh lebih keras dari lagu metal manapun"""
    )
    assert list(wikidump.keys()) == ["Hafal peradaban", "Peradaban III", "Peradaban IV"]


def test_join_wikidump_small():
    wikidump = {}
    wikidump_paths = ["tests/assets/wikidump/small_1", "tests/assets/wikidump/small_2"]
    for wikidum_path in wikidump_paths:
        wikidump.update(read_wikidump(wikidump_path=wikidum_path))
    assert (
        wikidump["Peradaban"]
        == """Lagu Peradaban jauh lebih keras dari lagu metal apapun yang pernah kami dengar, geramnya sampai kebas."""
    )
    assert (
        wikidump["pergijauh vs wordfangs"]
        == """Kalo lu denger rock terus bertahun-tahun lo akan bosen gitu. Sekarang anak-anak udah gak denger rock lagiGue masih denger sih"""
    )
    assert (
        wikidump["No debat"] == """Peradaban adalah musik tersangar di bumi. no debat"""
    )
    assert (
        wikidump["ngabuburit"]
        == """Ngabuburit nunggu sore Jam 5 sambil dengerin PeradabanBtw pecinta metal wajib denger lagu ini"""
    )
    assert wikidump["Hafal peradaban"] == """hafal peradaban doesn't make him stay"""
    assert wikidump["Peradaban III"] == """Peradaban vs everybody"""
    assert (
        wikidump["Peradaban IV"]
        == """Bayi ngomong peradaban jauh lebih keras dari lagu metal manapun"""
    )
    assert list(wikidump.keys()) == [
        "Peradaban",
        "pergijauh vs wordfangs",
        "No debat",
        "ngabuburit",
        "Hafal peradaban",
        "Peradaban III",
        "Peradaban IV",
    ]


def test_count_vocab_1():
    text = """Namaku Boy. Aku adalah anak tunggal. Kijang adalah hewan kesukaanku"""
    sw = stop_words.STOP_WORDS
    result = count_vocab(text, sw)
    assert list(result.keys()) == [
        "namaku",
        "boy",
        "anak",
        "tunggal",
        "kijang",
        "hewan",
        "kesukaanku",
    ]
    assert result["namaku"] == 1
    assert result["boy"] == 1
    assert result["anak"] == 1
    assert result["tunggal"] == 1
    assert result["kijang"] == 1
    assert result["hewan"] == 1
    assert result["kesukaanku"] == 1


def test_count_vocab_2():
    text = """kijang satu, kijang dua, ganti !!!"""
    sw = stop_words.STOP_WORDS
    result = count_vocab(text, sw)

    assert list(result.keys()) == ["kijang", "ganti"]
    assert result["kijang"] == 2
    assert result["ganti"] == 1


def test_count_vocab_3():
    text1 = """Namaku Boy. Aku adalah anak tunggal. Kijang adalah hewan kesukaanku."""
    text2 = """kijang satu, kijang dua, ganti !!!"""
    sw = stop_words.STOP_WORDS
    result = count_vocab([text1, text2], sw)
    assert list(result.keys()) == [
        "namaku",
        "boy",
        "anak",
        "tunggal",
        "kijang",
        "hewan",
        "kesukaanku",
        "ganti",
    ]
    assert result["namaku"] == 1
    assert result["boy"] == 1
    assert result["anak"] == 1
    assert result["tunggal"] == 1
    assert result["kijang"] == 3
    assert result["hewan"] == 1
    assert result["kesukaanku"] == 1
    assert result["ganti"] == 1
