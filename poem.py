#!/usr/bin/env python

from nltk.corpus import cmudict


class PoemGenerator:
    # constructor method for class
    def __init__(self, syllables=None):
        self.dictionary = cmudict.dict()
        self.syllables = syllables


    def generate(self):
        lines = []
        for syllable in self.syllables:
            line = self.generate_line(syllable)
            lines.append(line)

        return '\n'.join(lines)


    def number_of_syllables(self, word):
        #http://stackoverflow.com/questions/405161/detecting-syllables-in-a-word/4103234#4103234
        x = self.dictionary[word.lower()]
        phonemes = x[0]        
        length = len([phoneme for phoneme in phonemes if phoneme[-1].isdigit()])
        return length


    def generate_line(self, syllable):
        max_syllables = syllable

        # line = 'default line: %s' % syllable

        # 1) randomly grab a phrase from our phrase source
        # 2) count the syllables 
        # 3) subtract from max_syllables
        # 4) repeat until no syllables are left in max_syllables
        # * (need special logic to reject phrases that exceed the max syllables)

        return line


# function
def test_syllables():
    name = 'test poem'
    poem_generator = PoemGenerator()
    assert poem_generator.number_of_syllables('seven') == 2
    assert poem_generator.number_of_syllables('generator') == 4
    assert poem_generator.number_of_syllables('word') == 1
    assert poem_generator.number_of_syllables('discotheque') == 3
    print 'all good'



# function
def create_and_print_poem():
    name = 'test poem'
    poem_generator = PoemGenerator([5,7,5])
    poem = poem_generator.generate()
    print poem


if __name__ == "__main__":
    # test_syllables()
    # argparse if you want to parse command line arguments
    create_and_print_poem();