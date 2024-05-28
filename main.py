from encoding import *
from text import *
from decoding import *

def test_encoding_decoding():
    # Przykładowe dane źródłowe
    text = "Witam Teleinfe"
    # Kodowanie textu
    binary_data = text_to_binary(text)
    N = len(binary_data)
    encoded_symbols = encode(binary_data, N)
    print(encoded_symbols)
    # Dekodowanie zakodowanych symboli
    decoded_data = decode(encoded_symbols, N)
    decoded_text = binary_to_text(decoded_data)
    print("Odtworzone dane:", decoded_text)

    assert text==decoded_text

# Testowanie
test_encoding_decoding()
