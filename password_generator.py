import random
import string
total = string.ascii_letters + string.digits + string.punctuation
length = input('Введите необходимое количество символов пароля:')
try:
    password = "".join(random.sample(total, int(length)))
    print(password)
except:
    print('Количество символов должно быть целым положительным числом!')
