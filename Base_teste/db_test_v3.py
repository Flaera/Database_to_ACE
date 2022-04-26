import sqlite3
import csv

conn = sqlite3.connect ('db_test')
print ("banco de dados aberto com sucesso")

file_csv = open("new_data.csv", "r")
csv_contents = csv.reader(file_csv)
# for j in csv_contents:
#     print(j)

cursor = conn.cursor()
acc = 0
for i in csv_contents:
    # sql = "INSERT INTO Jogadores (Name,Age,Overall,Potential,Preferred_Foot,Weak_Foot,Position,Height,Weight,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,Vision,Penalties,Composure,Marking)" \
    #     "VALUES ("+csv_contents[i][1]+","+csv_contents[i][2]+","+csv_contents[i][3]+","+csv_contents[i][4]+","+" \
    #     "+csv_contents[i][5]+","+csv_contents[i][6]+","+csv_contents[i][7]+","+csv_contents[i][8]+","+" \
    #     "+csv_contents[i][9]+","+csv_contents[i][10]+","+csv_contents[i][11]+","+csv_contents[i][12]+","+" \
    #     "+csv_contents[i][13]+","+csv_contents[i][14]+","+csv_contents[i][15]+","+csv_contents[i][16]+","+" \
    #     "+csv_contents[i][17]+","+csv_contents[i][18]+","+csv_contents[i][19]+","+csv_contents[i][20]+","+" \
    #     "+csv_contents[i][21]+","+csv_contents[i][22]+","+csv_contents[i][23]+","+csv_contents[i][24]+","+" \
    #     "+csv_contents[i][25]+","+csv_contents[i][26]+","+csv_contents[i][27]+","+csv_contents[i][28]+","+" \
    #     "+csv_contents[i][29]+","+csv_contents[i][30]+","+csv_contents[i][31]+","+" \
    #     "+csv_contents[i][32]+","+csv_contents[i][33]+","+csv_contents[i][34]+","+csv_contents[i][35]+");"
    sql = "INSERT INTO Jogadores (ID,Name,Age,Overall,Potential,Preferred_Foot,Weak_Foot,Position,Height,Weight,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,Vision,Penalties,Composure,Marking)" \
        "VALUES ("+i[0]+","+i[1]+","+i[2]+","+i[3]+","+i[4]+","+i[5]+","+" \
        "+i[6]+","+i[7]+","+i[8]+","+" \
        "+i[9]+","+i[10]+","+i[11]+","+i[12]+","+" \
        "+i[13]+","+i[14]+","+i[15]+","+i[16]+","+" \
        "+i[17]+","+i[18]+","+i[19]+","+i[20]+","+" \
        "+i[21]+","+i[22]+","+i[23]+","+i[24]+","+" \
        "+i[25]+","+i[26]+","+i[27]+","+i[28]+","+" \
        "+i[29]+","+i[30]+","+i[31]+","+" \
        "+i[32]+","+i[33]+","+i[34]+");"
    print(acc)
    print("sql_comand=", sql)
    if (acc>0):
        conn.execute(sql)
    acc += 1

conn.commit ()
print("Registros criado com sucesso")
conn.close ()