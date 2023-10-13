# Modeus_scheduler
Программа, помогающая студентам УрФУ формировать индивидуальное расписание
<br /> <br />


# Навигация
[Информация о тестовом Telegram боте](#telegram_bot_info)
<br /> <br />


<a name="telegram_bot_info"></a> 
## Информация о тестовом Telegram боте
• Токен: 1300397462:AAGyQDVN8WUEEKPazUnB8Lv9KeDz5RmzzsE

• Ник бота: @exampdd_bot (Простенький бот, в нём пару вариантов экзамена по ПДД)
<br /> <br />


## Установка проекта на ПК
1. Откройте консоль, вбив в поисковике ПК: <code>cmd</code>
2. Перейдите в директорию, куда хотите установить проект, пропишите следующую команду в консоль: <code>cd N:\Путь\до\папки\с\проектами</code>
3. Введите следующую команду: <code>git clone https://github.com/GeekNekoS/Modeus_scheduler.git </code>
4. Откройте скачанный проект и можете приступать к разработке
<br /> <br />


## Настройка готового проекта
• Версия Python: 3.11.5

• После скачивания проекта к себе на компьютер не забудьте установить необходимые зависимости, прописав к консоли команду: 
<code>pip install -r requirements.txt</code>

• Создайте файл .env и заполните в нём переменные LOGIN и PASSWORD (пока что от вашего Modeus аккаунта)

• Установите PostgreSQL (отсюда: https://www.postgresql.org/download/) с дефолтными настройками (в настройках установки ничего не меняете)
<br /> <br />


## Настройка PoastgreSQL
В диалоговом окне установщика PoastgreSQL:

• Задаёте пароль для суперпользователя: <code>1</code> (в наших локальных проектах будет "1", а при деплое на сервер мы зададим нормальный пароль)

В итоге должно получиться:
1. Директория PostgreSQL: <code>C:\Program Files\PostgreSQL\16</code>
2. Директория данных: <code>C:\Program Files\PostgreSQL\16\data</code>
3. Пароль: <code>1</code>
4. Порт: <code>5432</code>

• Создайте новую базу данных через pgAdmin (дополнение к PostgreSQL, помогающее в более удобном формате работать с данными)

Инструкция:
1. Откройте pgAdmin
2. Нажмите правой кнопкой мыши "Servers" (в левом верхнем углу)
3. Введите ранее созданный пароль суперпользователя - "1"
4. Правой кнопкой мыши нажмите "Databases" в выплывшем перечне
5. Нажмите "Create"
6. Нажмите "Database..."
7. Введите название базы: <code>schedules</code>
8. Нажмите "Save"
<br /> <br />


## Структура базы данных (черновик)
<table>
    <thead>
        <tr><th>Уроки</th></tr>
    </thead>
    <tbody>
        <tr><td>ИТИС</td></tr>
        <tr><td>История</td></tr>
        <tr><td>Математика</td></tr>
        <tr><td>ИРГ</td></tr>
        <tr><td>Физика</td></tr>
        <tr><td>Английский</td></tr>
    </tbody>
</table>
<br />


## Музычка для разработки
• Pink Floyd <br />
|__ Waiting for the Worms ♡ <br />
|__ Run Like Hell <br />
|__ Hay You <br />
|__ Don't Leave Me Now <br />
|__ Young Lust ♡ <br />
|__ Breathe (In The Air) [2011 Remastered Version] ♡ <br />
|__ On The Run [2011 Remastered Version] <br />
|__ Since On You Crazy Diamond, Pst. 1-5 (Edited) ♡ <br />
|__ Money <br />
|__ Time (Edited) <br />
|__ Comfortably Numb <br />
|__ Learning to Fly
<br /> <br />


## Почистить зависимости
• pyttsx3 <br />
• pandas
<br /> <br />
