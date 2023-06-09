def count_digits_letters(sentence):
    
    sentence=sentence.upper()
    result_list=[0,0]
    for word in sentence.split():
        for letter in word:
            if ord(letter) in range(65,91):
                result_list[0]+=1
            elif ord(letter) in range(48,58):
                result_list[1]+=1
            
    
    return result_list

sentence="chennai-123"
print(count_digits_letters(sentence))
