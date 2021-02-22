import splitter
from fitbert import FitBert

def cloze(ques):
    spl = splitter.splitter(ques) #Splits based on splitter
    fb = FitBert()

    masked = spl[0]

    options = spl[1:]

    return fb.fitb(masked, options)

