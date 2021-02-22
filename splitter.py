import re

def splitter(string):
    re.sub('(\s)*', ' ', string.strip()) #removes extra spaces
    raw = re.split(" *\([A-Z]\) *", string) #Split into problem statement and options
    number = re.search('[0-9]+\s*\.', raw[0])
    print("number = " + number.group(0))
    if(number): #Removes problem number
        raw[0] = raw[0].replace(number.group(0), '').strip()
    else:
        print("No problem number found.")

    raw[0] = re.sub('_+', '***mask***', raw[0]) #turns underscores into ***mask***

    raw = [x.lower() for x in raw] #using BERT uncased

    return raw
