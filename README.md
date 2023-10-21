# Modeus_scheduler
Программа, помогающая студентам УрФУ формировать индивидуальное расписание
<br /> <br />


# Навигация
- [Установка проекта на ПК](#download_project)
- [Настройка готового проекта](#setting_up_project)
- [Настройка PoastgreSQL](#setting_up_postgres)
- [Структура базы данных (черновик)](#database_structure)
- [Музычка для разработки](#music)
- [Почистить зависимости](#clean_up_dependencies)
<br /> <br />


<a name="download_project"></a> 
## Установка проекта на ПК
1. Откройте консоль, вбив в поисковике ПК: <code>cmd</code>
2. Перейдите в директорию, куда хотите установить проект, пропишите следующую команду в консоль: <code>cd N:\Путь\до\папки\с\проектами</code>
3. Введите следующую команду: <code>git clone https://github.com/GeekNekoS/Modeus_scheduler.git </code>
4. Откройте скачанный проект и можете приступать к разработке
<br /> <br />


<a name="setting_up_project"></a>
## Настройка готового проекта
• Версия Python: 3.11.5

• После скачивания проекта к себе на компьютер не забудьте установить необходимые зависимости, прописав к консоли команду: 
<code>pip install -r requirements.txt</code>

• Создайте файл .env и заполните в нём переменные LOGIN и PASSWORD (пока что от вашего Modeus аккаунта)

• Установите PostgreSQL (отсюда: https://www.postgresql.org/download/) с дефолтными настройками (в настройках установки ничего не меняете)
<br /> <br />


<a name="setting_up_postgres"></a>
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


<a name="database_structure"></a>
## Структура базы данных (черновик)
<table>
    <thead>
        <tr><th>Модули</th></tr>
    </thead>
    <tbody>
        <tr><td>ИТИС</td></tr>
        <tr><td>История</td></tr>
        <tr><td>Математика</td></tr>
        <tr><td>ОРГ</td></tr>
        <tr><td>Физика</td></tr>
        <tr><td>Английский</td></tr>
    </tbody>
</table>
<br />


<a name="music"></a>
## Музычка для разработки
(слушать только в наушниках, передающих басы)

• Relax & Chill <br />
|__ [Study Music / relax & chill / rainy mood || Death Note OST ||](https://www.youtube.com/watch?v=uRzHHHz4Ypg) <br />
|__ [Nostalgic Minecraft Music](https://www.youtube.com/watch?v=TV1Nj555ShQ) <br />
|__ [Minecraft ambience](https://www.youtube.com/watch?v=FlaDNyuPnfg)

• Hideki Taniuchi <br />
|__ [Death Note Music Compilation - The Best of Death Note OST's](https://youtu.be/hKfKYpba0dE) ♡

• Jeremy Soule <br />
|__ [Skyrim Atmospheres [10 Hrs.]](https://www.youtube.com/watch?v=iGUEHPkaE5o)<br />

• Black Sun Empire [осторожно, берегите свои ушки]<br />
|__ [Eye-D Unicorn MF](https://www.youtube.com/watch?v=LT-pfqmq2kc&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=22) ♡ <br />
|__ [Boris The Blade](https://www.youtube.com/watch?v=5lAyhChKqNc&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=9) <br />
|__ [Swipe](https://www.youtube.com/watch?v=OoG_YE69aPg&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=8) <br />
|__ [The Rat](https://www.youtube.com/watch?v=jBhkRqAQo_E&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=6)

• A silly playlist for silly cat people <br />
|__ [Чистый кайф](https://www.youtube.com/watch?v=f-gi8k4IRh8)<br />
<br /> <br />


<a name="clean_up_dependencies"></a>
## Почистить зависимости
• pyttsx3 <br />
• pandas
<br /> <br />
