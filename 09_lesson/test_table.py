from sqlalchemy import create_engine, inspect, text


db_connection_string =
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject_id'

def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO subject(\"subject_id\") VALUES (:new_id)")
    connection.execute(sql, {"new_id": "17"})
    sql = text("INSERT INTO subject(\"subject_title\") VALUES (:new_title)")
    connection.execute(sql, {"new_title": "Art"})

    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("Update subject SET subject_title = :subject WHERE subject_id = :17")
    connection.execute(sql, {"subject": 'Painting', "id": 17})

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE id = :id")
    connection.execute(sql, {"id": 17})

    transaction.commit()
    connection.close()