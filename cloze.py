import splitter, re
from fitbert import FitBert

def clozer(ques):
    spl = splitter.splitter(ques) #preprocess the string

    fb = FitBert() 

    masked = spl[0]
    options = spl[1:]

    #Split the question statement into tokens
    tokens = re.findall(r"[\w']+|[.,!?;]", masked)

    res = []
    for i in range(len(tokens)): #tries to insert a ***mask*** token between every word except the last full stop
        _tok = tokens.copy() #just copies the value
        _tok.insert(i, "***mask***") 
        masked = ' '.join(_tok) #turns _tok back into a string
        predictions = fb.rank_with_prob(masked, options)
        res.append([predictions[1][0], masked.replace("***mask***", predictions[0][0])])

    ans = max(res, key = lambda x: x[0]) #gets max entry based on score

    return ans[1]
