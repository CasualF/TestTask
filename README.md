# Тестовое задание
## Запуск

Чтобы запустить код локально, сначала создайте .env файл с переменными указанными в env.example(поменяйте REDIS_HOST с redis на localhost) и используйте [pip](https://pip.pypa.io/en/stable/), чтобы скачать библиотеки

```bash
pip install -r requirements.txt
```

Для докера создайте также .env как указано выше(REDIS_HOST менять не надо) и используйте эти команды:
```bash
sudo docker-compose build
sudo docker-compose up
```

## Как использовать

Либо через сваггер либо сами отправьте пост запрос на ендпоинт /send_email с телом запроса 
```json
{
    "to": "example.email.com",
    "subject": "Test Subject",
    "message": "Some message"
}

