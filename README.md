# Modeus_scheduler
Программа, помогающая студентам УрФУ формировать индивидуальное расписание
<br /> <br />


# Навигация
- [Установка проекта на ПК](#download_project)
- [Настройка готового проекта](#setting_up_project)
- [Настройка PoastgreSQL](#setting_up_postgres)
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

   
<a name="music"></a>
## Музычка для разработки
• Oliver Huntemann <br />
|__ [Magnet](https://www.youtube.com/watch?v=jNOFwlYShnw&list=OLAK5uy_kYFDjGM0qAA0Q2cSyuc1sl5pv2NERoVIU&index=9) ♡ <br />
|__ [Tranquilizer](https://www.youtube.com/watch?v=wtRPzzWjlUk&list=OLAK5uy_kYFDjGM0qAA0Q2cSyuc1sl5pv2NERoVIU&index=10) <br />
|__ [They Are (Not) After You](https://www.youtube.com/watch?v=ZpZ2hfxK93o&list=OLAK5uy_kYFDjGM0qAA0Q2cSyuc1sl5pv2NERoVIU&index=7) <br />
|__ [WatergateWorldWide #8 Oliver Huntemann](https://www.youtube.com/watch?v=vcBUb7fXNl0)

• Enigma <br />
|__ [Silence Must Be Heard](https://www.youtube.com/watch?v=tCUran3CDFg) <br />
|__ [Callas Went Away](https://www.youtube.com/watch?v=gWkWxFdpFHE) <br />
|__ [Smell Of Desire](https://www.youtube.com/watch?v=oVKit3pjc1g) <br />
|__ [Morphing Thru Time](https://www.youtube.com/watch?v=ZntPhESIHf4) ♡ <br />

• Relax & Chill <br />
|__ [Cartridge 1987 - Last Escape (Full Album)](https://www.youtube.com/watch?v=RwhgIvqR7QI) ♡ <br />
|__ [The Ultimate Skyrim Playlist](https://www.youtube.com/watch?v=JcwceBDUd68) <br />
|__ [The Elder Scrolls | Summer Landscapes of Skyrim](https://www.youtube.com/watch?v=sOpmG_retJE) <br />
|__ [Chill Drive ~ Stress Relief, Chill Music](https://www.youtube.com/watch?v=7MJBeAyU1As) <br />
|__ [Chill Drive ~ Stress Relief, Relaxing Your Mind](https://www.youtube.com/watch?v=25BkVBgFD9Y) <br />
|__ [Best of Joachim Heinrich | Beautiful Ambient Mix](https://www.youtube.com/watch?v=H5NZtbbiyKM) <br />
|__ [PURE Ambient Cyberpunk Music [VERY Soothing]](https://www.youtube.com/watch?v=FULCBFlX3Eo) <br />
|__ [ＣＹＢＥＲ　ＤＲＥＡＭ [Chillwave - Synthwave Mix])](https://www.youtube.com/watch?v=yhCuCqJbOVE) <br />
|__ [Minecraft Lush Cave](https://www.youtube.com/watch?v=VqJ9yWNWZLI) <br />

• Hideki Taniuchi <br />
|__ [Death Note Music Compilation - The Best of Death Note OST's](https://youtu.be/hKfKYpba0dE) ♡

• Jeremy Soule <br />
|__ [Skyrim Atmospheres [10 Hrs.]](https://www.youtube.com/watch?v=iGUEHPkaE5o)<br />

• A silly playlist for silly cat people <br />
|__ [Чистый кайф](https://www.youtube.com/watch?v=f-gi8k4IRh8)<br />
<br /> <br />


<a name="clean_up_dependencies"></a>
## Почистить зависимости
• pyttsx3 <br />
• pandas
<br /> <br />


## Деплой
nekos
<br /> <br />
