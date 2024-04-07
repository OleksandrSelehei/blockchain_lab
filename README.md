# blockchain_lab

Результат виконання программи:

![image](https://github.com/OleksandrSelehei/blockchain_lab/assets/131198576/af91c029-bd9a-4848-93df-f6842d720585)

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
