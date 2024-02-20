import numpy as np


def uzitocnost(data):
    """
  Táto funkcia vypočíta užitočnosť daných dát.
  Argumenty:
      data: Dvojrozmerné pole obsahujúce dáta.
  Vracia:
      Užitočnosť dát.
  """
    # Vypočíta priemer a smerodajnú odchýlku dát.
    average = np.mean(data)
    stddev = np.std(data)

    # Vypočíta užitočnosť dát ako pomer priemeru a smerodajnej odchýlky.
    usitocnost = average / stddev

    return usitocnost


data = np.array([1, 2, 3, 4])


uzitocnost1 = uzitocnost(data)

print(f"Užitočnosť dát: {uzitocnost}")
