print("Enter a semtence :")
my_sentence=input()

def word_frequency_calc(sentence):
    final_dictionary={}
    for word in sentence.split():
        if word not in final_dictionary:
            final_dictionary[word]=1
        else:
            final_dictionary[word]+=1
    return final_dictionary

print(word_frequency_calc(my_sentence))
    
