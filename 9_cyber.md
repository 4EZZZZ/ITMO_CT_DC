# Условие задания:
Безопасность и криптография

В этом задании необходимо выполнить шесть заданий из семи. Если сделаете все, то вы получите два бонусных балла.

## Задание hash:

Найдите хеш SHA384 строки Reason always inside level north term security

## Задание encoding:

В результате нескольких последовательных кодирований алгоритмами base64 и base32 получилась следующая строка:
...

В качестве ответа введите исходную строку.

## Задание ssl:

Укажите серийный номер TLS-сертификата для сайта ... Ответом является HEX-строка.

## Задание rsa1:

Познакомьтесь с алгоритмом RSA. Наш приватный ключ — n = 1004214256301, d = 295356544733, зашифрованное сообщение — 167259477336. Расшифруйте сообщение и введите число в качестве ответа.

## Задание rsa2:

Мы зашифровали сообщение алгоритмом RSA с использованием паддинга PKCS#1 OAEP (RSAES-OAEP). Расшифруйте его.
Сообщение:
...
Приватный ключ:
...

## Задание ssh:

В этом задании вы научитесь использовать SSH-ключи для подключения к удалённым серверам — это гораздо более безопасный способ, чем вход по паролю. После выполнения этого задания не забудьте применить знания на практике: добавьте ваш ключ на GitHub и начните работать с ним по SSH.

Сгенерируйте пару SSH-ключей. Вставьте сюда ваш публичный ключ:

Публичный ключ:

Подключитесь с использованием этой пары ключей к серверу по адресу ___ с именем пользователя ___ и получите ответ.

Обратите внимание: вход должен быть произведён по ключу: SSH-клиент должен спросить у вас только пароль от SSH-ключа, если вы его задали. Пароль от сервера вводить не нужно. Если вы получаете приглашение ввести пароль вида 408459@ctddev.ifmo.ru's password:, то вы подключаетесь неправильно.

## Задание pgp:

Напишите нам письмо на ___ — но не простое, а зашифрованное.

Вставьте зашифрованный текст письма (он должен начинаться строкой -----BEGIN PGP MESSAGE----- и заканчиваться -----END PGP MESSAGE-----) прямо в тело сообщения.

Если у вас в GnuPG вместо зашифрованного сообщения получаются нечитаемые символы, попробуйте использовать флаг --armor.
Публичный ключ:

Чтобы задание зачлось, в вашем зашифрованном письме (не в теме) должна быть строка ___.
