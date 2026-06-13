1) Написать пайплайн для сборки и деплоя приложения https://github.com/AnastasiyaGapochkina01/cyberpunk-devops. Требования к пайплайну
    - имеется этап линтера для кода (можно использовать `pylint` и выставить `allow_failure: true`)
    - имеется этап сканирования кода на уязвимости (использовать библиотеку `bandit` https://github.com/pycqa/bandit ; `allow_failure: true` тоже разрешен)
    - пуш собранного docker image осуществляется в container registry gitlab
    - деплой запускается ТОЛЬКО в ручном режиме
