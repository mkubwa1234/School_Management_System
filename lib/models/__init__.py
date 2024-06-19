# lib/models/__init__.py
import sqlite3

CONN = sqlite3.connect('school_database.db')
CURSOR = CONN.cursor()
