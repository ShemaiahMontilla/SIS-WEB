from app import mysql


class Student(object):
    
    def __init__(self, school_id=None, first_name=None, last_name=None, course_code=None, year=None, gender=None):
        self.school_id = school_id
        self.first_name = first_name
        self.last_name = last_name
        self.course_code = course_code
        self.year = year
        self.gender =gender 

    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO student(school_id, first_name, last_name, course_code, year, gender) \
                VALUES('{self.school_id}','{self.first_name}','{self.last_name}','{self.course_code}', '{self.year}', '{self.gender}')" 

        cursor.execute(sql)
        mysql.connection.commit()
        return sql

    def edit(self, id_number):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE student SET first_name='{self.first_name}', last_name='{self.last_name}',course_code ='{self.course_code}', year = '{self.year}' , gender ='{self.gender}' WHERE school_id='{id_number}' " 
        cursor.execute(sql)
        mysql.connection.commit()
        
        
    @classmethod
    def open(cls, id_number):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from student where school_id = '{id_number}' "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def covert(cls, school_id):
        cursor = mysql.connection.cursor()

        sql = f"SELECT CONVERT({school_id}, CHAR)"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,school_id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from student where school_id= {school_id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

class college(object):
    
    def __init__(self, college_code= None, college_name = None):
        self.college_code = college_code
        self.college_name = college_name

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO college(college_code, name) \
                VALUES('{self.college_code}','{self.college_name}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    def edit(self, id):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE college SET name='{self.college_name}' WHERE college_code='{id}'" 
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def open(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from college where college_code = '{id}' "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,id_number):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from college where college_code= '{id_number}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

class course(object):

    def __init__(self, course_code = None, course_name = None, college_code = None):
        self.course_code = course_code
        self.course_name = course_name
        self.college_code = college_code

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO course(course_code, name, college_code) \
                VALUES('{self.course_code}','{self.course_name}','{self.college_code}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    def edit(self, course_code):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE course SET name='{self.course_name}', college_code = '{self.college_code}' WHERE course_code={course_code}"
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def open(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from course where course_code = '{id}' "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
        

    @classmethod
    def delete(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from course where course_code= '{id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False
