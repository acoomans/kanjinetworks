# -*- coding: utf-8 -*-

import json
import gzip

class JapaneseAppExporter:

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


import unittest
from kanjinetworks.extract.parser import KanjiNetworksParser

class TestJapaneseAppExporter(unittest.TestCase):

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
            j = JapaneseAppExporter().kanjis_to_notes_json(kanjis)
            notes = json.loads(j)

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