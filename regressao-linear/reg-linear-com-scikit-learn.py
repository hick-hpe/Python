import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Converter x para formato de matriz (n, 1) exigido pelo scikit-learn
x_np = np.array(x).reshape(-1, 1)
y_np = np.array(y)

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(x_np, y_np)

# Obter coeficientes
a = modelo.coef_[0]   # inclinação
b = modelo.intercept_ # intercepto

print(f"Coeficiente angular (a): {a}")
print(f"Coeficiente linear (b): {b}")

# Prever valores
y_pred = modelo.predict(x_np)

# Plotar
plt.scatter(x, y, color='blue', label='Dados reais')
plt.plot(x, y_pred, color='red', label='Regressão Linear')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear com scikit-learn')
plt.legend()
plt.grid()
plt.show()
