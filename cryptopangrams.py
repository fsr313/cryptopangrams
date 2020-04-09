if __name__=="__main__":
    from math import gcd
    import sys
    import string
    #### TODAS ESTAS LINEAS SON PARA NOMAS AGARRAR LOS DATOS DIRECTAMENTE DE CONSOLA
    T = int(sys.stdin.readline().strip())

    for case in range(T):
        data = list(sys.stdin.readline().strip().split())
        N, L = [int(i) for i in data]
        data = list(sys.stdin.readline().strip().split())
        data = [int(i) for i in data]
    #### TODAS ESTAS LINEAS SON PARA NOMAS AGARRAR LOS DATOS DIRECTAMENTE DE CONSOLA
        text = ['' for i in range(len(data)+1)] # creamos un arreglo donde se guardaran los numeros primos decifrados
        firstSolution = -1
        for i in range(len(data)-1): # la cabeza y la cola son casos especiales
            if data[i]!=data[i+1]: # checar si se puede resolver
                firstSolution = i+1
                text[i+1] = gcd(data[i],data[i+1]) # usando greater common divisor identificamos el numero que divide a ambos
                break
        for i in range(firstSolution,len(data)-1): #frontpropagation
            #print(text[i+1])
            #print(text[i])
            text[i+1] = data[i]//text[i]
        if firstSolution > 1:
                for i in range(firstSolution,1,-1): #backpropagation
                    text[i-1] = data[i-1]//text[i]

        
        
            

            
        text[0] = data[0]//text[1] # resolviendo para la cabeza
        text[-1] = data[-1]//text[-2] # resolviendo para la cola
        primes = list(set(text)) # arreglo con todos los numeros primos decifrados sin repeticion
        primes.sort() # lo acomodamos en orden ascendente
        letras = list(string.ascii_uppercase[0:26]) # alfabeto en mayusculas
        dictletras = dict(zip(primes,letras)) # diccionario relacionando los primos y el alfabeto
        textletters = []
        for prime in text:
            textletters.append(dictletras[prime])
        print('Case #'+str(case+1)+': '+''.join(textletters))
    sys.exit(0)

    #2
    #103 31
    #217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
    #10000 25
    #3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543
