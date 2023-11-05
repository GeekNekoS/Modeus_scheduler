def when_study(file):
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
        res += f"{team} {days} \n"

    table.close()
    return res

