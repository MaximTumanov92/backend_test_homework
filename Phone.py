# Родительский класс.
class Phone:

    # Атрибут базового класса.
    line_type = 'проводной'

    # Инициализатор базового класса.
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    # Метод базового класса.
    def ring(self):
        print('Дзззззыыыыыыыынь!')

    # Ещё один метод базового класса.
    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


# Дочерний класс, унаследованный от класса Phone.
class MobilePhone(Phone):
    pass 