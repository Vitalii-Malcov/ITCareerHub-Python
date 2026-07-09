""" 03 Извлечение email-адресов

Реализуйте программу, которая:
- находит в тексте все email-адреса, соответствующие следующим критериям:
    - перед @ допускаются буквы, цифры, точки (.) и подчёркивания (_),
            но не начинается и не заканчивается точкой.
    - после @ следует:
        - домен второго уровня: буквы, цифры, дефисы, точки.
        - затем домен верхнего уровня (например, .com, .org, .net, .pl), от 2 до 3 букв.
    - email не может содержать пробелы.

Данные:
text = '''
Valid:
- support@mail.com
- info@company.org
- personal_email123@edu.university.net
- user.name@sub.domain.com
- contact_us123@my-site.org
- hello.world@some.place.travel
- admin@server.local
- support@company-name.de
- user@data.edu.pl

Invalid:
- .support@mail.com
- support.@mail.com
- user@domain,com
- name@domaincom
- name@domain.c
- user@domain.toolongtldddddd
- no@space .com
- bad@@mail.com
- missing@dotcom
'''

Пример вывода:
support@mail.com
info@company.org
personal_email123@edu.university.net
user.name@sub.domain.com
contact_us123@my-site.org
support@company-name.de
user@data.edu.pl

"""
import re
import string

text = """
Valid:
- support@mail.com
- info@company.org
- personal_email123@edu.university.net
- user.name@sub.domain.com
- contact_us123@my-site.org
- support@company-name.de
- user@data.edu.pl

Invalid:
- .support@mail.com
- support.@mail.com
- user@domain,com
- name@domaincom
- name@domain.c
- user@domain.toolongtldddddd
- hello.world@some.place.travel
- no@space .com
- bad@@mail.com
- missing@dotcom
"""

# Собираем regex по частям, чтобы было понятнее:
#
# (?<![\w.])                      - слева не должно быть буквы/цифры/подчёркивания/точки
#                                   (иначе "мы бы влезли" в середину невалидного email,
#                                    например ".support@mail.com")
# [A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*
#                                 - локальная часть (до @): буквы, цифры, "_",
#                                   точки разрешены только МЕЖДУ символами,
#                                   поэтому email не может начинаться/заканчиваться точкой
# @                               - обязательный символ @
# [A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*
#                                 - домен второго уровня (и возможные поддомены):
#                                   буквы, цифры, дефисы, точки
# \.[A-Za-z]{2,3}                - домен верхнего уровня: точка + от 2 до 3 букв
# (?![\w.])                      - справа не должно быть буквы/цифры/"_"/точки
#                                   (иначе TLD длиннее 3 букв тоже бы "подошёл")
pattern = r'(?<![\w.])[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,3}(?![\w.])'

emails = re.findall(pattern, text)

for email in emails:
    print(email)


#///////////////////////////////////////////////////////

def is_valid_local_part(local):
    if not local or local[0] == "." or local[-1] == ".":
        return False
    allowed = set(string.ascii_letters + string.digits + "._")
    return all(ch in allowed for ch in local)

def is_valid_domain(domain):
    if "." not in domain:
        return False
    second_level, _, tld = domain.rpartition(".")
    return second_level and 2 <= len(tld) <= 3 and tld.isalpha() and \
        all(ch in set(string.ascii_letters + string.digits + "-.") for ch in second_level)

def is_valid_email(candidate):
    if candidate.count("@") != 1:
        return False
    local, domain = candidate.split("@")
    return is_valid_local_part(local) and is_valid_domain(domain)

emails = [word for word in text.split() if is_valid_email(word)]
print()
print("\n".join(emails))
