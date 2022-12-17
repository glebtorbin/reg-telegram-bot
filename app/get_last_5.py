from sqlalchemy import create_engine

ENGINE = create_engine('sqlite:///sqlite.db')

def get_last_5():
    last_5 = []
    query = ENGINE.execute('SELECT * FROM user ORDER BY id DESC LIMIT 5')
    for i in query:
        role_name = ENGINE.execute(f'SELECT * FROM roles WHERE id={i.id_role}')
        for r in role_name:
            list = [i.fio, i.datar, r.name]
            last_5.append(list)
    return last_5


