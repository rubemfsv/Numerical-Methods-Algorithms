import math


# Equação dada na questão
def Equation(x, Re):
    y = (1 / math.sqrt(x)) - (4 * math.log10(Re * x)) + 0.4
    return y


# Aplicação da bisecção para descobrir o resultado
def Bisect(Re):
    xl = 0.001  # Limite inferior do fator de atrito de Fanning, substituindo xl por 0.00001 e xu por 1, consegue que a função resolva problemas com uma gama mais ampla de Re
    xu = 0.01  # Limite superior do fator de atrito de Fanning
    xr = 0
    fl = Equation(xl, Re)  # Chama a equação a cima
    i = 0  # Numero de iterações
    print("  i     xl         xu         xr         ea         f(xr)\n")
    while (1):
        i = i + 1  # Aumenta a iteração
        xrold = xr  # Guarda o valor antigo de xr para utilizar posteriormente
        xr = (xl + xu) / 2  # Valor novo de xr
        fr = Equation(xr, Re)  # Chama a equação a cima para os valores dados
        if (xr != 0):  # Condição para verificar se xr é diferente de 0
            ea = abs((xr - xrold) / xr)  # Calculo do erro
        print(i, xl, xu, xr, ea, fr)  # Exibe os valores da iteração
        test = fl * fr  # Guarda o resultado da multiplicação de fl por fr
        if (
                test < 0
        ):  # Condicionais para mudar os valores das variáveis para a próxima iteração
            xu = xr
        else:
            if (test > 0):
                xl = xr
                fl = fr
            else:
                ea = 0

        if (ea < 0.000005):  # Condição de parada das iterações
            break


# Substituir o valor entre parenteses para testar outros valores, estou testando a função para 30000
Bisect(30000)