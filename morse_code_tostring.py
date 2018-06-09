#!/usr/bin/python
import sys
code = '.-. .---- .--. ... .- -- ..- ...-- .-.. -- ----- .-. ... ...--'
morse = []
text = ''
def morseTostring(string):
        char_morse = ['.-','-...','-.-.','-..',
                      '.','..-.','--.','....',
                      '..','.---','-.-','.-..',
                      '--','-.','---','.--.',
                      '--.-','.-.','...','-',
                      '..-','...-','.--','-..-',
                      '-.--','--..','.----','..---',
                      '...--','....-','.....',
                      '-....','--...','---..','----.',
                      '-----']
        char_text = ['A','B','C','D','E',
                     'F','G','H','I','J',
                     'K','L','M','N','O',
                     'P','Q','R','S','T',
                     'U','V','W','X','Y',
                     'Z','1','2','3','4',
                     '5','6','7','8','9',
                     '0']
        return char_text[char_morse.index(string)]

if len(sys.argv) > 1 :
        for i in range(len(sys.argv)) :
                if i >= 1 : morse.append(sys.argv[i])
        for i in morse :
                text += morseTostring(i)
        print('string is => ' + text)
else :
        morse = code.split(" ")
        for i in morse :
                text += morseTostring(i)
        print('string is => ' + text)
