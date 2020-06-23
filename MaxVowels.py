from math import  inf

class Vowels:

    def __init__(self, words ):
        #properties
        self.words  = words
        self.answer = None

    def countVowelsForWord(self, word ):
        counter = 0
        # for loop to go through character by character
        for i in range(0, len(word) ):
            char = word[i]
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                counter = counter + 1
        # for- loop complete
        return counter

    def determineMaxVowelWord(self):
        pair = []   # element = {word, count}
                    #           {"hello", 2}
                    #           {"world", 1}

        # assign words a count
        for i in range(0 , len(self.words) ):
            word   = self.words[i]
            countW = self.countVowelsForWord(word)
            pair.append( (word, countW) )

        maxw = ""
        maxc = -inf

        # find max vowel word
        for i in range(0, len(pair) ):
            w = pair[i][0]  # name
            c = pair[i][1]  # count

            # comparing the count to our max value
            if c >= maxc:
                maxw = w  # name is changed
                maxc = c  # count is changed

        self.answer = (maxw, maxc)
        return self.answer  # return answer



object1 =  Vowels( ["hello", "world"] )
# print( object1.determineMaxVowelWord() )

object2 =  Vowels( ["Zumi", "Codrone", "Rokit", "Robolink"] )
print( object2.determineMaxVowelWord() )

