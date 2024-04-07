# blockchain_lab

Результат виконання программи:

![2024-04-07 (1)](https://github.com/OleksandrSelehei/blockchain_lab/assets/131198576/70d2ac4e-115a-466f-9bdb-2490c87ca6dc)

для використання программи не потрібні сторонні бібліотеки.

Для запуску потрібен Python:

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

ця змінна byte дається на вхід скрипту, тому щоб змінити взідні дані потрібно замінити дані в змінній

byte = <ващі дані(8-біт)>
