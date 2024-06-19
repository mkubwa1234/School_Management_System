# lib/models/department.py
from models.__init__ import CURSOR, CONN

class Department:
    all = {}

    def __init__(self, name, location, head, id=None):
        self.id = id
        self.name = name
        self.location = location
        self.head = head

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}, {self.head}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string")

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        if isinstance(head, str) and len(head):
            self._head = head
        else:
            raise ValueError("Head must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            head TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO departments (name, location, head)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location, self.head))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location, head):
        department = cls(name, location, head)
        department.save()
        return department

    def update(self):
        sql = """
            UPDATE departments
            SET name = ?, location = ? , head = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.head, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        department = cls.all.get(row[0])
        if department:
            department.name = row[1]
            department.location = row[2]
            department.head = row[3]
        else:
            department = cls(row[1], row[2], row[3])
            department.id = row[0]
            cls.all[department.id] = department
        return department

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM departments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM departments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM departments
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def teachers(self):
        from models.teacher import Teacher
        sql = """
            SELECT * FROM teachers
            WHERE department_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Teacher.instance_from_db(row) for row in rows]
