## grep
```bash
# строки с 'alice'
grep alice /etc/passwd

# поиск без учета регистра
grep -i bob data/users.txt

# рекурсивный поиск по директории
grep -r alex ./data

# строки, НЕ содержащие шаблон
grep -v bob data/students
```
## cut
```bash
# имя и email
cut -d',' -f2,3 data/users.csv

# имена пользователей в системе
cut -d':' -f1 /etc/passwd

# дата
cut -c1-8 data/data.txt

# код сервиса
cut -c9-13 data/data.txt

# статус
cut -c14- data/data.txt
```
## awk
```bash
# имена пользователей
awk -F',' 'NR>1 {print $2}' data/users.csv

# возраст больше 27
awk -F',' 'NR>1 && $4+0 > 27 {print $2, $4}' data/users.csv

# только ростовчане
awk -F',' 'NR>1 && $5 == "Rostov" {print $0}' data/users.csv
```

## sort, uniq, wc
```bash
# по алфавиту
sort data/fruits.txt

# в порядке возрастания
sort -n data/numbers.txt

# в порядке убывания
sort -nr data/numbers.txt

# в порядке убывания с удалением дубликатов
sort -r -u data/fruits.txt

# по полю
sort -k2 -n data/students.txt

sort data/fruits.txt | uniq -c

# подсчет строк
wc -l data/auth.log
```
## пайплайны
```bash
grep "user" /etc/passwd | cut -d: -f1
grep 'INFO' /var/log/cloud-init.log
grep 'INFO' /var/log/cloud-init.log | grep stages.py

# топ ip
grep -oE '(from|rhost=) [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' data/auth.log | awk '{print $2}' | sort | uniq -c | sort -nr | head -10

# топ user
grep -o 'for [^ ]*' data/auth.log | awk '{print $2}' | sort | uniq -c | sort -nr | head -10

df -h | grep -vE '^(tmpfs|devtmpfs)' | awk 'NR>1 {print $5 " " $6}'
free -h | awk 'NR==2 {print "Total: " $2 ", Used: " $3}'
```
## find
```bash
# все файлы .conf в /etc
find /etc -name "*.conf"

# readme.txt, README.TXT и т.п.
find ./ -iname "readme.txt"

# все .c файлы в каталогах src
find . -path "*src/*.c"

# все блочные устройства в /dev
find /dev -type d

# все скрипты .sh
find . -type f -name "*.sh"

# файлы больше 10 мегабайт
find . -size +10M

# файлы с битом s
sudo find / -perm /u+s

# удалить все .tmp файлы
find . -name "*.tmp" -delete 

# удалить все file
find . -name "file*" -exec rm {} \;

mkdir ../bkp
# скопировать каждый .txt в ../bkp
find . -name "*.txt" -exec cp {} ../bkp \;

# множественная смена прав
find /var/www -type f -exec chmod 644 {} \;
find /var/www -type d -exec chmod 755 {} \;
```
### xargs
```bash
ls *.log | xargs rm

find . -name "*.log" -type f -print0 | xargs -0 rm -f
```
## потоки 
```bash
cat > somefile
line1
line2
Ctrl+D

cat somefile

cat << EOF > anotherfile
line1
line2
EOF

# перезапись файла (создание и запись, если не существовало)
ls -l > filelist

# добавляет вывод в конец файла
ls -l >> filelist.txt

# Сохранить только ошибки, обычный вывод проигнорировать
find / -name "*.conf" 2> errors.txt > /dev/null

# Записать весь вывод (и обычный, и ошибки) в один файл
make all > build.log 2>&1

# полное подавление вывода
ls -l nofile /home  > /dev/null 2>&1

# разделение потоков в разные файлы
ls -l nofile /home 1> results 2> errors
```
## репозитории и пакетный менеджер
```bash
# обновить кэш
sudo apt update

# установить пакет
sudo apt install -y bat

# удалить пакет
sudo apt remove bat
# или
sudo apt purge bat

# альтернативная установка
wget https://github.com/sharkdp/bat/releases/download/v0.26.1/bat_0.26.1_amd64.deb
sudo apt install ./bat_0.26.1_amd64.deb
bat --version
bat ~/.bashrc

# сборка из исходников
sudo apt install build-essential libncurses-dev
git clone https://github.com/htop-dev/htop.git
cd htop
./autogen.sh
./configure --prefix=/usr/local
make -j$(nproc) # -j для параллельной сборки на всех ядрах
sudo make install
# Проверяем
/usr/local/bin/htop --version
htop --version
```