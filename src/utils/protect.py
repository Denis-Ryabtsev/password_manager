import base64
import io
import random
import re
import requests
import string

from captcha.image import ImageCaptcha
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image


# Генерация ключа
def generate_key() -> bytes:
    return get_random_bytes(16)

# Шифрование. ct- ciphertext, iv - initialization vector
def encrypt_create(key: bytes, data: str) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# Шифрование для удаления
def encrypt_delete(key: bytes, data: str, iv: str) -> str:
    iv = base64.b64decode(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return ct

# Расшифровка. pt- plaintext
def decrypt(key: bytes, iv: str, ct: str):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt

# Captcha
def generate_captcha() -> str:
    captcha = ImageCaptcha()
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    captcha_image_bytes = captcha.generate(captcha_text)
    captcha_image = Image.open(io.BytesIO(captcha_image_bytes.getvalue()))
    #captcha_image.show()  # Отображение изображения
    captcha_image.save("captcha.png")
    return captcha_text

# Проверка на сложность пароля
def password_complexity(object: str) -> bool:
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')
    special_regex = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~]')
    if upper_regex.search(object) and lower_regex.search(object) and \
        digit_regex.search(object) and special_regex.search(object):
        return True
    else:
        return False

# Проверка подключения к интернету
def check_internet() -> bool:
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        return False
    
# Генерация кода для подтверждения почты
def generate_code() ->  str:
    digits = ''.join(random.choice(string.digits) for _ in range(2))
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(3))
    code = ''.join(random.sample(digits + letters, k = 5))
    return code