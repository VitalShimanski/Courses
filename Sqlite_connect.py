import sqlite3
_connection = None


def get_connection():
    global _connection
    if _connection is None:
        _connection = sqlite3.connect('anketa.db')
    return _connection


def init_db(force: bool = False):
    """ Проверить что нужные таблицы существуют, иначе создать их

        Важно: миграции на такие таблицы необходимо производить самостоятельно!

        :param force: явно пересоздать все таблицы
    """
    conn = get_connection()

    c = conn.cursor()

    # информация о пользователе
    # TODO: создать при необходимости...

    # сообщения от пользователей
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_message'(
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            text        TEXT NOT NULL
        )
    ''')
    # сохранить изменения
    conn.commit()


def add_message(user_id: int, text: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO user_message (user_id, text) VALUES (?, ?);", (user_id, text))
    conn.commit()


if __name__ == '__main__':
    init_db()

    add_message(user_id=1234, text='kekx')