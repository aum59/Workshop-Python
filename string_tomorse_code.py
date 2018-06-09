#!/usr/bin/python
import sys
def stringTomorse(string):
    char_morse = ['.-','-...','-.-.','-..','.',
		      '..-.','--.','....','..','.---',
		      '-.-','.-..','--','-.','---',
		      '.--.','--.-','.-.','...','-',
		      '..-','...-','.--','-..-','-.--',
		      '--..','.----','..---','...--','....-',
		      '.....','-....','--...','---..','----.',
		      '-----',' ']
    char_text = ['A','B','C','D','E',
                 'F','G','H','I','J',
                 'K','L','M','N','O',
                 'P','Q','R','S','T',
                 'U','V','W','X','Y',
                 'Z','1','2','3','4',
                 '5','6','7','8','9','0',' ']
    code = ''
    for i in string:
        code += char_morse[char_text.index(i)] + ' '
    return code
text = ''
if len(sys.argv) > 1 :
    text = stringTomorse(str(sys.argv[1]).upper())
    print(str(sys.argv[1]).upper() + ' is => ' + text)
else :
    text = stringTomorse('PYTHON')
    print('PYTHON is => ' + text)
