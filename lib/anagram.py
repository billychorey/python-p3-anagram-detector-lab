# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list):
        matches = []

        for word in word_list:
            lowercase_word = self.word.lower()
            lowercase_anagram = word.lower()

            if sorted(lowercase_word) == sorted(lowercase_anagram):
                matches.append(word)

        return matches