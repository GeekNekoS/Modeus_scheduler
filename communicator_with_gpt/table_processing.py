def when_study(file):
    """with open(file, "r", encoding="utf-8") as table:
        return table.read()"""

    res=""
    table = open(file)
    headers = table.readline().split()
    main_part=[]
    for row in table.readlines():
        main_part.append([i.encode('cp1251').decode('utf-8') for i in row.split()])

    teams={i[0]:"Учатся в: " for i in main_part}

    for action in main_part:
        teams[action[0]]+= action[2] + " "

    for team,days in teams.items():
        res += f"Команда {team} {days} \n"

    table.close()
    return res



