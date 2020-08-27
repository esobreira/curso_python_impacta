def somar(numero1, numero2):
    return(numero1 + numero2)

def subtrair(numero1, numero2):
    return(numero1 - numero2)

def funcao(**kwargs):
    for key, value in kwargs.items():
        #print("%s == %s" %(key, value))
        print("%.2f == %s" %(10.2545345435, value))
        #print("{0} == {1}".format(key, value))

#string.format("{0}, {1}", "eberton", "sobreira")

# x = somar(10, 20)
# print(x)

# y = subtrair(50, 25)
# print(y)

funcao(nome="eberton", sobrenome="sobreira")