import csv

exp = []
inexp =[]
teams = dict()

def experience_sorter():
    with open("soccer_players.csv", newline = "") as csvfile:
        sreader = csv.reader(csvfile, dialect='excel', delimiter = ",")
        rows = list(sreader)
        for row in rows[1:]:
            row.remove(row[1])
            if "YES" in row:
                exp.append(row)
            else:
                inexp.append(row)


def team_sorter():
    teams.update({"Dragons": list(exp[:3] + inexp[:3]), "Raptors": list(exp[3:6] + inexp[3:6]), "Sharks": list(exp[-3:] + inexp[-3:])})


def output_file():
    with open("teams.txt", "w") as file:
        for key, value in teams.items():
            file.write("\n" + key.upper() + ":\n")
            for v in value:
                file.write(", ".join(v) + "\n")
    file.close()



if __name__ == '__main__':
    experience_sorter()
    team_sorter()
    output_file()


    for key, value in teams.items():
        for v in value:
            name = v[0]
            guardian = v[2]
            name_file = "_".join(name.split()).lower()
            with open(name_file+'.txt', 'w') as file:
                file.write("Dear {},".format(guardian) + "\n"+ "We would like to congratulate {} on becoming a member of team {}! Welcome! \n First practice will be on 8th of June in 9AM. \n See you there! ".format(name, key))
    
