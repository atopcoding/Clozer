import splitter
from fitbert import FitBert

def cloze(ques):

    spl = splitter.splitter(ques)

    fb = FitBert()

    masked = spl[0]

    options = spl[1:]

    return fb.fitb(masked, options)

