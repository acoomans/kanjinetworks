#!/usr/bin/env python2

import argparse

from kanjinetworks import get_text
from kanjinetworks import KanjiNetworksParser
from kanjinetworks import JapaneseApp3Exporter, JapaneseApp4Exporter

# def statistics(text):
#     number_of_empty_lines = 0
#     for line in text.split('\n'):
#         if not len(line):
#             number_of_empty_lines = number_of_empty_lines + 1
#     print "number_of_empty_lines %s" % number_of_empty_lines

if __name__ == "__main__":

    argparser = argparse.ArgumentParser(description='Replace notes in a backup file from the Japanese iOS app with Kanji Networks etymologies.')
    argparser.add_argument('filename', type=str, help='Japanese app backup file')
    argparser.add_argument('-v', '--version', type=int, help='Japanese app version (3,4)', default=4)
    args = argparser.parse_args()

    text = get_text()
    # statistics(text)

    kanjis = KanjiNetworksParser().parse(text, split_shinjitai=True)
    # for kanji in kanjis:
    #     print unicode(kanji)
    print "imported %s kanjis" % len(kanjis)

    if args.version is 3:
        print "exporting to version 3 ..."
        JapaneseApp3Exporter().replace_notes_in_file(args.filename, kanjis)
    if args.version is 4:
        print "exporting to version 4 ..."
        JapaneseApp4Exporter().replace_notes_in_file(args.filename, kanjis)