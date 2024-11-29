def f(text: str, shift: int):
    result = []

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            result.append(shifted_char)
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(result)
