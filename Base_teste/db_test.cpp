#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <map>
//#include <functional>
#include "sqlite3.h"

using namespace std;


string readFileIntoString(const string& path) {
    auto ss = ostringstream{};
    ifstream input_file(path);
    if (!input_file.is_open()) {
        cerr << "Could not open the file - '"
             << path << "'" << endl;
        exit(EXIT_FAILURE);
    }
    ss << input_file.rdbuf();
    return ss.str();
}


int callback (void * NotUsed, int argc, char ** argv, char ** azColName) {
   int i;
   //for (i = 0; i & lt; argc; i ++) {
    for (i = 0; argc; i ++) {
        //printf ( "%s = %s \n", azColName [i], argv [i] argv [i]: "NULL");
        printf ( "%s = %s \n", azColName [i], argv [i]);
    }
   printf ( "\n");
   return 0;
}


int main (int argc, char * argv [])
{
   sqlite3 * db;
   char * zErrMsg = 0;
   int rc;
   char * sql;
   //string sql;

   /* Abrir banco de dados */
   rc = sqlite3_open ( "db_test.db", &db);
   if (rc) {
      fprintf (stderr, "Não é possível abrir banco de dados: %s \n", sqlite3_errmsg (db));
      exit (0);
   } else {
      fprintf (stderr, "banco de dados aberto com êxito \n");
   }


    string filename("new_data.csv");
    string file_contents;
    std::map<int, std::vector<string>> csv_contents;
    char delimiter = ',';

    file_contents = readFileIntoString(filename);

    istringstream sstream(file_contents);
    std::vector<string> items;
    string record;

    int counter = 0;
    while (std::getline(sstream, record)) {
        istringstream line(record);
        while (std::getline(line, record, delimiter)) {
            //record.erase(std::remove_cv(record.begin(), record.end(), isspace), record.end());
            items.push_back(record);
        }

        csv_contents[counter] = items;
        items.clear();
        counter += 1;
    }


    for (int i=0; i<counter; i++)
    {
        /* Criar instrução SQL */
        
        sql = "INSERT INTO Jogadores (Name,Age,Overall,Potential,Preferred_Foot,Weak_Foot,Position,Height,Weight,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,Vision,Penalties,Composure,Marking)" \
        "VALUES ("+csv_contents[i][1]+","+csv_contents[i][2]+","+csv_contents[i][3]+","+csv_contents[i][4]+" \
        "+csv_contents[i][5]+","+csv_contents[i][6]+","+csv_contents[i][7]+","+csv_contents[i][8]+" \
        "+csv_contents[i][9]+","+csv_contents[i][10]+","+csv_contents[i][11]+","+csv_contents[i][12]+" \
        "+csv_contents[i][13]+","+csv_contents[i][14]+","+csv_contents[i][15]+","+csv_contents[i][16]+" \
        "+csv_contents[i][17]+","+csv_contents[i][18]+","+csv_contents[i][19]+","+csv_contents[i][20]+" \
        "+csv_contents[i][21]+","+csv_contents[i][22]+","+csv_contents[i][23]+","+csv_contents[i][24]+" \
        "+csv_contents[i][25]+","+csv_contents[i][26]+","+csv_contents[i][27]+","+csv_contents[i][28]+" \
        "+csv_contents[i][29]+","+csv_contents[i][30]+","+csv_contents[i][31]+" \
        "+csv_contents[i][32]+","+csv_contents[i][33]+","+csv_contents[i][34]+","+csv_contents[i][35]+");";
        //cout<<"lines="<<csv_contents[i][35]<<endl;
        /* Executar instrução SQL */
        rc = sqlite3_exec (db, sql, callback, 0, & zErrMsg);
    }
   if (rc != SQLITE_OK) {
      fprintf (stderr, "Erro de SQL: %s \n", zErrMsg);
      sqlite3_free (zErrMsg);
   } else {
      fprintf (stdout, "registros criados com sucesso \n");
   }
   sqlite3_close (db);
   return 0;
}