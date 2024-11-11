import re
import string
import random

# проверка на наличие спец символов в пароле
def check_pass(password):
    return bool(re.search(r'[!@#$%^&*()_+{}|:"<>?]', password))

# генерация паролей
def gen_passwd(count):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(string.ascii_uppercase) +
                       random.choice(string.ascii_lowercase) +
                       random.choice(string.digits) +
                       random.choice(string.punctuation) +
                       random.choice(all_characters)
                       for _ in range(count // 5))
    while len(password) < 12:
        password += random.choice(all_characters)
    password = ''.join(random.sample(password, len(password)))
    
    return password