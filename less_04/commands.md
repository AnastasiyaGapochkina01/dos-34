# Сеть
## ifupdown
устанавливаем пакеты
```bash
sudo apt update
sudo apt install ifupdown net-tools resolvconf -y
```
редактируем параметр grub в `/etc/default/grub`:
```ini
GRUB_CMDLINE_LINUX=" netcfg/do_not_use_netplan=true "
```
обновляем
```bash
sudo update-grub
```
смотрим названия интерфейсов
```bash
ip link show
ip -4 -o a
```
пишем файл с настройками `/etc/network/interfaces`
```
auto lo
iface lo inet loopback

auto enp0s8
iface enp0s8 inet dhcp

auto enp0s9
iface enp0s9 inet static
address 172.16.1.10
netmask 255.255.255.0
dns-nameservers 8.8.8.8 8.8.4.4
```
ребутаем машину и удаляем netplan
```bash
apt-get --assume-yes purge netplan.io
rm -rf /etc/netplan/
```
## netplan
смотрим интерфейсы
```bash
sudo netplan status -a
```
редактируем файл с настройками сети `/etc/netplan/50-cloud-init.yaml`
```yaml
network:
  version: 2
  ethernets:
    enp0s8:
      dhcp4: true
    enp0s9:
      addresses:
        - 172.16.1.10/24
      nameservers:
        addresses:
          - 1.1.1.1
          - 8.8.8.8
```
применяем и проверяем
```bash
sudo netplan try
sudo netplan status -a
ip link show
ip -4 -o a
```
собираем bridge
```yaml
network:
  version: 2
  ethernets:
    enp0s8:
      dhcp4: no
    enp0s9:
      dhcp4: no
  bridges:
    br0:
      interfaces: [enp0s8, enp0s9]
      dhcp4: true
```
```bash
sudo apt install bridge-utils
sudo netplan apply
ip link show
brctl show
```

# Пользователи и права доступа
## пользователи и группы
```bash
# содание пользователя
sudo useradd alice
sudo useradd -m -s /bin/bash tom
sudo adduser bob

# изменение пользователя
# переименование tom -> jerry
sudo usermod -l tom jerry
# изменение shell
sudo usermod -s /bin/sh jerry

# создание группы
sudo groupadd developers
# добавляем существующего пользователя в группу
sudo usermod -aG developers bob
```
## права доступа
```bash
# создаем директорию и файлы для примера
mkdir -p permissions/docs
touch permissions/{app,readme.md}
touch permissions/docs/{report_01.txt,report_02.txt}
# устанавливаем пакет tree
sudo apt install -y tree
# смотрим структуру
tree permissions
# смотрим права
ls -l permissions
```
## владение файлами
```bash
# меняем владельцев/группы
sudo chown alice permissions/app
ls -l permissions
sudo chgrp developers permissions/app
ls -l permissions
sudo chown bob:alice permissions/app
ls -l permissions
# рекурсивно на всю директорию
sudo chown -R bob:developers permissions/docs
ls -l permissions/docs
```
## режим доступа
```bash
chmod 775 permissions/readme.md
ls -l permissions
chmod u-x permissions/readme.md
chmod o+x permissions/readme.md
ls -l permissions
```