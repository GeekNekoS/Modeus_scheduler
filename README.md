# Modeus_scheduler
Программа, помогающая студентам УрФУ формировать индивидуальное расписание
<br /> <br />


# Навигация
- [Установка проекта на ПК](#download_project)
- [Настройка готового проекта](#setting_up_project)
- [Настройка PoastgreSQL](#setting_up_postgres)
- [Музычка для разработки](#music)
<br /> <br />


<a name="download_project"></a> 
## Установка проекта на ПК
1. Откройте консоль, вбив в поисковике ПК: <code>cmd</code>
2. Перейдите в директорию, куда хотите установить проект, пропишите следующую команду в консоль: <code>cd N:\Путь\до\папки\с\проектами</code>
3. Введите следующую команду: git clone https://github.com/[ник]/Modeus_scheduler.git
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

   
<a name="music"></a>
## Музычка для разработки
• Christmas Bass <br />
|__ [Jingle Bells Trap Remix](https://www.youtube.com/watch?v=ARMrGvYjgSs&list=PLaDRVbwxGG59mdCRtUFBB4w-y_Uy1saSU&index=1)

• Chill and relax <br />
|__ [Сладкий рождественский джаз в уютной кофейне](https://www.youtube.com/watch?v=2hgmHmOS_HM)

• For New Year's mood <br />
|__ [Frank Sinatra - Jingle Bells](https://www.youtube.com/watch?v=hLf0-lro8X8) <br />
|__ [Let It Snow! Let It Snow! Let It Snow!](https://www.youtube.com/watch?v=Rnil5LyK_B0) ♡ <br />

|__ [Rockin' Around The Christmas Tree](https://www.youtube.com/watch?v=1qYz7rfgLWE) <br />
|__ [Jingle Bell Rock](https://www.youtube.com/watch?v=Z0ajuTaHBtM) <br />
|__ [All I Want For Christmas Is You](https://www.youtube.com/watch?v=yXQViqx6GMY)
