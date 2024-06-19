from models.__init__ import CURSOR, CONN

class Student:
    all = {}

    def __init__(self, name, age, gender, email, contact, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.contact = contact

    def __repr__(self):
        return f"<Student {self.id}: {self.name}, {self.age}, {self.gender}, {self.email}, {self.contact}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must not be an empty string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            raise ValueError("Age must be an integer")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and len(gender):
            self._gender = gender
        else:
            raise ValueError("Gender must not be an empty string")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email):
            self._email = email
        else:
            raise ValueError("Email must not be an empty string")

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        if isinstance(contact, str) and len(contact):
            self._contact = contact
        else:
            raise ValueError("Contact must not be an empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            email TEXT,
            contact TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS students;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO students (name, age, gender, email, contact)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.gender, self.email, self.contact))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age, gender, email, contact):
        student = cls(name, age, gender, email, contact)
        student.save()
        return student

    def update(self):
        sql = """
            UPDATE students
            SET name = ?, age = ?, gender = ?, email = ?, contact = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.gender, self.email, self.contact, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM students
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        student = cls.all.get(row[0])
        if student:
            student.name = row[1]
            student.age = row[2]
            student.gender = row[3]
            student.email = row[4]
            student.contact = row[5]
        else:
            student = cls(row[1], row[2], row[3], row[4], row[5])
            student.id = row[0]
            cls.all[student.id] = student
        return student

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM students
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM students
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM students
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
