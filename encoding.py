import random
import numpy as np

def soliton_distribution(N):
    """
    Generuje rozkład Solitona dla kodu LT.
    Rozkład Solitona jest używany do wybierania stopnia (d) zakodowanego symbolu.
    """
    p = [0] * N
    p[0] = 1 / N
    for i in range(2, N + 1):
        p[i - 1] = 1 / (i * (i - 1))
    # Normalizacja rozkładu
    total = sum(p)
    p = [x / total for x in p]
    return p

def generate_encoded_symbol(data, p):
    """
    Generuje jeden zakodowany symbol na podstawie danych źródłowych i rozkładu prawdopodobieństwa.
    """
    N = len(data)
    d = np.random.choice(range(1, N + 1), p=p)  # Wybierz stopień d
    chosen_indices = random.sample(range(N), d)  # Wybierz d indeksów
    encoded_symbol = 0
    for index in chosen_indices:
        encoded_symbol ^= data[index]  # Wykonaj XOR wybranych symboli źródłowych
    return encoded_symbol, chosen_indices

def encode(binary_data, N):

    p = soliton_distribution(N)  # Generowanie rozkładu Solitona

    # Automatyczne dobieranie liczby zakodowanych symboli (np. 1.5 razy więcej niż długość wiadomości)
    num_encoded_symbols = int(2.5 * N)

    # Generowanie zakodowanych symboli
    encoded_symbols = []
    for _ in range(num_encoded_symbols):
        encoded_symbol, indices = generate_encoded_symbol(binary_data, p)
        encoded_symbols.append((encoded_symbol, indices))

    return encoded_symbols