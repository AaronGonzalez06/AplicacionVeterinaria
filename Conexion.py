import mysql.connector
import pymysql
class DataBase:
    def __int__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            db="clinicaVeterinaria"
        )
        self.cursor=self.connection.cursor()


def hacerConsulta(sql):
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    return cur.fetchall()
