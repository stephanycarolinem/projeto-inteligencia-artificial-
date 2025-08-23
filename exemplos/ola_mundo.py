# Primeiro exemplo de IA: prever resultado com base em dados
from sklearn.linear_model import LinearRegression

# Dados simples
x = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]  # saída esperada

modelo = LinearRegression()
modelo.fit(x, y)

print(modelo.predict([[5]]))  # Deve prever algo próximo de 10
