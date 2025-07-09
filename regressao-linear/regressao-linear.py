import matplotlib.pyplot as plt

def calcular_a(x, y):
    n = len(x)
    if n == 0:
        return 0
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x_squared = sum(xi ** 2 for xi in x)
    
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    return a

def calcular_b(x, y):
    n = len(x)
    if n == 0:
        return 0
    sum_x = sum(x)
    sum_y = sum(y)
    
    a = calcular_a(x, y)
    b = (sum_y - a * sum_x) / n
    return b

def calcular_regressao_linear(x, y):
    a = calcular_a(x, y)
    b = calcular_b(x, y)
    return a, b

def plotar_grafico(x, y, a, b):
    plt.scatter(x, y, color='blue', label='Dados')
    
    x_line = [min(x), max(x)]
    y_line = [a * xi + b for xi in x_line]
    
    plt.plot(x_line, y_line, color='red', label='Linha de Regressão')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regressão Linear')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    a, b = calcular_regressao_linear(x, y)
    
    print(f"Coeficiente angular (a): {a}")
    print(f"Coeficiente linear (b): {b}")

    plotar_grafico(x, y, a, b)

main()