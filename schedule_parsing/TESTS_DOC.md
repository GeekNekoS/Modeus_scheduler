# Tests documentation
Разработка и тестирование бота-парсера
<br /> <br />


## Запуск тестов
• Запуск из папки tests: <code>python -m pytest schedule_parsing/tests/</code>

• Запуск из папки tests на 20-и процессорах: <code>python -m pytest schedule_parsing/tests/ -n 20</code>

• Запуск unit-тестов: <code>python -m unittest unittests</code>

• Всех автотестов проекта: <code>pytest</code>

• Многопоточный запуск на 20-и процессорах: <code>pytest -n 20</code>

• Запуск автотестов с отчётностью в Allure: <code>py.test --alluredir=allure-results</code>

• Просмотр отчётности Allure: <code>allure serve allure-results</code>
<br /> <br />


## Многопоточный запуск тестов
Добавить по необходимости: <code>pip install pytest-xdist</code>
<br /> <br />
