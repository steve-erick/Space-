import sqlite3
from createdb import createDb

class DB():
    def conn(self):
        self.connection = sqlite3.connect('Space.db')
        self.cursor = self.connection.cursor()
    
    def __init__(self):
        try:
            createDb()
        except:
            print("Criação de tabela não executada")
        finally:
            print("Tabela criada com sucesso")
    def inserir(self,Nome,Lancamento,Destino,Estado,Tripulacao,Cargas,Custo,Duracao,Status,Nave):
        try:
            self.conn()  # Estabelece uma nova conexão
            QUERY = """INSERT INTO Missions(
            Nome, 
            Lancamento,
            Destino,
            Estado,
            Tripulacao,
            Cargas,
            Custo,
            Duracao,
            Status,
            Nave
            ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(QUERY, (Nome,Lancamento,Destino,Estado,Tripulacao,Cargas,Custo,Duracao,Status,Nave))
            self.connection.commit()
            print("inserção realizada com sucesso")
            return True
        except sqlite3.Error as error:
            print(error)
            return False
        finally:
            self.connection.close()
            print('Conexão encerrada')

    def View(self,ms_id=None):
        try:
            self.conn()  # Estabelece uma nova conexão
            if(ms_id != None):
                QUERY = """SELECT * FROM Missions WHERE id = ?"""
                self.cursor.execute(QUERY, (ms_id,))
                Mission = self.cursor.fetchone()  # O
                # print("chegou no if")
                return Mission
            else:     
                QUERY = """SELECT * FROM Missions"""
                rows = self.cursor.execute(QUERY).fetchall()
                # print("chegou no else")
                return rows
        except sqlite3.Error as error:
            print(error)
        finally:
            self.connection.close()
            print('Conexão encerrada')

    def update(self,ms_id,Nome,Lancamento,Destino,Estado,Tripulacao,Cargas,Custo,Duracao,Status,Nave):
        try:
            self.conn()
      
            QUERY = """UPDATE Missions SET 
            Nome = ?, 
            Lancamento = ?,
            Destino = ?,
            Estado = ?, 
            Tripulacao = ?,
            Cargas = ?,
            Custo = ?,
            Duracao = ?,
            Status = ?,
            Nave = ?  
            WHERE id = ?"""

            print(Nome,Lancamento,Destino,Estado,Tripulacao,Cargas,Custo,Duracao,Status,Nave,ms_id)
            self.cursor.execute(QUERY,(Nome,Lancamento,Destino,Estado,Tripulacao,Cargas,Custo,Duracao,Status,Nave,ms_id))
            self.connection.commit()
            return True
            # self.View()
        except sqlite3.Error as error:
            print(error)
            return False
        finally: 
            self.connection.close()
            print("Conexão encerrada")
    def delete(self,ms_id):
        try:
            self.conn()
            QUERY = """DELETE FROM Missions WHERE id = ?"""
            self.cursor.execute(QUERY,(ms_id,))
            self.connection.commit()
        except sqlite3.Error as error:
            print(error)
        finally: 
            self.connection.close()
            print("Conexão encerrada")

# Criar uma instância da classe DB
# db = DB()

# Inserir dados e visualizar
# db.inserir("Exploração de marte 2", "teste" ,"Marte","Em andamento","Capitão JONAS TENENTE BRUNO0","500G DE CELITA",100.00,10,"Atualmente a equipe esta pisando na superficie de marte","Aerotime-2")
# print(db.View())
# db.delete(3)
# db.View()

# db.update(3,'ANDERSON',1234)
