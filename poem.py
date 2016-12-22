#!/usr/bin/env python


class PoemGenerator:
    # constructor method for class
    def __init__(self, syllables):
        self.syllables = syllables


    def generate(self):
        lines = []
        for syllable in self.syllables:
            line = self.generate_line(syllable)
            lines.append(line)

        return '\n'.join(lines)


    def generate_line(self, syllable):
        line = 'default line: %s' % syllable
        return line


# function
def create_and_print_poem():
    name = 'test poem'
    poem_generator = PoemGenerator([5,7,5])    
    poem = poem_generator.generate()
    print poem


if __name__ == "__main__":
    #argparse if you want to parse command line arguments
    create_and_print_poem();