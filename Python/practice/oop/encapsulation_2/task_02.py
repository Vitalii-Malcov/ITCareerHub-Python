""" 02 Смена кода

Доработайте класс Door:
- добавьте метод для смены кода change_code(), где:
    - новый код можно установить только после проверки текущего кода.
    - логика проверки корректности кода должна не должна дублироваться.
"""

class Door:
    def __init__(self, code):
        self.code = code

    def __is_valid_code(self, code):
        return code == self.code

    def unlock(self, code):
        if self.__is_valid_code(code):
            print("Access granted.")
            return True
        else:
            print("Access denied.")
            return False

    def change_code(self, code, new_code):
        if self.__is_valid_code(code):
            self.code = new_code
            print("Code changed.")
        else:
            print("Access denied. Code not changed.")
            return False



if __name__ == "__main__":
    d = Door("1234")
    d.change_code("0000", "9999")
    d.unlock("1234")
    d.change_code("1234", "9999")
    d.unlock("1234")
    d.unlock("9999")

    # Access denied. Code not changed.
    # Access granted.
    # Code changed.
    # Access denied.
    # Access granted.
