
import random
import urllib
import urllib.request

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_site)
text = response.read().decode('utf-8')
words_global = text.splitlines()


def split_word(word, length):
    shuffled = ''.join(random.sample(word, len(word)))
    return word[:length], word[length:], word[length::-1], shuffled

def length_to_split(word):
    if len(word) == 4:
        split_size = 2
        return split_size
    elif len(word) < 4:
        split_size = 1
        return split_size
    elif len(word) > 4:
        split_size = random.randint(3, 4)
        return split_size
    
def word_getter():
    while True:
        try:
            word = random.choice(words_global)
            while len(words_global) < 3:
                continue
            else:
                return word
        
        except ValueError as e:
            print(f'Error. {e}')


            
def main():
    word = word_getter()
    length = length_to_split(word)
    word1, word2, word3, word4 = split_word(word, length)
    print(42*'*')
    print('\tWelcom to the word builder game!')
    print(42*'*')
    print(f'\nFrom the words listed, what is a possible word to make?\n>> {word2}\n>> {word3}\n>> {word4}\n>> {word1}')

    while True:
        try:
            answer = input("Enter you answer: ").lower()
            if not answer:
                print(f'\nThe correct answer is {word}')
                choice = input('Continue (y/n)?').lower()
                if choice =='n':
                    break
                if choice =='y':
                    main()
                    break

            if answer != word:
                print(f'{answer} is not correct!. Try again (Press Enter to show answer).')
                continue
            elif answer == word:
                print(f'{answer} is correct!')
                choice = input('Continue (y/n)?').lower()
                if choice =='n':
                    break
                if choice =='y':
                    main()
                    break
        except ValueError as e:
            print(f'Error {e}')

main()