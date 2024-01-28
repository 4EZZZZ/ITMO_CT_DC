# Task 1(hash)
import hashlib
line = "___"
hashed = hashlib.sha224(line.encode('utf-8')).hexdigest()
print(hashed)

# Task 2(encoding)
import base64
encoded = "___"
while True:
    try:
        decoded = base64.b64decode(encoded).decode('utf-8')
        encoded = decoded
    except:
        try:
            decoded = base64.b32decode(encoded).decode('utf-8')
            encoded = decoded
        except:
            break
print(decoded)

# Task 3(ssl)
# pip install cryptography (cmd от имени админа)
import ssl
import socket
from cryptography import x509
from cryptography.hazmat.backends import default_backend
context = ssl.create_default_context()
with socket.create_connection(('___', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='___') as ssock:
        der_cert = ssock.getpeercert(binary_form=True)
certificate = x509.load_der_x509_certificate(der_cert, default_backend())
serial_number = certificate.serial_number
preans = hex(serial_number)[:1] + hex(serial_number)[2:].upper()
ans = ":".join([preans[i:i+2] for i in range(0, len(preans), 2)])
print(ans)

# Task 4(rsa1)
c = ___
d = ___
n = ___
m = 1
c = c % n
while d > 0:
    if d % 2 == 1:
        m = (m * c) % n
    c = (c * c) % n
    d = d // 2
print(m)

# Task 5(rsa2)
# pip install pycryptodome (cmd от имени админа)
# pip install rsa (cmd от имени админа)
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64
ciphertext = b'___'
decoded_ciphertext = base64.b64decode(ciphertext)
private_key = '''___'''
key = RSA.importKey(private_key)
cipher = PKCS1_OAEP.new(key)
message = cipher.decrypt(decoded_ciphertext)
print(message.decode("utf-8"))

# Task 6(ssh)
# Переходим по ссылке ниже и качаем под свою ОС
# https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
# Выключаем брандмауэр
# Переходим в папку PuTTY и запускаем puttygen.exe
# Нажимаем Generate и пока это происходит, двигаем произвольно мышкой по интерфейсу приложения и нажимаем рандомные кнопки на клавиатуре
# Из поля Public key... полностью копируем ключ и добавляем его на сайт ЦК, нажимаем отправить
# Нажимаем Save private key
# Запускаем PuTTY Configurator
# В поле Host Name ctddev.ifmo.ru
# В поле Port данный в заданиии порт
# В поле Saved Sessions любое имя
# Нажимаем Save
# В левой части приложения находится поле Category
# При неоходимости нажимаем на плюсики и переходим на Connection/SSH/Auth/Credentials
# В поле Private key file... нажимаем Browse и выбираем скачанный ключ
# Возвращаемся в Session и нажимаем Save
# При желании можно проверить настройку, нажав на Default Settings Load и проверив отсутствие ключа в Credentials
# В Session выбираем нашу сессию, нажимаем Load
# Нажимаем Open
# Вводим выданное имя пользователя
# Радуемся

# Task 7(pgp)
# Устанавливаем GnuPG
# В любой папке создаём файлы для ключа(.asc) и сообщения(.txt) (Например, key.asc, message.txt)
# Вставляем в эти файлы содержимое с сайта
# Открываем cmd
# cd 'Директория с ключом и сообщением'
# gpg --import '___.asc'(любое имя для ключа)
# gpg --list-keys (Берём почту)
# gpg --encrypt --armor --recipient ___ '___.txt' (любое имя для сообщения)
# y
# Файл с расширением .txt.asc открываем для просмотра и копируем содержимое полностью
# Открываем свою почту
# Пишем письмо на ___@i.nsychev.ru
# В тексте сообщения вставляем скопированное содержимое
# Отправляем
