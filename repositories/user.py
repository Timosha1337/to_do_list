from models import engine, Users, Tasks, reset_database
from sqlalchemy import insert, select, func, delete
from datetime import datetime


class UserRepository:
    def __init__(self, engine):
        self.engine = engine
        
    def create(self,name, login, password):
        with self.engine.begin() as transaction:
            stmt = insert(Users).values(name=name,login=login,password=password).returning(Users.c.id)
            result = transaction.execute(stmt)
            return result.scalar_one()
    def delete_user(self, id):
        with self.engine.begin() as transaction:
            stmt = delete(Users).where(Users.c.id == id)
            transaction.execute(stmt)


