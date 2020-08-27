def main():
    s = set()
    s.add(1)
    s.add(14)
    s.add(27)
    s.add(14)   #não repete a adição
    
    print(s)

    s.pop()

    print(s)
    print(s.__len__())


main()