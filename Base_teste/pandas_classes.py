import sqlite3
import pandas


class CreateDB():
    def __init__(self):
        """Constructor:
        Constructor to create to database.
	DEPRECATED: It need corrections!!
        """
        conn = sqlite3.connect ('db_test')
        print ("Banco de dados aberto com sucesso=", conn)

        file_csv = pandas.read_csv("new_data_v2.csv", header=0)
        print("file=",file_csv.Name[0])
        print("lenght=",len(file_csv.ID))
        for i in range(0, len(file_csv.ID)):
            # print(i)
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
                [
                    file_csv.Name[i], file_csv.Age[i],
                    file_csv.Overall[i], file_csv.Potential[i], file_csv.Preferred_Foot[i],
                    file_csv.Weak_Foot[i], file_csv.Position[i], file_csv.Height[i],
                    file_csv.Weight[i], file_csv.Finishing[i], file_csv.HeadingAccuracy[i],
                    file_csv.ShortPassing[i], file_csv.Volleys[i], file_csv.Dribbling[i],
                    file_csv.Curve[i], file_csv.FKAccuracy[i], file_csv.LongPassing[i],
                    file_csv.BallControl[i], file_csv.Acceleration[i], file_csv.LongPassing[i],
                    file_csv.Agility[i], file_csv.Reactions[i], file_csv.Balance[i],
                    file_csv.ShotPower[i], file_csv.Jumping[i], file_csv.Stamina[i],
                    file_csv.Strength[i], file_csv.LongShots[i], file_csv.Aggression[i],
                    file_csv.Interceptions[i], file_csv.Positioning[i], file_csv.Vision[i],
                    file_csv.Penalties[i], file_csv.Composure[i], file_csv.Marking[i],
                    file_csv.Colum_plus[i]
                ]
            )
        conn.commit ()

        print("Registros criados com sucesso")
        conn.close ()
