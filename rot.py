#!/usr/bin/python
import sys
char = ['a','b','c','d','e',
	'f','g','h','i','j',
	'k','l','m','n','o',
        'p','q','r','s','t',
	'u','v','w','x','y','z'];

def DecodeROT(n,code):
    text = ''
    n = int(n)   ## sys.argv[2] is type of <str>
    if n > 26 : n = n % 26
    for i in code :
        if i == ' ' :
            text += ' '
        elif char.index(i) >= 0 :
            charIndex = char.index(i) + n
            if charIndex > 25 : charIndex = charIndex % 25 -1
            text += char[charIndex]
        else :
            text += i
    return text

def EncodeROT(n,text):
    code = ''
    n = int(n)   ## sys.argv[2] is type of <str>
    if n > 26 : n = n % 26
    for i in text :
        if i == ' ' :
            code += ' '
        elif char.index(i) >= 0 :
            charIndex = char.index(i) - n
            if charIndex > 25 : charIndex = charIndex % 25 - 1
            code += char[charIndex]
        else :
            code += i
    return code

if len(sys.argv) > 1  :
    if sys.argv[1] == '-e' :
        code = EncodeROT(sys.argv[2],sys.argv[3])
        print('Encode ROT' + sys.argv[2] + ' => ' + code)
    elif sys.argv[1] == '-d' :
        text = DecodeROT(sys.argv[2],sys.argv[3])
        print('Decode ROT' + sys.argv[2] + ' => ' + text)
    else :
        print("rot  <option>  <number>  'Message'")
        print('<option>   -e  Encrypt Massage to Code')
        print('<option>   -d  Decrypt Code to Message')
        print('<number>   ( 1 - 25 ) ROT1 - ROT25')
        print("'Message'  Type your massage to Encrypt or Decrypt")
else :
        print('rot <option> <number> "Message" ')
        print('<option>   -e  Encrypt Massage to Code')
        print("<option>   -d  Decrypt Code to 'Message'")
        print('<number>   ( 1 - 25 ) ROT1 - ROT25')
        print("'Message'  Type your massage to Encrypt or Decrypt")
