# Sprint_7

## # Тесты на API "Яндекс.Самокат"

## Структура проекта

1. allure_results - папка с отчетом о тестировании 
2. tests - папка с тестами 
3. conftest.py - фикстуры 
4. requirements.txt - файл с необходимыми библиотеками
5. data.py - файл с данными для тестов
6. helpers.py - файл с методами для тестов

## Запуск тестов
1. Установка зависимостей - pip install -r requirements.txt
2. Запуск тестов без отчета - pytest -v
3. Запуск тестов с отчетом - pytest --alluredir=allure_results
