def decode(encoded_symbols, N):
    """
    Dekodowanie zakodowanych symboli, aby odzyskać oryginalne dane źródłowe.

    Args:
    - encoded_symbols: lista zakodowanych symboli wraz z ich indeksami
    - N: liczba symboli źródłowych

    Returns:
    - decoded: lista odzyskanych symboli źródłowych
    """
    decoded = [None] * N  # Inicjalizacja listy do przechowywania odzyskanych symboli
    while any(symbol is None for symbol in decoded):
        for i, (encoded_symbol, indices) in enumerate(encoded_symbols):
            # Jeśli symbol ma stopień 1
            if len(indices) == 1:
                index = indices[0]
                if decoded[index] is None:
                    decoded[index] = encoded_symbol  # Odzyskanie symbolu źródłowego
                    # Aktualizacja pozostałych zakodowanych symboli
                    for j, (es, idxs) in enumerate(encoded_symbols):
                        if j != i and index in idxs:
                            encoded_symbols[j] = (es ^ encoded_symbol, [idx for idx in idxs if idx != index])
    return decoded