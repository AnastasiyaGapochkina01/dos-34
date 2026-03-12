> [!NOTE]  
> все необходимые файлы лежат в директории `tasks-data` рядом с заданием

1) В файле `tasks-data/syslog` найти записи о dhcp
2) В файле `tasks-data/syslog` найти info записи
3) В файле `tasks-data/metrics.txt` найти все строки с `cpu_usage`
4) В файле `tasks-data/metrics.txt` подсчитать количество метрик `http_requests_total`
5) Из файла `tasks-data/metrics.txt` вывести только успешные HTTP-запросы (строки с `code="200"`)
6) Из файла `tasks-data/metrics.txt` вывести все значения использрвания памяти и диска
7) Вывести топ-5 IP по частоте из файла `tasks-data/access.log`
8) В файле `tasks-data/access.log` найти 404 ошибки
9) В файле `tasks-data/access.log` найти запросы от мобильных устройств (mobile iphone android)
10) В файле `tasks-data/access.log` посчитать количество ошибок (4xx/5xx)