# -*- coding: utf-8 -*-

import json
import gzip


class JapaneseAppBaseExporter:

    def kanjis_to_notes_json(self, kanjis):
        return json.dumps(self.kanjis_to_notes(kanjis))

    def replace_notes_in_file(self, path, kanjis):

        with gzip.GzipFile(path, "rb") as file:
            contents = file.read()

        d = json.loads(contents)
        d["notes"] = self.kanjis_to_notes(kanjis)
        contents = json.dumps(d)

        with gzip.GzipFile(path, "wb") as file:
            file.write(contents)

class JapaneseApp3Exporter(JapaneseAppBaseExporter):

    def kanjis_to_notes(self, kanjis):
        notes = dict()

        for kanji in kanjis:
            kanji_dict = dict(
                updatedAt="2016-09-11T20:40:19+0000",
                text=u"[%s] %s" % (kanji.kanji, kanji.definition)
            )
            code = str(ord(kanji.kanji))
            notes[code] = kanji_dict

        return notes

class JapaneseApp4Exporter(JapaneseAppBaseExporter):

    def kanjis_to_notes(self, kanjis):
        notes = []

        for kanji in kanjis:
            kanji_dict = dict(
                id=str(ord(kanji.kanji)),
                updatedAt="2017-08-19T20:40:19+0000",
                text=u"[%s] %s" % (kanji.kanji, kanji.definition)
            )
            notes.append(kanji_dict)

        return notes


import unittest
from kanjinetworks.extract.parser import KanjiNetworksParser

class TestJapaneseApp3Exporter(unittest.TestCase):

        def test_kanjis_to_notes(self):

            text = u'''
艝 (17) そり
雪 snow + 舟 boat → (boat-shaped) *sleigh*; *sled*. Compare 橇 and 轌.

轌 (18) そり
雪 snow + 車 vehicle → *sleigh*; *sled*. Compare 橇 and 艝.

萢 (11) やら
苞 miscanthus + 水 water → *wetlands*; *marshland* (← place where miscanthus plants flourish).
'''

            kanjis = KanjiNetworksParser().parse(text)
            j = JapaneseApp3Exporter().kanjis_to_notes_json(kanjis)
            notes = json.loads(j)

            self.assertIsInstance(notes, dict)

            self.assertIsInstance(notes["33373"], dict)
            self.assertIsInstance(notes["33373"]["updatedAt"], unicode)
            self.assertIsInstance(notes["33373"]["text"], unicode)
            self.assertTrue(len(notes["33373"]["updatedAt"]))
            self.assertTrue(len(notes["33373"]["text"]))

            self.assertIsInstance(notes["36684"], dict)
            self.assertIsInstance(notes["36684"]["updatedAt"], unicode)
            self.assertIsInstance(notes["36684"]["text"], unicode)

            self.assertIsInstance(notes["33826"], dict)
            self.assertIsInstance(notes["33826"]["updatedAt"], unicode)
            self.assertIsInstance(notes["33826"]["text"], unicode)


class TestJapaneseApp4Exporter(unittest.TestCase):
    def test_kanjis_to_notes(self):
        text = u'''
艝 (17) そり
雪 snow + 舟 boat → (boat-shaped) *sleigh*; *sled*. Compare 橇 and 轌.

轌 (18) そり
雪 snow + 車 vehicle → *sleigh*; *sled*. Compare 橇 and 艝.

萢 (11) やら
苞 miscanthus + 水 water → *wetlands*; *marshland* (← place where miscanthus plants flourish).
'''

        kanjis = KanjiNetworksParser().parse(text)
        j = JapaneseApp4Exporter().kanjis_to_notes_json(kanjis)
        notes = json.loads(j)

        self.assertIsInstance(notes, list)

        self.assertIsInstance(notes[0], dict)
        self.assertIsInstance(notes[0]["id"], unicode)
        self.assertIsInstance(notes[0]["updatedAt"], unicode)
        self.assertIsInstance(notes[0]["text"], unicode)
        self.assertEquals(notes[0]["id"], "33373")
        self.assertTrue(len(notes[0]["updatedAt"]))
        self.assertTrue(len(notes[0]["text"]))

        self.assertIsInstance(notes[1], dict)
        self.assertIsInstance(notes[1]["id"], unicode)
        self.assertIsInstance(notes[1]["updatedAt"], unicode)
        self.assertIsInstance(notes[1]["text"], unicode)
        self.assertEquals(notes[1]["id"], "36684")
        self.assertTrue(len(notes[1]["updatedAt"]))
        self.assertTrue(len(notes[1]["text"]))

        self.assertIsInstance(notes[2], dict)
        self.assertIsInstance(notes[2]["id"], unicode)
        self.assertIsInstance(notes[2]["updatedAt"], unicode)
        self.assertIsInstance(notes[2]["text"], unicode)
        self.assertEquals(notes[2]["id"], "33826")
        self.assertTrue(len(notes[2]["updatedAt"]))
        self.assertTrue(len(notes[2]["text"]))
