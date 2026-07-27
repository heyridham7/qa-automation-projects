import sqlite3
import pytest

@pytest.fixture

def db():
    conn = sqlite3.connect(':memory:')
    cursor=conn.cursor()

    cursor.execute("""CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    status TEXT)
    """)

    cursor.execute("INSERT INTO users VALUES (1, 'ridham', 'ridham@test.com', 'active')")
    cursor.execute("INSERT INTO users VALUES (2, 'john', 'john@test.com', 'inactive')")
    cursor.execute("INSERT INTO users VALUES (3, 'alice', 'alice@test.com', 'active')")

    conn.commit()
    yield conn
    conn.close()

def test_user_exists(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username='ridham'")
    user = cursor.fetchone()
    assert user is not None 

def test_active_status(db):
    cursor=db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE status='active' ")
    user = cursor.fetchone()[0]
    assert user == 2

def test_user_mail(db):
    cursor = db.cursor()
    cursor.execute("SELECT email FROM users WHERE username = 'ridham'")
    email = cursor.fetchone()[0]
    assert email == 'ridham@test.com'

