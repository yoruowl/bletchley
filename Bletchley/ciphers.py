"""
This file provides the backend of ciphers. 

Cases are preserved where possible


"""

import random
import string
import os
from faker import Faker
import re 
import json

global lower_alphabet
global upper_alphabet
global alphabet
global punctuation
global numbers

lower_alphabet="abcdefghijklmnopqrstuvwxyz"
upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet=lower_alphabet+upper_alphabet
punctuation=".,></;:'[]!@#$%^&*()—-_=+`~|\"\\"
numbers="1234567890"

faker = Faker()

class realEngine:
    def __init__(self, corpus="small_specialized"):

        if corpus=="large":
            f = open("wordlists/words_dictionary.json", "r")
            self.data = json.load(f)
            f.close()
        elif corpus=="small":
            with open("wordlists/words.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="small_specialized":
            with open("wordlists/words_specialized.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="large_specialized":
            with open("wordlists/words_dictionary_specialized.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="dictionary":
            with open("wordlists/dictionary.txt") as f:
                self.data = f.read().splitlines() 
            f.close()

        self.corpus=corpus

    def is_this_real(self, word):
        word=word.lower()

        if word in self.data:
            return True
        else:
            return False

def ceaser(text, increment):
    # Increments the text based on the increment
    # Leaves spaces, punctuation, and numbers alone. Breaks with special characters

    global punctuation
    global lower_alphabet
    global upper_alphabet
    global alphabet
    global numbers

    encrypted=""

    for i in text:
        if i in punctuation:
            encrypted+=i
            continue
        elif i in numbers:
            encrypted+=i
            continue
        elif i == " ":
            encrypted+=i
            continue
        elif i in upper_alphabet:
            letter_index=upper_alphabet.index(i)+increment
            letter_index=letter_index%26
            encrypted+=upper_alphabet[letter_index]

        elif i in lower_alphabet:
            letter_index=lower_alphabet.index(i)+increment
            letter_index=letter_index%26
            encrypted+=lower_alphabet[letter_index]
    return(encrypted)


def password():
    password=""
    while len(password)<9:
        password=faker.word()
    return((password).lower())

def randome(length):
    lowercase_letters = string.ascii_lowercase
    random_sentence = ''.join(random.choices(lowercase_letters, k=length))
    return random_sentence

def randomText():
    length=random.randint(1,50)
    return(randome(length))

def vigenere_backend(text):
    text=''.join(e for e in text if e.isalnum())
    text=text.replace("ù", "u").replace("é", "e").replace("æ", "ae").replace("ê", "e").replace("è", "e").replace("ç", "c").replace("ô", "o")
    text=re.sub(r'\d+', '', text)
    text=text.lower()


    passw=password()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encrypted=""
    passIndex=0

    for i in text:
        value = alphabet.index(i)
        value = (value+alphabet.index(passw[passIndex]))%26
        encrypted+=alphabet[value]
        if passIndex==len(passw)-1:
            passIndex=0
        else:
            passIndex+=1

    return(encrypted)

def vigenere():
    f=open("quotes.csv", "r")
    quotes=f.readlines()
    for i in quotes:
        print(vigenere_backend(i))
    f.close()

def randomSentence():
    book=random.choice(os.listdir('texts'))
    with open("texts/"+book) as f:
        lines = f.readlines()
    return(random.choice(lines))

def ciphertext():
    line=""
    while line=="" or line=="\n" or line==" " or len(line)<5:
        line=randomSentence()
    return vigenere(line)

def randomData():
    ciph=ciphertext()
    length=len(ciph)
    return(ciph, randome(length))
