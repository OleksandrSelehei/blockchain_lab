# S-таблиця
s_table = [
    0x1, 0x0, 0x3, 0x2, 0x4, 0x6, 0x7, 0x5,
    0x9, 0x8, 0xb, 0xa, 0xc, 0xe, 0xf, 0xd,
]

# Зворотня S-таблиця
s_table_inv = [
    0xe, 0x3, 0x9, 0x8, 0x1, 0x0, 0x4, 0x6,
    0xf, 0xd, 0x2, 0xb, 0x7, 0x5, 0xa, 0xc,
]

# P-таблиця
p_table = [
    0, 1, 2, 3, 4, 5, 6, 7,
    4, 5, 6, 7, 0, 1, 2, 3,
    1, 0, 3, 2, 5, 4, 7, 6,
    6, 7, 4, 5, 2, 3, 0, 1,
]

# Зворотня P-таблиця
p_table_inv = [
    0, 4, 1, 5, 2, 6, 3, 7,
    7, 3, 6, 2, 5, 1, 4, 0,
    3, 2, 7, 6, 0, 4, 1, 5,
    5, 1, 4, 0, 7, 6, 2, 3,
]


def s_box(byte):
    """Функція S-перетворення"""

    # Розбиття байта на тетради
    left_nibble = byte >> 4
    right_nibble = byte & 0xF

    # Заміна тетрад за допомогою S-таблиці
    left_nibble = s_table[left_nibble]
    right_nibble = s_table[right_nibble]

    # Об'єднання тетрад
    return (left_nibble << 4) | right_nibble


def s_box_inv(byte):
    """Функція зворотнього S-перетворення"""

    # Розбиття байта на тетради
    left_nibble = byte >> 4
    right_nibble = byte & 0xF
    # Заміна тетрад за допомогою зворотної S-таблиці
    left_nibble = s_table_inv[left_nibble]
    right_nibble = s_table_inv[right_nibble]

    # Об'єднання тетрад
    return (left_nibble << 4) | right_nibble


def p_box(byte):
    """Функція P-перетворення"""

    result = 0
    # ітерація
    for i in range(8):
        # зсув
        result |= ((byte >> (7 - i)) & 0x1) << p_table[i]
    return result


def p_box_inv(byte):
    """Функція зворотного P-перетворення"""

    result = 0
    # ітерація
    for i in range(8):
        # зсув
        result |= ((byte >> (7 - p_table[i])) & 0x1) << i
    return result


def main():
    # Приклад
    byte = 0b01011010
    print(f"Вхід: {byte:08b}")
    byte = s_box(byte)
    print(f"S-перетворення: {byte:08b}")
    byte = p_box(byte)
    print(f"P-перетворення: {byte:08b}")
    byte = p_box_inv(byte)
    print(f"Зворотнє P-перетворення: {byte:08b}")
    byte = s_box_inv(byte)
    print(f"Зворотнє S-перетворення: {byte:08b}")


if __name__ == '__main__':
    main()
