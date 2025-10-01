"""
Тест работы с SQLalchemy
"""
from sqlalchemy import create_engine, inspect, text

# соединение с базой
DB_CONNECTION_STRING = "postgresql://postgres:Study2024@localhost:5432/mybase"
db = create_engine(DB_CONNECTION_STRING)


def test_db_connection():
    """ Тест соединения с локальной базой """
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'


def test_insert():
    """ Добавление новой строки: название и идентификатор """
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(\"subject_id\", \"subject_title\")"
               "VALUES (:new_id, ;new_title)")
    connection.execute(sql, {"new_id": "17"}, {"new_title": "Art"})

    # sql = text("INSERT INTO subject(\"subject_id\") VALUES (:new_id)")
    # connection.execute(sql, {"new_id": "17"})
    # sql = text("INSERT INTO subject(\"subject_title\") VALUES (:new_title)")
    # connection.execute(sql, {"new_title": "Art"})

    transaction.commit()
    connection.close()


def test_update():
    """ Изменение строки: название предмета """
    connection = db.connect()
    transaction = connection.begin()

    sql = text("Update subject SET subject_title = :subject "
               "WHERE subject_id = :id")
    connection.execute(sql, {"subject": 'Painting', "id": 17})

    transaction.commit()
    connection.close()


def test_delete():
    """ Удаление строки через обнаружение по идентификатору """
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 17})

    transaction.commit()
    connection.close()
