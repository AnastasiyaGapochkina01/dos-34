1) Запустить Flask-приложение, сохраняющее логи в volume на хосте и маппингом портов. Структура проекта
```
task-01/
├── Dockerfile
├── app.py
└── logs/
```
содержимое файла `app.py`
```python
from flask import Flask
import os, datetime
app = Flask(__name__)

@app.route('/')
def hello():
    log_path = '/logs/app.log'
    with open(log_path, 'a') as f:
        f.write(f"Request at {datetime.datetime.now()}\n")
    with open(log_path, 'r') as f:
        logs = f.read()
    return f"<h1>Hello Docker!</h1><pre>{logs}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
проверка
```bash
curl http://localhost:5000
```
2) Запустить с помощью docker compose приложение https://github.com/AnastasiyaGapochkina01/simple-docker-apps/tree/main/py-http-server
3) Запустить с помощью docker compose приложение https://github.com/AnastasiyaGapochkina01/cyberpunk-devops
