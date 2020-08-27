import random, string

def main():
    print(random.random())
    print(random.randint(100, 200))

    x = ['gol', 'fusca', 'astra', 'verona', 'prisma', 'focus']
    print(random.choice(x))

    random.shuffle(x)
    print(x)

    teste = 'teste'
    #teste = string.punctuation
    print(teste)

main()