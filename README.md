# DRF_HomeWorks

Учебный проект по работе с курсами (API)

## Команды при работе с проектом 

### Установка всех зависимостей из файла
```commandline
pip install -r requirements.txt
```
### Тестирование (отчёт о покрытии)
```commandline
coverage run --source='.' manage.py test
```

```commandline
coverage report
```

### Запуск сервера redis 
```commandline
redis-server
```

### Запуск celery
```commandline
celery -A config worker -l INFO
```

### celery - beat 
```commandline
celery -A config worker --beat --scheduler django --loglevel=info
```

### запуск docker
```commandline
docker-compose up -d --build
```

https://docs.stripe.com/terminal/references/testing#standard-test-cards карты для тестирования платежей 