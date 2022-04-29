import sqlite3
import csv

conn = sqlite3.connect ('db_test')
print ("banco de dados aberto com sucesso")

file_csv = open("new_data.csv", "r")
csv_contents = csv.reader(file_csv)
# for j in csv_contents:
#     print(j[1])


def ConverterINT(string):
    # acc = 0
    # number = 0
    # for i in string:
    #     if (acc==0):
    #         number=number+int(i)
    #     else:
    #         number=(number)+(int(i)*10)
    #     acc+=1
    #     if (acc==5):break
    #     print("-i=", int(i), "acc=", acc, "method=", 10)
    number = int(string)
    print("number=", number)
    return number


# cursor = conn.cursor()
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
    # sql = )
    # print(acc)
    # print("sql_comand=", sql)
    if (acc>0):
        conn.execute(
            """INSERT INTO Jogadores (
                ID,Name,Age,
                Overall,Potential,Preferred_Foot,
                Weak_Foot,Position,Height,
                Weight,Finishing,HeadingAccuracy,
                ShortPassing,Volleys,Dribbling,
                Curve,FKAccuracy,LongPassing,
                BallControl,Acceleration,SprintSpeed,
                Agility,Reactions,Balance,
                ShotPower,Jumping,Stamina,
                Strength,LongShots,Aggression,
                Interceptions,Positioning,Vision,
                Penalties,Composure,Marking)
        VALUES (
            ?,?,?,?,?,?,
            ?,?,?,?,?,?,
            ?,?,?,?,?,?,
            ?,?,?,?,?,?,
            ?,?,?,?,?,?,
            ?,?,?,?,?,?);""",
         [ConverterINT(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),
        str(i[6]),str(i[7]),str(i[8]),
        str(i[9]),str(i[10]),str(i[11]),str([12]),
        str(i[13]),str(i[14]),str(i[15]),str(i[16]),
        str(i[17]),str(i[18]),str(i[19]),str(i[20]),
        str(i[21]),str(i[22]),str(i[23]),str(i[24]),
        str(i[25]),str(i[26]),str(i[27]),str(i[28]),
        str(i[29]),str(i[30]),str(i[31]),
        str(i[32]),str(i[33]),str(i[34]),str(i[35]),
        str(i[36])]
        )
    acc += 1

conn.commit ()
print("Registros criado com sucesso")
conn.close ()