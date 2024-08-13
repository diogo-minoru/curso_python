def from_base10(n, b):
    if b < 2:
        raise ValueError("Base deve ser maior que 2.")
    if n < 0:
        raise ValueError("Valor deve ser maior que 0.")
    if n == 0:
        return [0]
    
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return print(digits)


def encode(digits, digit_map):
    if max(digits) > len(digit_map):
        raise ValueError("Não é possível representar o valor utilizando o mapeamento atual.")
    return ''.join(digit_map[d] for d in digits)

print(encode([15,15], "0123456789ABCDEF"))

