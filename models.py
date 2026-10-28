import sqlalchemy
from sqlalchemy import create_engine, Table, Column, DateTime, Text, Integer, MetaData, ForeignKey, Boolean, insert, CheckConstraint
from datetime import datetime

engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5438/postgres", echo= True)


metadata = MetaData()

created_at = Column("created_at",DateTime(), default=datetime.now)
update_at = Column("update_at",DateTime(), default=datetime.now, onupdate=datetime.now)

def reset_database():
    metadata.drop_all(engine)
    metadata.create_all(engine)

Users = (Table(
    'Users',metadata,
    Column('id',Integer(),primary_key=True),
    Column('name', Text(),nullable= False),
    Column('login',Text(), nullable=False, unique=True),
    Column('password', Text(), nullable=False),
    created_at,update_at,
    CheckConstraint('length(trim(name)) > 1', name='name_not_empty'),
    CheckConstraint('length(trim(login)) > 1', name='login_not_empty'),
    CheckConstraint('length(trim(password)) > 1', name='password_not_empty')
))

Tasks = (Table(
    'Tasks', metadata,
    Column('id',Integer(), primary_key=True),
    Column('user_id', Integer(),ForeignKey(Users.c.id, ondelete="CASCADE")),
    Column('title', Text(), nullable=False),
    Column('description', Text(), nullable=True),
    Column('due_date', DateTime(),nullable=True),
    Column('is_completed',Boolean(), default= False),
    Column("created_at",DateTime(), default=datetime.now),
    Column("update_at",DateTime(), default=datetime.now, onupdate=datetime.now)
))
