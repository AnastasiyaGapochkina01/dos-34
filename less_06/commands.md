##### Процессы
1) Вывести дерево каталогов
```bash
pstree -p
ps aufx
```
ключи `ps`
- a - все терминалы
- u - пользовательский формат
- f - в виде дерева
- x - показывает процессы без терминала* (демоны)

2) Вывести список процессов со своим набором параметров
```bash
ps -eo pid,comm,pri,nice,stat
```

3) Запуск процессов с приоритетом
```bash
nice -n -5 make -j$(nproc)
sudo renice -10 -p $pid
```

4) Background и foreground режимы
```bash
# foreground
ping google.com
    Ctrl+Z
# background
ping ya.ru > ping.log 2>&1 &

ps aux
jobs -l
# %1 - номер job`ы
fg %1
```

5) Запуск с отвязкой от сесии (screen)
```bash
screen -S longtask
sleep 1000
Ctrl+A D
ps aux

screen -ls
screen -r longtask
```

##### Сигналы
```bash
# список сигналов
kill -l
```
Игнорирование сигналов
```python
# ign.py
import signal
import time

signal.signal(signal.SIGINT, signal.SIG_IGN)

while True:
    time.sleep(1)
```

```bash
# запускаем в фоне
python3 ign.py > output 2>&1 &
# смотрим, есть ли процес
ps aux | grep [i]gn


kill -INT $pid
ps aux | grep [i]gn
kill $pid
ps aux | grep [i]gn
```
##### systemd
```bash
sudo systemctl status nginx              # состояние
sudo systemctl start nginx               # запуск
sudo systemctl stop nginx                # остановка
sudo systemctl restart nginx             # перезапуск
sudo systemctl enable nginx              # автозапуск
sudo systemctl disable nginx             # отключить автозапуск
sudo systemctl is-enabled <name>
sudo systemctl is-active <name>
sudo journalctl -u nginx -f              # логи сервиса
```

###### Пишем свой (для приложения из домашки)

> [!IMPORTANT]  
> Установить nodejs
> curl -fsSL https://deb.nodesource.com/setup_22.x | sudo bash - 
> sudo apt-get install -y nodejs

unit-file (`/etc/systemd/system/nodeapp.service`)
```ini
[Unit]
Description=Nodejs simple server
After=network.target

[Service]
Type=simple
User=anestesia
Group=anestesia
Environment=MYAPP_PORT=3000
WorkingDirectory=/home/anestesia/less_06
ExecStart=/usr/bin/node app.js
Restart=always
RestartSec=10

SyslogIdentifier=nodeapp

[Install]
WantedBy=multi-user.target
```

проверка
```bash
sudo systemctl start nodeapp
sudo systemctl status nodeapp

curl 127.0.0.1:3000
curl 127.0.0.1:3000/kill

sudo systemctl status nodeapp
sudo journalctl -u nodeapp
```
