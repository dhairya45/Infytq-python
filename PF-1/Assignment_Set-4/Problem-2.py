#lex_auth_01269444195664691284
"""
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.
"""
def encrypt_sentence(sentence):
    x=""
    count=0
    vowels=['a','e','i','o','u']
    split=sentence.split()
    for i in sentence.split():
        if count%2==0:
            x=x+i[::-1]+" "
            count+=1
        else:
            vowels=['a','e','i','o','u']
            c=""
            v=""
            for j in i:
                if j in vowels:
                    v+=j
                else:
                    c+=j
            count+=1
            x=x+c+v+" "
    
    x=x.rstrip()
    return x
                

sentence="She sells sea shells on the sea shore"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
