1) Запустить процесс top в одном терминале. Во втором терминале поотправлять ему разные сигналы с помощью kill и посмотреть как меняется статус процесса:
- SIGSTOP
- SIGCONT 
- SIGTERM/SIGKILL
2) Установить на ВМ nginx; найти все процессы nginx и вывести для них ppid, pid, command
3) Посмотреть дерево процессов только для nginx
4) Убить master процесс nginx; проверить состояние сервиса nginx (systemctl)
5) Запустить сервис nginx
6) Убить один из воркеров nginx; проверить количество воркеров после убийства одного
7) Запустить `sleep 3000`
- остановить процесс
- вывести список job`s
- перевести процесс sleep в background
- вытащить процесс sleep в foreground

### Задача со звездочкой
Установить на ВМ redis (инструкция досупна под VPN https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux/); запустить через unit-файл второй экземпляр redis на той же ВМ