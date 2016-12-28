import random
from nltk.corpus import cmudict


def number_of_syllables(list_of_words):
  dictionary = cmudict.dict()
# here, the list of words makes it intact -- all words in phrase are present
  print list_of_words
# however, this only returns the first word and its length?!
  for word in list_of_words:
    call_dictionary =  dictionary[word.lower()]
    phonemes = call_dictionary[0]
### cody's version: 
    length = len([phoneme for phoneme in phonemes if phoneme[-1].isdigit()])
### posted version -- does not work?:
### length = len([y for y in x if y[-1].isdigit()] for x in phonemes)
    print word
    print length
    return length


def line_generate():
  # open the file
  target = open("phrases.txt")
  # read the file
  all_phrases = target.read()
  # split the file into a list of lines
  #   (could possibly use readline() here?)
  list_of_phrases = all_phrases.splitlines()
  # select one line from the list at random
  phrase = random.choice(list_of_phrases)
  return phrase
  target.close()


# call the line generator
display_phrase = line_generate()

# split the line into a list of words to be analyzed
list_of_words = display_phrase.split()

# grab number of syllables in each word in the list
number_of_syllables(list_of_words)





###########################



  # next steps:
  #
  # 1. add syllables in phrase
  # 2. compare with max_syllables
  # 3. use if/elif to keep or discard:
  #
  # if phrase_syllables == max_syllables:
  # return phrase
  # elif phrase_syllables >= max_syllables:
  # try again
  # elif phrase_syllables <= max_syllables:
  # return phrase
  # max_syllables = max_syllables - phrase_syllables
  #
  # use append() / extend() to add lines to new file





#def divide_phrase():
  # split the line into a list of words
# list_of_words = display_phrase.split()
  # iterate through the list and grab each word at a time
  # hmmm... only grabs the first word...
  #while True:
# return list_of_words
  #for word in list_of_words_in_phrase:
  # print word # all words print
  # return words



#divide_phrase()


# retrieve word(s) from the generated line
#got_word = divide_phrase()
#print got_word

# send (each) word to the syllable counter
#display_syllables = number_of_syllables(got_word)
#print display_syllables











# possibilities for line and stanza generator
#
# from sys import argv
#
# script, stanzas, lines = argv
# raw_key = raw_input('Please enter randomizer key for syllable count: ')
#
# number_of_stanzas = int(stanzas)
# number_of_lines = int(lines)
# syllable_key = str(raw_key)
#
# print "Your poem has %d stanzas." % number_of_stanzas
# print "Your poem has %d lines." % number_of_lines
# print "The randomizer key for your poem is %s." % syllable_key