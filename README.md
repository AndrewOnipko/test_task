# Тестовое задание

## Запуск скрипта 

Из корня проекта

```bash
python main.py --file test_logs/example1.log --report average --date 2025-06-22
```

* --file - путь к файлу
* --report - тип отчета 
* --date - опциональный фильтр по дате. 

## Тестирование

```bash
pytest --cov=.
```

## Для сборки Docker контейнера

```bash
docker-compose up -d --build
```

## Адрес Swagger после сборки

```
http://localhost:8000/docs#/
```