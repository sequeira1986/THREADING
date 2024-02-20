# Import knižníc
import matplotlib.pyplot as plt
import numpy as np

# Definícia funkcie
def f(x):
  return 2 * x**2 - 4 * x + 3

# Vytvorenie grafu
x = np.linspace(-2, 4, 100)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Zobrazenie grafu
plt.show()
