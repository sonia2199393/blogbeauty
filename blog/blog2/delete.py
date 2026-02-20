import sqlite3


DB_NAME = "blog.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def update_post(post_id, section_id): #функція для зміни поста. ВОна знаходить пост за ІД, змінює section_id. Якщо тобі потрібно змінити якесь інше поле, то зміни section_id на інше поле. Можна змінювати значення декілька полів
    with get_db() as db:
        db.execute("""
            UPDATE posts
            SET section_id = ?
            WHERE id = ?
        """, (section_id, post_id))


def delete_post(post_id):  # функція для видалення поста, потрібно передати лише ід поста для його видалення
    with get_db() as db:
        db.execute("""
            DELETE FROM posts
            WHERE id = ?
        """, (post_id,))

delete_post(16)  # приклад використання функції для видалення поста (видалить пост із ІД 16)
