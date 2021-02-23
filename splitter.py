import re

def splitter(string):
    string = re.sub('[\n\r\s]+', ' ', string).strip()
    raw = re.split(" *\([A-Z]\) *", string) #Split into problem statement and options
    number = re.search('[0-9]+\s*\.', raw[0])
    if(number): #Removes problem number
        print("Question Number = " + number.group(0))
        raw[0] = raw[0].replace(number.group(0), '').strip()
    else:
        print("No problem number found.")

    raw[0] = re.sub('_+', '', raw[0]) #deletes all underscores

    raw = [x.lower() for x in raw] #using BERT uncased

    return raw





