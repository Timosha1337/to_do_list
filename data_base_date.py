from models import engine, Users, Tasks, reset_database
from sqlalchemy import insert
from datetime import datetime
from repositories.user import UserRepository
from repositories.task import TaskRepository




connection = engine.connect()
reset_database()
connection.execute(insert(Users),[
    {
        "name": "Vladimir Belousov",
        "login": "andescols",
        "password": "Vlad12345"
    },
    {
        "name": "Alexander Petrov",
        "login": "alexpetrov",
        "password": "Alex98765"
    },
    {
        "name": "Dmitry Sokolov",
        "login": "d_sokolov",
        "password": "Dmitr54321"
    },
    {
        "name": "Ivan Morozov",
        "login": "ivanmoroz",
        "password": "Ivan45678"
    },
    {
        "name": "Maxim Volkov",
        "login": "maxvolkov",
        "password": "Maxim13579"
    },
    {
        "name": "Sergey Orlov",
        "login": "sergey_orlov",
        "password": "Sergey24680"
    },
    {
        "name": "Nikita Fedorov",
        "login": "nik_fedorov",
        "password": "Nikita11223"
    },
    {
        "name": "Andrey Kuznetsov",
        "login": "andrey_kuz",
        "password": "Andrey77889"
    },
    {
        "name": "Mikhail Lebedev",
        "login": "mikelebedev",
        "password": "Mikhail33445"
    },
    {
        "name": "Roman Smirnov",
        "login": "roman_smirnov",
        "password": "Roman55667"
    }
])


connection.execute(insert(Tasks),[
    {
        "user_id": 1,
        "title": "Подготовить отчет по проекту",
        "description": "Собрать результаты за текущий месяц и подготовить отчет для руководителя.",
        "due_date": datetime(2026, 8, 28, 18, 0),
        "is_completed": False
    },
    {
        "user_id": 1,
        "title": "Обновить документацию",
        "description": "Проверить актуальность технической документации проекта.",
        "due_date": datetime(2026, 8, 30, 15, 0),
        "is_completed": True
    },

    {
        "user_id": 2,
        "title": "Провести встречу с командой",
        "description": "Обсудить текущие задачи, проблемы и планы на следующую неделю.",
        "due_date": datetime(2026, 8, 29, 11, 0),
        "is_completed": False
    },
    {
        "user_id": 2,
        "title": "Разобрать входящие письма",
        "description": "Ответить на важные письма и распределить остальные обращения.",
        "due_date": datetime(2026, 8, 27, 19, 0),
        "is_completed": True
    },

    {
        "user_id": 3,
        "title": "Исправить ошибки в API",
        "description": "Исправить ошибки обработки запросов и проверить API через Postman.",
        "due_date": datetime(2026, 8, 31, 17, 0),
        "is_completed": False
    },
    {
        "user_id": 3,
        "title": "Написать тесты",
        "description": "Добавить unit-тесты для основных функций приложения.",
        "due_date": datetime(2026, 9, 2, 18, 0),
        "is_completed": False
    },

    {
        "user_id": 4,
        "title": "Оплатить счета",
        "description": "Проверить счета за текущий месяц и произвести необходимые платежи.",
        "due_date": datetime(2026, 8, 28, 12, 0),
        "is_completed": True
    },
    {
        "user_id": 4,
        "title": "Записаться к врачу",
        "description": "Найти подходящее время для приема и записаться через приложение.",
        "due_date": datetime(2026, 9, 5, 10, 0),
        "is_completed": False
    },

    {
        "user_id": 5,
        "title": "Подготовить презентацию",
        "description": "Сделать презентацию для завтрашнего выступления.",
        "due_date": datetime(2026, 8, 28, 20, 0),
        "is_completed": False
    },
    {
        "user_id": 5,
        "title": "Проверить макеты",
        "description": "Проверить последние версии макетов перед передачей в разработку.",
        "due_date": datetime(2026, 8, 29, 16, 0),
        "is_completed": True
    },

    {
        "user_id": 6,
        "title": "Купить продукты",
        "description": "Купить продукты на ближайшие несколько дней.",
        "due_date": datetime(2026, 8, 27, 20, 0),
        "is_completed": False
    },
    {
        "user_id": 6,
        "title": "Убраться дома",
        "description": "Провести уборку квартиры и привести в порядок рабочее место.",
        "due_date": datetime(2026, 8, 30, 14, 0),
        "is_completed": False
    },

    {
        "user_id": 7,
        "title": "Изучить SQLAlchemy",
        "description": "Разобраться с Core API, таблицами и выполнением SQL-запросов.",
        "due_date": datetime(2026, 9, 1, 21, 0),
        "is_completed": False
    },
    {
        "user_id": 7,
        "title": "Создать CRUD для задач",
        "description": "Реализовать создание, получение, изменение и удаление задач.",
        "due_date": datetime(2026, 9, 4, 18, 0),
        "is_completed": False
    },

    {
        "user_id": 8,
        "title": "Забронировать отель",
        "description": "Выбрать подходящий отель и забронировать номер на выходные.",
        "due_date": datetime(2026, 9, 3, 19, 0),
        "is_completed": True
    },
    {
        "user_id": 8,
        "title": "Составить план поездки",
        "description": "Определить места для посещения и составить маршрут.",
        "due_date": datetime(2026, 9, 6, 18, 0),
        "is_completed": False
    },

    {
        "user_id": 9,
        "title": "Проверить базу данных",
        "description": "Проверить структуру таблиц и наличие некорректных записей.",
        "due_date": datetime(2026, 8, 30, 17, 0),
        "is_completed": True
    },
    {
        "user_id": 9,
        "title": "Оптимизировать SQL-запросы",
        "description": "Найти медленные запросы и проверить возможность добавления индексов.",
        "due_date": datetime(2026, 9, 3, 18, 0),
        "is_completed": False
    },

    {
        "user_id": 10,
        "title": "Обновить резюме",
        "description": "Добавить последние проекты, навыки и опыт работы.",
        "due_date": datetime(2026, 9, 1, 20, 0),
        "is_completed": False
    },
    {
        "user_id": 10,
        "title": "Изучить новую технологию",
        "description": "Посмотреть документацию и попробовать реализовать небольшой учебный проект.",
        "due_date": datetime(2026, 9, 7, 21, 0),
        "is_completed": False
    }
])

connection.commit()
connection.close()
user = UserRepository(engine)
user_id = user.create("Nikitisik","Mujik1337","123")
task = TaskRepository(engine)
task_id = task.create(user_id=user_id,title="Surfing",due_date = datetime(2026, 9, 7, 21, 0))
print(f"\ntask_id = {task_id}")
task.update_task(user_id=user_id,task_id = task_id,status=True)
user.delete_user(1)
user.delete_user(111)
task.delete_task(333)