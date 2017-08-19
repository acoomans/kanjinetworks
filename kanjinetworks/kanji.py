class Kanji():

    def __init__(self):
        self.kanji = None
        self.strokes = 0
        self.pronunciation = None
        self.definition = ""
        self.kanji_shinjitai = None
        self.strokes_shinjitai = 0

    def __unicode__(self):
        if self.kanji_shinjitai:
            ks = " (%s)" % self.kanji_shinjitai
        if self.strokes_shinjitai:
            ss = " (%s)" % self.strokes_shinjitai
        return u"<kanji: %s%s, strokes: %s%s, pronunciation: %s, definition: %s>" % (self.kanji, ks, self.strokes, ss, self.pronunciation, self.definition)