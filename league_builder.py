import csv

exp = []
inexp =[]
teams = dict()

# Iterate through csv file and devide players into experienced and inexperienced
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

# sorting players equally into groups
def team_sorter():
    teams.update({"Dragons": list(exp[:3] + inexp[:3]), "Raptors": list(exp[3:6] + inexp[3:6]), "Sharks": list(exp[-3:] + inexp[-3:])})

# write the teams with players in teams.txt
def output_file():
    with open("teams.txt", "w") as file:
        for key, value in teams.items():
            file.write("\n" + key.upper() + ":\n")
            for v in value:
                file.write(", ".join(v) + "\n")
    file.close()

# welcome letter for every player as a text file named after the player,adressed to the guardian/s. Should contain name of player, team and date and time of first practice.
def welcome_letters(dict):
    for key, value in dict.items():
        for v in value:
            name = v[0]
            guardian = v[2]
            name_file = "_".join(name.split()).lower()
            with open(name_file+'.txt', 'w') as file:
                file.write("Dear {},".format(guardian) + "\n"+ "We would like to congratulate {} on becoming a member of team {}! Welcome! \nFirst practice will be on 8th of June in 9 AM. \nSee you there! ".format(name, key))

# make file run only when explicitly ran, not when imported

if __name__ == '__main__':
    experience_sorter()
    team_sorter()
    output_file()
    welcome_letters(teams)
