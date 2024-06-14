import numpy as np  # Importa a biblioteca NumPy para operações eficientes com arrays

# Supondo que peso_laranja e diametro_laranja são arrays NumPy definidos anteriormente
# Aqui está um exemplo de definição:
peso_laranja = np.array([150, 160, 170, 180, 190])  # Exemplo de pesos das laranjas em gramas
diametro_laranja = np.array([7.0, 7.5, 8.0, 8.5, 9.0])  # Exemplo de diâmetros das laranjas em centímetros

Y = peso_laranja  # Define Y como o array de pesos das laranjas
X = diametro_laranja  # Define X como o array de diâmetros das laranjas
n = np.size(X)  # Calcula o número de elementos em X (ou Y, já que ambos têm o mesmo tamanho)

# Calcula o coeficiente 'a' (slope) da regressão linear
a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y)) / (n*np.sum(X**2) - np.sum(X)**2)

# Calcula o coeficiente 'b' (intercept) da regressão linear
b = np.mean(Y) - a*np.mean(X)

# Agora 'a' e 'b' representam os coeficientes da linha de regressão: Y = aX + b
print(f"Coeficiente angular (a): {a}")
print(f"Coeficiente linear (b): {b}")


