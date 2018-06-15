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
            row.remove(row[1])  # removing the player's hight, info that is unnecessary
            if "YES" in row:
                exp.append(row)
            else:
                inexp.append(row)

# sorting players equally into groups
def team_sorter():
    num_players = len(exp)/3
    dragons = []
    raptors = []
    sharks = []
    for item in exp:
        if exp.index(item) < num_players:
            dragons.append(item)
            dragons.append(inexp[exp.index(item)])
        elif exp.index(item) >= num_players * 2:
            sharks.append(item)
            sharks.append(inexp[exp.index(item)])
        else:
            raptors.append(item)
            raptors.append(inexp[exp.index(item)])
    teams.update({'Dragons': dragons, 'Raptors': raptors, 'Sharks': sharks})


# write the teams with players in teams.txt
def output_file():
    with open("teams.txt", "w") as file:
        for key, value in teams.items():
            file.write("\n" + key.upper() + ":\n")
            for val in value:
                file.write(", ".join(val) + "\n")
    file.close()

# welcome letter for every player as a text file named after the player,adressed to the guardian/s. Should contain name of player, team and date and time of first practice.
def welcome_letters(dict):
    for key, value in dict.items():
        if key == 'Sharks':
            practice = 'June 20th in 8 AM'
        elif key == 'Raptors':
            practice = 'June 21st in 8 AM'
        else:
            practice = 'June 22nd in 8 AM'
        for val in value:
            name = val[0]
            guardian = val[2]
            name_file = "_".join(name.split()).lower()
            with open(name_file+'.txt', 'w') as file:
                file.write("Dear {},".format(guardian) + "\n"+ "We would like to congratulate {} on becoming a member of team {}! Welcome! \nFirst practice will be on {}. \nSee you there! ".format(name, key, practice))

# make file run only when explicitly ran, not when imported

if __name__ == '__main__':
    experience_sorter()
    team_sorter()
    output_file()
    welcome_letters(teams)
