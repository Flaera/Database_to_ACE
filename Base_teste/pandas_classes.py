import sqlite3
import pandas


class CreateDB():
    def __init__(self):
        """Constructor:
        Constructor to create to database.
	    DEPRECATED: It need corrections in colums that were added!!
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



class CreateTableMedia():
    def __init__(self):
        """Constructor:
        
        """

        self.conn = sqlite3.connect('db_test_new.db')
        print ("Banco de dados aberto com sucesso=", self.conn)

        self.file_csv = pandas.read_csv("data2.csv", header=0)
        print("data_frame: ", self.file_csv)

        self.medians = [0.0,0.0,0.0,0.0,0.0,
                    0.0,0.0,0.0,0.0,0.0,
                    0.0,0.0]
        #print("medians=",medians)

        self.lenght = len(self.file_csv)
        print("len=", self.lenght)
        # for i in range(0, self.lenght):
        #     self.medians[0] += self.file_csv.Finishing[i]
        self.medians[0] = self.file_csv.Finishing.sum()
        self.medians[1] = self.file_csv.HeadingAccuracy.sum()
        self.medians[2] = self.file_csv.ShortPassing.sum()
        self.medians[3] = self.file_csv.Dribbling.sum()
        self.medians[4] = self.file_csv.FKAccuracy.sum()
        self.medians[5] = self.file_csv.LongPassing.sum()
        self.medians[6] = self.file_csv.Acceleration.sum()
        self.medians[7] = self.file_csv.Reactions.sum()
        self.medians[8] = self.file_csv.Stamina.sum()
        self.medians[9] = self.file_csv.LongShots.sum()
        self.medians[10] = self.file_csv.Marking.sum()
        self.medians[11] = self.file_csv.Penalties.sum()
        acc = 0
        for i in self.medians:
            self.medians[acc] = i / self.lenght
            acc+=1
        print(self.medians)

        self.conn.execute(
                    """INSERT INTO MediaJogadores (
                        Finishing,HeadingAccuracy,
                        ShortPassing,Dribbling,
                        FKAccuracy,LongPassing,
                        Acceleration,
                        Reactions,Stamina,
                        LongShots,
                        Marking,Penalties)
                    VALUES (
                        ?,?,
                        ?,?,
                        ?,?,
                        ?,
                        ?,?,
                        ?,
                        ?,?);""",
                [
                    self.medians[0],self.medians[1],
                    self.medians[2],self.medians[3],
                    self.medians[4],self.medians[5],
                    self.medians[6],
                    self.medians[7],self.medians[8],
                    self.medians[9],
                    self.medians[10],self.medians[11]
                ]
            )
        self.conn.commit()

        self.conn.close()
        