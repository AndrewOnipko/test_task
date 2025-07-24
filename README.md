# Тестовое задание

## Запуск скрипта

```bash
python main.py --file example1.log --report average --date 2025-06-22
```

* --file - путь к файлу
* --report - тип отчета 
* --date - опциональный фильтр по дате. 

## Тестирование

```bash
pytest --cov=.
```