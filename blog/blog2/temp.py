import sqlite3
from db import init_db

init_db()

DB_NAME = "blog.db"
conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row




conn.executemany("""
    INSERT INTO sections (name, slug)
    VALUES (?, ?)
""", [
    ("Манікюр", "manicure"),
    ("Макіяж", "makeup"),
    ("Догляд за шкірою", "skincare"),
    ("Догляд за волоссям", "haircare"),
])

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def update_post(post_id, text, image, section_id):
    with get_db() as db:
        db.execute("""
            UPDATE posts
            SET text = ?, image = ?, section_id = ?
            WHERE id = ?
        """, (text, image, section_id, post_id))


def delete_post(post_id):
    with get_db() as db:
        db.execute("""
            DELETE FROM posts
            WHERE id = ?
        """, (post_id,))
        db.commit()

delete_post(16)



conn.commit()
conn.close()

