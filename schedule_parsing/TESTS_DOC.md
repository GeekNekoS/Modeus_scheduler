# Tests documentation
Разработка и тестирование бота-парсера
<br /> <br />


## Запуск тестов
• Запуск unit-тестов: <code>python -m unittest unittests</code>

• Всех автотестов проекта: <code>pytest</code>

• Многопоточный запуск тестов на 20-и процессорах: <code>pytest -n 20</code>

• Запуск автотестов с отчётностью в Allure: <code>py.test --alluredir=allure-results</code>

• Просмотр отчётности Allure: <code>allure serve allure-results</code>

<!--
• Тестов модуля: <code>pytest test_mod.py</code>

• Запуск тестов из директории: <code>pytest testing/</code>
-->
<br /> <br />


## Многопоточный запуск тестов
Добавить по необходимости: <code>pip install pytest-xdist</code>
<br /> <br />
