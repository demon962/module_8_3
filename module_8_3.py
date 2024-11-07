class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        # Проверка корректности VIN и номеров машины
        if not self.__is_valid_vin(self.__vin):
            raise IncorrectVinNumber("Неверный диапазон для vin номера.")

        if not self.__is_valid_numbers(self.__numbers):
            raise IncorrectCarNumbers("Неверная длина номера.")

        print(f"{self.model} успешно создан")

    def __is_valid_vin(self, vin_number):
        # Пример валидации VIN: должно быть целым числом в определенном диапазоне (например, 10000000000000000 до 99999999999999999)
        if isinstance(vin_number, int) and 10000000000000000 <= vin_number <= 99999999999999999:
            return True
        return False

    def __is_valid_numbers(self, numbers):
        # Пример валидации: номера автомобиля должны быть строкой длиной от 1 до 10 символов
        if isinstance(numbers, str) and 1 <= len(numbers) <= 10:
            return True
        return False


# Примеры использования
try:
    my_car1 = Car("Model1", 12345678901234567, "ABC123")
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as e:
    print(e.message)

try:
    my_car2 = Car("Model2", 123, "A")  # Неверный VIN
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as e:
    print(e.message)

try:
    my_car3 = Car("Model3", 12345678901234567, "")  # Неверные номера
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as e:
    print(e.message)
