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
|__ [Tranquilizer](https://www.youtube.com/watch?v=wtRPzzWjlUk&list=OLAK5uy_kYFDjGM0qAA0Q2cSyuc1sl5pv2NERoVIU&index=10) <br />
|__ [Magnet](https://www.youtube.com/watch?v=jNOFwlYShnw&list=OLAK5uy_kYFDjGM0qAA0Q2cSyuc1sl5pv2NERoVIU&index=9) ♡ <br />
|__ [They Are (Not) After You](https://www.youtube.com/watch?v=ZpZ2hfxK93o&list=OLAK5uy_kYFDjGM0qAA0Q2cSyuc1sl5pv2NERoVIU&index=7) <br />
|__ [WatergateWorldWide #8 Oliver Huntemann & Marco Resmann](https://www.youtube.com/watch?v=vcBUb7fXNl0) 

• Magdalena Bay <br />
|__ [Head Over Heels](https://www.youtube.com/watch?v=T8WDr5fkwCw&list=PLS28calGpTQ88M7zu6IkgLwm5Rbk0nNVD&index=50 <br />
|__ [Tonguetwister](https://www.youtube.com/watch?v=GATMtsjKOL0&list=PLS28calGpTQ88M7zu6IkgLwm5Rbk0nNVD&index=3) ♡ ♡ ♡ <br />
|__ [Top Dog](https://www.youtube.com/watch?v=ekxNdBZizNQ) ♡ <br />
|__ [All You Do](https://www.youtube.com/watch?v=-_DuYs33JJk) <br />
|__ [Killshot](https://www.youtube.com/watch?v=lhfs1CzzUPM)

• Enigma <br />
|__ [Silence Must Be Heard](https://www.youtube.com/watch?v=tCUran3CDFg) <br />
|__ [Callas Went Away](https://www.youtube.com/watch?v=gWkWxFdpFHE) <br />
|__ [Smell Of Desire](https://www.youtube.com/watch?v=oVKit3pjc1g) <br />
|__ [Morphing Thru Time](https://www.youtube.com/watch?v=ZntPhESIHf4) ♡ <br />

• Relax & Chill <br />
|__ [The Ultimate Skyrim Playlist | Eleven Hours of Peaceful and Immersive Skyrim Music & Ambience |](https://www.youtube.com/watch?v=JcwceBDUd68) ♡ <br />
|__ [The Elder Scrolls | Summer Landscapes with Peaceful Music from Skyrim, Morrowind, Oblivion, and ESO](https://www.youtube.com/watch?v=sOpmG_retJE) ♡ <br />
|__ [Chill Drive - Lofi hip hop mix ~ Stress Relief, Chill Music](https://www.youtube.com/watch?v=7MJBeAyU1As) <br />
|__ [The Elder Scrolls: Skyrim | Winter Storms Music & Ambience 🎧 12 Peaceful Scenes](https://www.youtube.com/watch?v=FNBf2yNOzhY) ♡ <br />
|__ [Chill Drive - Lofi hip hop mix ~ Stress Relief, Relaxing Your Mind](https://www.youtube.com/watch?v=25BkVBgFD9Y) ♡ <br />
|__ [Best of Joachim Heinrich | Beautiful Ambient Mix](https://www.youtube.com/watch?v=H5NZtbbiyKM) ♡ <br />
|__ [all of a sudden, everything becomes alright...](https://www.youtube.com/watch?v=ANkxRGvl1VY) <br />
|__ [Windy 🌬️ Lofi Keep You Safe 🍂 Lofi Hip Hop ~ Deep to Sleep / Relax / Study](https://www.youtube.com/watch?v=qW2lX0LnTQA) <br />
|__ [Cruising Through the Galaxy with Synthwave](https://www.youtube.com/watch?v=DUQkBgTDCiE) <br />
|__ [Synthwave/Electric Mixtape I | For Study/Relax](https://www.youtube.com/watch?v=k3WkJq478To) <br />
|__ [💜 Minecraft Amethyst Geode Koi Pond 💜](https://www.youtube.com/watch?v=5zl30-PZxqI) <br />
|__ [The Forest of Dreams 🌿 Minecraft Ambience & Music Box](https://www.youtube.com/watch?v=8TvpUMKZoCU) <br />
|__ [The Forest of Tranquility 🌿 Minecraft Ambience w/ C418 Music (Slowed)](https://www.youtube.com/watch?v=2Qh5YcV0p-I) <br />
|__ [Nature's Lullaby | Minecraft Ambience w/ C418 Music](https://www.youtube.com/watch?v=bjyjDNzQemo) <br />
|__ [Engineering Colony VI 'Cadwell's Reach' Kepler-62F (4 Hour Ambient)](https://www.youtube.com/watch?v=nVpXV6QDtj0) <br />
|__ [PURE Ambient Cyberpunk Music For Focus and DEEP Relaxation [VERY Soothing]](https://www.youtube.com/watch?v=FULCBFlX3Eo) ♡ <br />
|__ [ＣＹＢＥＲ　ＤＲＥＡＭ [Chillwave - Synthwave Mix])](https://www.youtube.com/watch?v=yhCuCqJbOVE) <br />
|__ [Blade Runner Bliss](https://www.youtube.com/watch?v=4FhsjQ2xess) <br />
|__ [3 hours of minecraft relaxing music with house in rain to sleep and relax](https://www.youtube.com/watch?v=MZqcaMe4FNE) <br />
|__ [Petals in the Moonlight](https://www.youtube.com/watch?v=BKjUfSb5UU0) <br />
|__ [Minecraft Lush Cave](https://www.youtube.com/watch?v=VqJ9yWNWZLI) ♡ <br />
|__ [Minecraft Lush Cave Ambience w/ C418 Music Box | 8 Hours](https://www.youtube.com/watch?v=HnLScCOFCv0) <br />
|__ [Wake up, you're dreaming...](https://www.youtube.com/watch?v=oC4o0litO-4) <br />
|__ [A Night of Chills | Minecraft Ambience](https://www.youtube.com/watch?v=PzC-QfWdYoE) <br />
|__ [Nostalgic Minecraft Music](https://www.youtube.com/watch?v=TV1Nj555ShQ) <br />
|__ [Minecraft ambience](https://www.youtube.com/watch?v=FlaDNyuPnfg) <br />
|__ [Quiet & Restful Skyrim Music and Ambience](https://www.youtube.com/watch?v=lO9yYT1I7cU) <br />

• Drop Your Weapon [осторожно, берегите свои ушки] <br />
|__ [Drop Your Weapon](https://www.youtube.com/watch?v=2MNCQcLPGxI) <br />
|__ [Turn Off Your Radio](https://www.youtube.com/watch?v=giH4y6XRdzY) ♡ <br />
|__ [Chaos OD](https://www.youtube.com/watch?v=zE7xJ8QFZZQ) 

• Black Sun Empire [осторожно, берегите свои ушки] <br />
|__ [Don't You](https://www.youtube.com/watch?v=Y4YAsRd1Swk&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=2) <br />
|__ [Black Sun Empire - B-Negative (Ill Skillz Remix)](https://www.youtube.com/watch?v=GQAF9VYBBzc&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=11) ♡ <br />
|__ [Eye-D Unicorn MF](https://www.youtube.com/watch?v=LT-pfqmq2kc&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=22) ♡ <br />
|__ [Boris The Blade](https://www.youtube.com/watch?v=5lAyhChKqNc&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=9) ♡ <br />
|__ [Sinthetix - Cryogenic (Black Sun Empire remix)](https://www.youtube.com/watch?v=2L6pu0BPeJc&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=12) <br />
|__ [Swipe](https://www.youtube.com/watch?v=OoG_YE69aPg&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=8) <br />
|__ [The Rat](https://www.youtube.com/watch?v=jBhkRqAQo_E&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=6) <br />
|__ [Typecell - Bad Illusions (Black Sun Empire Remix)](https://www.youtube.com/watch?v=RunkjktX6Eg&list=OLAK5uy_nQDBv6d8yGaRObX_mIKW05ksSHOh-txQU&index=15) ♡

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
