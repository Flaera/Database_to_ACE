using System.Data.SQLite;
using System.Text;
using System.Windows;

namespace bd_ace
{
    public class Connection
    {
        public SQLiteConnection conn = new SQLiteConnection("Data Source=bd_ace.sdb");

        public void ToConnection(){
            conn.Open();
        }
        public void ToDesconnection(){
            conn.Close();
            //MessageBox();
        }
    }
}