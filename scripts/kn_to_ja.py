#!/usr/bin/env python2

import argparse

from kanjinetworks import get_text
from kanjinetworks import KanjiNetworksParser
from kanjinetworks import JapaneseAppExporter

# def statistics(text):
#     number_of_empty_lines = 0
#     for line in text.split('\n'):
#         if not len(line):
#             number_of_empty_lines = number_of_empty_lines + 1
#     print "number_of_empty_lines %s" % number_of_empty_lines

if __name__ == "__main__":

    argparser = argparse.ArgumentParser(description='Replace notes in a backup file from the Japanese iOS app with Kanji Networks etymologies.')
    argparser.add_argument('filename', type=str, help='Japanese app backup file')
    args = argparser.parse_args()

    text = get_text()
    statistics(text)

    kanjis = KanjiNetworksParser().parse(text)
    # for kanji in kanjis:
    #     print unicode(kanji)
    print "imported %s kanjis" % len(kanjis)

    JapaneseAppExporter().replace_notes_in_file(args.filename, kanjis)