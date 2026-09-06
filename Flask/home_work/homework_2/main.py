from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, ValidationError


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)


class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=0, le=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Имя должно содержать только буквы")
        return value


    @model_validator(mode="after")
    def validate_employment_age(self):
        if self.is_employed and not 18 <= self.age <= 65:
            raise ValueError(
                "Если пользователь работает, его возраст должен быть от 18 до 65 лет"
            )
        return self


def register_user(json_string):
    try:
        user = User.model_validate_json(json_string)

        print("Регистрация успешна")
        return user.model_dump_json(indent=4)

    except ValidationError as error:
        print("Ошибка валидации")
        print(error)
        return None

json_input = """
{
    "name": "John Doe",
    "age": 70,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}
"""

print(register_user(json_input))
