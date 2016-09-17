Kanji Networks
==============

kanjinetworks is an interface for the Kanji Networks database.

[![Build](https://api.travis-ci.org/acoomans/kanjinetworks.png)](https://travis-ci.org/acoomans/kanjinetworks)
[![Pypi version](http://img.shields.io/pypi/v/kanjinetworks.svg)](https://pypi.python.org/pypi/kanjinetworks)
[![Pypi license](http://img.shields.io/pypi/l/kanjinetworks.svg)](https://pypi.python.org/pypi/kanjinetworks)
![Python 2](http://img.shields.io/badge/python-2-blue.svg)

## Description

[Kanji Networks](http://www.kanjinetworks.com) was a website offering etymologies for kanjis. The website was closed end of August 2016, but the database was made available as a PDF.

kanjinetworks is an interface for extracting, parsing and exporting the etymologies from the PDF file in python.

The package also include the `kn_to_ja.py` script to import the Kanji Networks etymologies into a [iOS Japanese App](https://japaneseapp.com/) backup files as notes. Warning: existing notes might be lost as this script replaces them.

## Requirements

kanjinetworks is compatible with Python versions 2 and depends on PDF miner.

## Install

To install kanjinetworks, run pip:

	pip install kanjinetworks
	
or clone this directory and run setup:

    python setup.py install

## Usage

To import etymologies into a Japanese App backup files:
	
	kn_to_ja.py PATH_TO_JAPANESE_BACKUP_FILE
	
To use the parser:

	from kanjinetworks import get_text
	from kanjinetworks import KanjiNetworksParser
	
    text = get_text()

    kanjis = KanjiNetworksParser().parse(text)
    for kanji in kanjis:
		print unicode(kanji)

# Credits

The Etymological Dictionary of Han/Chinese Characters is by Lawrence J. Howell / Research Collaborator Hikaru Morimoto / Kanji Networks (http://www.kanjinetworks.com).

File distributed with the permission of the author.

