import sqlite3

def createDb():
    conn = sqlite3.connect("Space.db")
    cursor = conn.cursor()
    try:
        Missions = """  CREATE TABLE IF NOT EXISTS Missions(
                        Id INTEGER PRIMARY KEY, 
                        Nome TEXT NOT NULL, 
                        Lancamento DATE,
                        Destino TEXT NOT NULL,
                        Estado TEXT NOT NULL,
                        Tripulacao TEXT NOT NULL,
                        Cargas TEXT NOT NULL,
                        Custo DECIMAL NOT NULL,
                        Duracao INTEGER NOT NULL,
                        Status TEXT NOT NULL,
                        Nave TEXT NOT NULL)"""
        cursor.execute(Missions)

        conn.commit()
    except sqlite3.Error as error:
            return error
    finally:
            conn.close()
            print('Conexão finalizada')
createDb()