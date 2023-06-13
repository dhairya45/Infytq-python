"""
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

Rules are as follows: 
a. Spaces are to be retained as is 
b. Each word should be encoded separately

If a word has only vowels then retain the word as is

If a word has a consonant (at least 1) then retain only those consonants
"""

def sms_encoding(data):
    output=""
    vowel=["a",'e','i','o','u',"I"]
    for x in data.split():
        if len(x)==1:
           output=output+x
        else :
           for t in x: 
            if t in vowel :
               x.replace(t,"")
            else:
                output=output+t

        output=output+" "
    output=output.rstrip()
    return output
                
               
data="I love Python"
print(sms_encoding(data))
