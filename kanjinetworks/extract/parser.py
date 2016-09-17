# -*- coding: utf-8 -*-

import argparse
import re

from kanjinetworks import Kanji

class KanjiNetworksParser():

    def parse(self, text):

        def kanji_from_line(line):
            match = re.match(r'^\s*(?P<kanji>.?)\s+\((?P<strokes>\d*)\)\s+(?P<pronunciation>.*)', line, flags=re.UNICODE)
            if match and match.group("kanji"):
                # print "match: %s" % match
                # print "groups:"
                # print match.groups()
                # print "0: %s" % match.group(0)
                # print "1: %s" % match.group(1)
                # print "2: %s" % match.group(2)
                # print "3: %s" % match.group(3)
                # print "kanji: %s" % match.group("kanji")
                # print "strokes: %s" % match.group("strokes")
                # print "pronunciation: %s" % match.group("pronunciation")
                kanji = Kanji()
                kanji.kanji = match.group("kanji").strip()
                kanji.strokes = int(match.group("strokes").strip())
                kanji.pronunciation = match.group("pronunciation").strip()
                kanji.definition = u""
                return kanji
            else:
                return None

        def kanji_append_definition(kanji, line):
            if not kanji.definition:
                kanji.definition = line
            else:
                kanji.definition += " "
                kanji.definition += line

        kanjis = list()

        class ParserState():
            LOOK_FOR_KANJI = 1
            RECORD_DEFINITION = 2
            LAST_LINE_EMPTY = 3

        state = ParserState.LOOK_FOR_KANJI
        current_kanji = None

        for line in text.split('\n'):
            # print "\n===\nline: %s" % line

            if state == ParserState.LOOK_FOR_KANJI:

                new_kanji = kanji_from_line(line)
                if new_kanji:
                    # print "new kanji found"

                    if current_kanji:
                        # print current_kanji
                        kanjis.append(current_kanji)

                    current_kanji = new_kanji
                    state = ParserState.RECORD_DEFINITION
                    continue

            if len(line):
                if current_kanji:
                    kanji_append_definition(current_kanji, line)
                    state = ParserState.RECORD_DEFINITION

            else:
                state = ParserState.LOOK_FOR_KANJI

        if current_kanji:
            # print current_kanji
            kanjis.append(current_kanji)
        return kanjis


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Parse a Kanji Network database text.')
    argparser.add_argument('text', type=str, help='Text to parse')
    args = argparser.parse_args()
    knparser = KanjiNetworksParser()
    kanjis = knparser.parse(args.text)
    for kanji in kanjis:
        print unicode(kanji)

import unittest

class TestParser(unittest.TestCase):

    def test_base(self):
        text = u'''
竏　(8)　キロリットル　
立 (ON reading: リツ) for the sound of リ(ッ) as an abbreviated transliteration of "liter" (リットル) +
千 one thousand → one *kiloliter*.
'''
        kanjis = KanjiNetworksParser().parse(text)
        self.assertEqual(len(kanjis), 1)
        kanji = kanjis[0]
        self.assertEqual(kanji.kanji, u'竏')
        self.assertEqual(kanji.strokes, 8)
        self.assertEqual(kanji.pronunciation, u'キロリットル')
        self.assertEqual(kanji.definition, u'立 (ON reading: リツ) for the sound of リ(ッ) as an abbreviated transliteration of "liter" (リットル) + 千 one thousand → one *kiloliter*.')


    def test_base2(self):
        text = u'''
古　(5)　コ；ふる（い・びる・めかしい）
The relevant oracle bone form of 古 combines 口 mouth + an object filling it → expectorate *old*,
*dried out*, *hard* food → *dry up*; *stale* → *used*; *old-fashioned*.
'''
        kanjis = KanjiNetworksParser().parse(text)
        self.assertEqual(len(kanjis), 1)
        kanji = kanjis[0]
        self.assertEqual(kanji.kanji, u'古')
        self.assertEqual(kanji.strokes, 5)
        self.assertEqual(kanji.pronunciation, u'コ；ふる（い・びる・めかしい）')
        self.assertEqual(kanji.definition, u'The relevant oracle bone form of 古 combines 口 mouth + an object filling it → expectorate *old*, *dried out*, *hard* food → *dry up*; *stale* → *used*; *old-fashioned*.')

    def test_starts_with_space(self):
        text = u'''
竍　(7)　デカリットル　
立 (ON reading: リツ) for the sound of リ(ッ) as an abbreviated transliteration of "liter" (リットル) +
十 ten → one *decaliter*.
'''
        kanjis = KanjiNetworksParser().parse(text)
        self.assertEqual(len(kanjis), 1)
        kanji = kanjis[0]
        self.assertEqual(kanji.kanji, u'竍')
        self.assertEqual(kanji.strokes, 7)
        self.assertEqual(kanji.pronunciation, u'デカリットル')
        self.assertEqual(kanji.definition, u'立 (ON reading: リツ) for the sound of リ(ッ) as an abbreviated transliteration of "liter" (リットル) + 十 ten → one *decaliter*.')

    def test_break_in_definition(self):
        text = u'''
虞 (13) グ;おそれ
As per 呉# (rowdy) + 虍 tiger → tigers locked in combat (compare 麌 and 牾). *Give careful thought to* is a borrowed meaning, as are *be anxious about*, *fear*, *apprehension* and

*concern*.
'''
        kanjis = KanjiNetworksParser().parse(text)
        self.assertEqual(len(kanjis), 1)
        kanji = kanjis[0]
        self.assertEqual(kanji.kanji, u'虞')
        self.assertEqual(kanji.strokes, 13)
        self.assertEqual(kanji.pronunciation, u'グ;おそれ')
        self.assertEqual(kanji.definition, u'As per 呉# (rowdy) + 虍 tiger → tigers locked in combat (compare 麌 and 牾). *Give careful thought to* is a borrowed meaning, as are *be anxious about*, *fear*, *apprehension* and *concern*.')

    def test_double_kanji(self):
        text = u'''
兒 (8) ジ;ニ  Shinjitai 児 (7)
The relevant seal inscription form shows, as depicted in 思, a profusion of fine bones in fontanels
(open spaces in an infant's skull over which the skull bones eventually fuse) + 儿 person → *infant*; (very young) *child*.
'''
        kanjis = KanjiNetworksParser().parse(text)
        self.assertEqual(len(kanjis), 1)
        kanji = kanjis[0]
        self.assertEqual(kanji.kanji, u'兒')
        self.assertEqual(kanji.strokes, 8)
        self.assertEqual(kanji.pronunciation, u'ジ;ニ  Shinjitai 児 (7)')
        self.assertEqual(kanji.definition, u'The relevant seal inscription form shows, as depicted in 思, a profusion of fine bones in fontanels (open spaces in an infant\'s skull over which the skull bones eventually fuse) + 儿 person → *infant*; (very young) *child*.')

    def test_break_between_kanji_and_definition(self):
        text = u'''
御 (12) ゴ;ギョ;お;おん;み

As per 卸# (whip) + 彳 movement → whip a horse in driving a chariot → *manage*; *control*; *tame*. Also, *honorary prefix* (originally, with reference to one who manages/controls).
*Defend* is a borrowed meaning via 禦.
'''
        kanjis = KanjiNetworksParser().parse(text)
        self.assertEqual(len(kanjis), 1)
        kanji = kanjis[0]
        self.assertEqual(kanji.kanji, u'御')
        self.assertEqual(kanji.strokes, 12)
        self.assertEqual(kanji.pronunciation, u'ゴ;ギョ;お;おん;み')
        self.assertEqual(kanji.definition, u'As per 卸# (whip) + 彳 movement → whip a horse in driving a chariot → *manage*; *control*; *tame*. Also, *honorary prefix* (originally, with reference to one who manages/controls). *Defend* is a borrowed meaning via 禦.')

    def test_multiple(self):
        text = u'''
蝴 (15) コ
As per 胡# (rough, covering substance) + 虫 insect/creature → insect/creature with a rough covering substance. The compound 蝴蝶 (sometimes written 胡蝶) refers to a butterfly.

祜 (10) コ;さいわ(い)
古# old + 示 altar/the supernatural → *prosperity* and *happiness* bestowed by the heavens
(accruing from proper veneration of ancestors).

呉 (7) ゴ
The relevant seal inscription form is 口# mouth + a head leaning forward → mouths figuratively intersecting in rowdy conversation. The pronunciation of the character simulates the sound of animated conversation, or quarreling. The ancient Chinese kingdom of Wu (Japanese: *Go*) is a borrowed meaning → *China*.
'''
        kanjis = KanjiNetworksParser().parse(text)
        kanjis = sorted(kanjis, key=lambda kanji: kanji.strokes)
        self.assertEqual(len(kanjis), 3)

        kanji = kanjis[0]
        self.assertEqual(kanji.kanji, u'呉')

        kanji = kanjis[1]
        self.assertEqual(kanji.kanji, u'祜')

        kanji = kanjis[2]
        self.assertEqual(kanji.kanji, u'蝴')

    def test_missing_kanji(self):
        text = u'''
  (5) シツ;シチ;しか(る)
口 mouth + 七# (cut) as well as for the sound to simulate scolding → *scold* in a sharp voice → *shout*; *reprove* (compare 咤).
'''
        kanjis = KanjiNetworksParser().parse(text)
        self.assertFalse(kanjis)
