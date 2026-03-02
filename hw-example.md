1. Создал VM Ubuntu_us на гипервизозе VMWare
<img width="1210" height="858" alt="image" src="https://github.com/user-attachments/assets/3c204acd-aa89-48b6-9bfe-76e4d30954f3" />

2. Настроил доступ по ssh
3. Установил утилиту tree (`sudo apt install -y`)
- вывел корневое дерево каталогов (tree -L 1 /)
4. В домашней директории создал каталог `dvps-tasks` (`mkdir /dvps-tasks`)
- в каталоге dvps создал каталог Linux_01 (`mkdir /dvps-tasks/linux_01`)
- в каталоге Linux_01 создал файл text-00 (`nano text-00`)
5. Выяснил в каком нахожусь каталоге (`pwd`, `ls`)
- перешел в корень файловой системы (`cd /`, `pwd`, `cd`,)
- перешел в каталог /var/log и вывел сождержимое (`cd /var/log`, `Ls -1`)
- перешел в tmp по относительному пути (cd../../tmp)
- вернулся в домашний каталог (cd)
- перешел в каталог /usr/share из него в /etc/ssh далее в /usr/bin используя относительные пути(cd ../../)
