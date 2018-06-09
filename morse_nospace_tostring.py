#!/usr/bin/python
import sys,json
## code = '.-. .---- .--. ... .- -- ..- ...-- .-.. -- ----- .-. ... ...--'
code = '.-..----.--.....---..-...--.-..-------.-.......--'
data = {}
text = []
def morseTochar(morse_string):
	char_morse = ['.-','-...','-.-.','-..','.',
		      '..-.','--.','....','..','.---',
		      '-.-','.-..','--','-.','---',
		      '.--.','--.-','.-.','...','-',
		      '..-','...-','.--','-..-','-.--',
		      '--..','.----','..---','...--','....-',
		      '.....','-....','--...','---..','----.',
		      '-----'];
	char_text = ['A','B','C','D','E',
		      'F','G','H','I','J',
		      'K','L','M','N','O',
		      'P','Q','R','S','T',
		      'U','V','W','X','Y',
		      'Z','1','2','3','4',
		      '5','6','7','8','9',
		      '0'];
	morse = ''
	ch = ''
	for i in morse_string :
            morse += i
            print(morse)
            if morse in char_morse :
                ch = char_text[char_morse.index(morse)]
                if char_text[char_morse.index(morse)] in data :
                    print(data[char_text[char_morse.index(morse)]])
                else :
                    print('char not in data{}')
                ## ch.append(char_text[char_morse.index(morse)])                print(ch)
                data[ch] = {}
            morseTochar(morse_string[len(morse):],data);
        return data

if len(sys.argv) > 1  :
    code = sys.argv[1].split(" ")
data = morseTochar(code);
print('first char is => ' + str(text))

print(data)
