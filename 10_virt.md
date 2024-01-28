Условие задания находится в конце файла

# Ход решения:

Создаём свой репозиторий и помещаем на него файлы server и client

Качаем Ubuntu 22.04.03 и выше. Более старые версии не поддерживают распаковку qcow2

Открываем CMD
wsl --update
wsl --shutdown
Закрываем CMD

Открываем Ubuntu(Окно 1)
Открываем Ubuntu(Окно 2)
Открываем Ubuntu(Окно 3)

# Окно 1:
sudo apt update
sudo apt upgrade

sudo apt install qemu
sudo apt install qemu-kvm
sudo apt install qemu-system-common
sudo apt install qemu-system-ppc64
sudo apt install qemu-system-s390x
sudo apt install qemu-kvm libvirt-daemon-system
sudo apt install libvirt-daemon
sudo apt install bridge-utils

Наводим на ссылку для скачаивания файлов с архитектурами и нажимаем "Copy Link" и помещаем её ниже на место ссылки с моего времени:

wget https://storage.yandexcloud.net/ct-itmo-intro-public/virt/alpine-ppc64le.qcow2
wget https://storage.yandexcloud.net/ct-itmo-intro-public/virt/alpine-s390x.qcow2

sudo sysctl net.ipv4.ip_forward=1
sudo sysctl net.bridge.bridge-nf-call-iptables=1
sudo sysctl net.bridge.bridge-nf-call-ip6tables=1

sudo systemctl enable libvirtd.service
sudo systemctl start libvirtd.service

sudo virsh net-autostart --network default
sudo virsh net-start --network default

sudo mkdir /etc/qemu
cd /etc/qemu
sudo touch bridge.conf
sudo nano bridge.conf
allow virbr0
^O + Enter + ^X

sudo chown root:root /etc/qemu/bridge.conf
sudo chmod 0640 /etc/qemu/bridge.conf
sudo chmod u+s /usr/lib/qemu/qemu-bridge-helper

# Окно 2:
mac_ppc64=$(printf '52:54:00:%02x:%02x:%02x\n' $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)))

Команда для запуска контейнера с клиентом (ppc64le):

sudo qemu-system-ppc64 -nographic -netdev bridge,id=hn0,br=virbr0 -device virtio-net-pci,netdev=hn0,id=nic1,mac=$mac_ppc64 -drive file=alpine-ppc64le.qcow2

Логин: root, пароль пустой
apk add git
git clone https://github.com/4EZZZZ/files
cd files
rm server
mv client /root/
cd /root/
rm -fr files
touch token
echo 'Токен с сайта ЦК' > token
cat token | base64 -d > decoded
chmod 777 client
chmod 777 decoded

# Окно 3:
mac_s390x=$(printf '52:54:00:%02x:%02x:%02x\n' $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)))

Команда для запуска контейнера с сервером (s390x):

sudo qemu-system-s390x -nographic -netdev bridge,id=hn0,br=virbr0 -device virtio-net-pci,netdev=hn0,id=nic1,mac=$mac_s390x -drive file=alpine-s390x.qcow2

Логин: root, пароль пустой
apk add git
git clone https://github.com/4EZZZZ/files
cd files
rm client
mv server /root/
cd /root/
rm -fr files
chmod 777 server
ifconfig
С eth0 копируем ip-адрес со второй строки с inet addr
./server

# Окно 2:
./client 'inet addr' decoded

Копируем ключ и вставляем на сайт ЦК, вместе с собранными командами

# Условие задания:

Виртуализация

В этом задании вы познакомитесь с эмулятором QEMU, в частности с его режимом полной эмуляции системы (System Emulation mode).

Легенда: на одном предприятии было установлено несколько очень дорогих мейнфреймов, на которых работала критически важная система аттестации токенов. К превеликому сожалению, они вышли из строя (внезапно, оба, сразу). Пока мейнфреймы находятся в ремонте, вам срочно нужно обработать один важный токен. Как часто бывает в подобной ситуации, у вас есть только бинарные файлы программ, без исходных кодов, потому что их написал какой-то фрилансер 15 лет назад. Единственным возможным решением в данной ситуации является эмуляция мейнфреймов на вашем личном компьютере.

Даны следующие файлы:

    server — Программа-сервер, обрабатывающая токены.
    client — Программа-клиент, которая отправляет токен на сервер.
    alpine-ppc64le.qcow2 — образ с установленной Alpine Linux для архитектуры PowerPC (64-bit, little-endian)
    alpine-s390x.qcow2 — образ с установленной Alpine Linux для архитектуры z/Architecture

Необходимо запустить оба образа при помощи QEMU и установить между ними виртуальный network bridge. Затем запустите в них пару сервер-клиент, передав клиенту ваш уникальный токен. Клиент запишет бинарный файл, который необходимо закодировать base64 и отправить в форму на этой странице.

Подсказки:

    Поскольку ваш процессор почти наверняка не поддерживает аппаратную виртуализацию используемых архитектур, а QEMU не производит JIT-компиляцию машинного кода, то производительность эмулируемой системы будет достаточно низкая. По этой причине guest OS может загружаться долго, наберитесь терпения.
    Используйте флаг -nographic, чтобы напрямую соединить ваш терминал с эмулируемой машиной. Графическая оболочка не установлена, поэтому эмуляция VGA будет только мешать.
    Логин: root, пароль пустой.
    Доставить исполняемые файлы в guest OS можно любым удобным вам способом.
    Чтобы определить архитектуру, под которую собран исполняемый файл, можно использовать уже известные вам shell-команды.
    Чтобы протестировать работу network bridge, можно использовать команду ping. Это может быть удобно для поиска проблем с конфигурацией: например, когда из-за проблем с файерволлом guest OS по мосту могут общаться с host OS, а друг с другом — нет.
        Если вы используете Linux и ничего не работает, вы можете быть заинтересованы в sysctl-переменной net.bridge.bridge-nf-call-iptables.

Ваш токен в формате base64: ...
