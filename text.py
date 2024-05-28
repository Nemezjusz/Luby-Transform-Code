def text_to_binary(text):
    """
    Konwertuje tekst na listę wartości binarnych.
    """
    return [ord(char) for char in text]

def binary_to_text(binary_data):
    """
    Konwertuje listę wartości binarnych na tekst.
    """
    return ''.join(chr(num) for num in binary_data)
