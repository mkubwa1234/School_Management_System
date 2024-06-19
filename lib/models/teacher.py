from models.__init__ import CURSOR, CONN

class Teacher:
    all = {}

    def __init__(self, name, gender, subject, email, department_id, department, id=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.subject = subject
        self.email = email
        self.department_id = department_id
        self.department = department

    def __repr__(self):
        return f"<Teacher {self.id}: {self.name}, {self.gender}, {self.subject}, {self.email}, {self.department_id}, {self.department}>"

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
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and len(gender):
            self._gender = gender
        else:
            raise ValueError("Gender must not be an empty string")

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if isinstance(subject, str) and len(subject):
            self._subject = subject
        else:
            raise ValueError("Subject must not be an empty string")

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
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        if isinstance(department_id, int):
            self._department_id = department_id
        else:
            raise ValueError("Department ID must be an integer")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        if isinstance(department, str) and len(department):
            self._department = department
        else:
            raise ValueError("Department must not be an empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            gender TEXT,
            subject TEXT,
            email TEXT,
            department_id INTEGER,
            department TEXT,
            FOREIGN KEY (department_id) REFERENCES departments(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS teachers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO teachers (name, gender, subject, email, department_id, department)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.gender, self.subject, self.email, self.department_id, self.department))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, gender, subject, email, department_id, department):
        teacher = cls(name, gender, subject, email, department_id, department)
        teacher.save()
        return teacher

    def update(self):
        sql = """
            UPDATE teachers
            SET name = ?, gender = ?, subject = ?, email = ?, department_id = ?, department = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.gender, self.subject, self.email, self.department_id, self.department, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM teachers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        teacher = cls.all.get(row[0])
        if teacher:
            teacher.name = row[1]
            teacher.gender = row[2]
            teacher.subject = row[3]
            teacher.email = row[4]
            teacher.department_id = row[5]
            teacher.department = row[6]
        else:
            teacher = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            teacher.id = row[0]
            cls.all[teacher.id] = teacher
        return teacher

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM teachers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM teachers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM teachers
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def department(self):
        from models.department import Department
        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.department_id,))
        row = CURSOR.fetchone()
        return Department.instance_from_db(row) if row else None