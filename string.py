import string

def main():
    print(dir(string))
    #print('================')
    #teste = 'teste'
    #print(dir(teste))
    #print('================')
    teste = string.punctuation
    print(teste)
    #print(teste.capitalize())
    #print(teste.cap())
    s = 'The waxwork man'

    print(s[::-1])

    print(s[:7])

    print(s[-3:])

    print(s[4:11])


main()