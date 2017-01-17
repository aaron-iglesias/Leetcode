# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation 
# is unique if no other word from the dictionary has the same abbreviation.

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        self.d = {}
        for w in dictionary:
            key = self.abbreviate(w)
            if key in self.d:
                self.d[key].append(w)
            else:
                self.d[key] = [w]

    def isUnique(self, word):
        key = self.abbreviate(word)
        return key not in self.d or (len(self.d[key]) == 1 and self.d[key][0] == word)
    
    def abbreviate(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[len(word) - 1]