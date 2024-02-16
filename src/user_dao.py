import sqlite3
from user import User
from singleton import Singleton

class UserDAO(metaclass=Singleton):
    """Classe qui va gérer les datas de type database et en faire des objets"""
    
    def __init__(self, filename) -> None:
        self.__con = sqlite3.connect(filename, password = "toto")
        self.__cur = self.__con.cursor()

    def __del__(self):
        if self.__con:
            print("Je femre dans le destruteur")
            self.__con.close()
        
        print("C'est détruit")

    def __enter__(self):
        """Nécessaire à l'implémentation de la classe en context manager (pour l'utiliser avec with)"""
        return self

    def __exit__(self, *exc):
        self.__con.close()
        self.__con = None
        print("Je ferme en sortant du context manager")
        return False

    def find_all(self):
        """Plutot que retourner une liste, on crée un générateur. Cela allège la mémoire"""

        sql = "SELECT * From users_tbl"

        res = self.__cur.execute(sql)

        for r in res.fetchall():
            user = User(*r)
            yield user

    def find_by_id(self, id: int):
        return next(self.__find("id", id))

    def __find(self, champ, valeur):
        sql = f"SELECT * From users_tbl WHERE {champ} = ?"

        res = self.__cur.execute(sql, [valeur])

        for r in res.fetchall():
            user = User(*r)
            yield user