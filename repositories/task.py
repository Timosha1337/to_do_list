from models import engine, Users, Tasks, reset_database
from sqlalchemy import insert, select, func, delete, update
from datetime import datetime

class TaskRepository:
    def __init__(self, engine):
        self.engine = engine

    def create(self,*, user_id, title, description:str = None, due_date: datetime = None, is_completed=False):
        with self.engine.begin() as transaction:
            stmt = insert(Tasks).values(user_id = user_id,
                                       title =title,
                                       description = description,
                                       due_date = due_date,
                                       is_completed = is_completed).returning(Tasks.c.id)
            result = transaction.execute(stmt)
            return result.scalar_one()
            
    def update_task(self, *,task_id, user_id, status:bool | None = None, title:str|None = None, decription:str|None = None, due_date:datetime|None=None):
        values = {}
        if status is not None:
            values["is_completed"] = status
        if title is not None:
            values["title"] = title
        if decription is not None:
            values["decription"] = decription
        if due_date is not None:
            values["due_date"] = due_date
        with self.engine.begin() as transaction:
            stmt = update(Tasks).where((Tasks.c.user_id == user_id)&(Tasks.c.id==task_id)).values(**values)
            result = transaction.execute(stmt)
            if result.rowcount == 0:
                raise Exception(f"Задача task_id = {task_id} не найдена для пользователя user_id = {user_id}")
    def delete_task(self,task_id):
            with self.engine.begin() as transaction:
                stmt = delete(Tasks).where(Tasks.c.id == task_id)
                transaction.execute(stmt)