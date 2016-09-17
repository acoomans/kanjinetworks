class Kanji():

    def __init__(self):
        self.kanji = None
        self.strokes = 0
        self.pronunciation = None
        self.definition = ""

    def __unicode__(self):
        return u"<kanji: %s, strokes: %s, pronunciation: %s, definition: %s>" % (self.kanji, self.strokes, self.pronunciation, self.definition)