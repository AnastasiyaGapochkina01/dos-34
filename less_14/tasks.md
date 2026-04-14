1) Написать скрипт, для для мониторинга systemd-службы
- имя службы задается через позиционный аргумент
- проверяется налилчие указанной в аргументе функции
- если она существует - раз в минуту проверяется работает она или нет
- если НЕ работатет - производится попытка запустить службу (3 попытки с интервалом 5 секунд)
- после каждой попытки проверяет, запустилась сулжба или нет
- все действия логируются в файл `checker.log` в формате
```
[$timestamp] $loglevel msg: $message
```
например
```
[2026-04-14T07:18:39] WARNING msg: nginx is down. trying to restart - attempt 1
[2026-04-14T07:18:39] INFO msg: nginx successfully started

[2026-04-14T07:18:39] WARNING msg: mariadb is down. trying to restart - attempt 1
[2026-04-14T07:18:39] WARNING msg: mariadb failed to start
```
- написать systemd unit для запуска скрипта как systemd-службы
2) Написать скрипт для управления приложением `simple-server` https://github.com/AnastasiyaGapochkina01/dos-34/blob/main/less_14/simple-server ; \
**управляем процессом НЕ через systemd**
- запуск процесса в фоновом режиме с перенаправлением stdout и stderr в файл `simple-server.log`
- остановка процесса
- проверка работоспособности приложения (`curl`)
- все действия логируются в файл `simple-server-control.log`
