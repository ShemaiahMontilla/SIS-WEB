from flask import render_template, redirect, request, jsonify, flash
from . import student_bp
import app.models as models
from app.student.forms import StudentForm, CourseForm, CollegeForm
from app import mysql

@student_bp.route('/')
@student_bp.route('/student')
@student_bp.route('/index')
def index():
    student = models.Student.all()
    return render_template('index.html', data=student,title='Home',something='something')

@student_bp.route('/course')
def course():
    course = models.course.all()
    return render_template('course.html', data=course,title='Home',something='something')

@student_bp.route('/college')
def college():
    college = models.college.all()
    return render_template('college.html', data=college,title='Home',something='something')

@student_bp.route('/student/add_student', methods=['POST','GET'])
def add_student():
    form = StudentForm(request.form)
    if request.method == 'POST' and form.validate():
        student = models.Student(school_id=form.id.data, first_name=form.first_name.data, last_name=form.last_name.data, course_code=form.course_code.data, year = form.year.data, gender = form.gender.data)
        student.add()
        return redirect('/student')
    else:
        return render_template('add_student.html', form=form)

@student_bp.route('/course/add_course', methods=['POST','GET'])
def add_course():
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        course = models.course(course_code=form.course_code.data, course_name=form.course_name.data, college_code=form.college_code.data)
        course.add()
        return redirect('/course')
    else:
        return render_template('add_course.html', form=form)

@student_bp.route('/college/add_college', methods=['POST','GET'])
def add_college():
    form = CollegeForm(request.form)
    if request.method == 'POST' and form.validate():
        college = models.college(college_code=form.college_code.data, college_name=form.college_name.data)
        college.add()
        return redirect('/college')
    else:
        return render_template('add_college.html', form=form)


@student_bp.route('/student/edit/<id_number>', methods=['POST','GET'])
def edit(id_number):
    form = StudentForm(request.form)
    details = models.Student.open(id_number)
    if request.method == 'GET':
        form.id.data = details[0][0]    
        form.first_name.data = details[0][1]
        form.last_name.data = details[0][2]
        form.course_code.data = details[0][3]
        form.year.data = details[0][4]
        form.gender.data = details[0][5]
    
        return render_template('edit_student.html', 
                            title = 'Update Student', 
                            id_number=id_number,
                            form=form)
    
    elif request.method == 'POST' and form.validate():
        student = models.Student( first_name = form.first_name.data, last_name = form.last_name.data,course_code = form.course_code.data,  year  =form.year.data, gender = form.gender.data)
        student.edit(id_number)  
        flash('Student info has been updated!')
        return redirect('/student')

@student_bp.route("/student/delete/<string:school_id>", methods=['GET','POST'])
def delete(school_id):
    cursor = mysql.connection.cursor()
    sql = f"DELETE from `student` where `student`.`school_id`= '{school_id}'"
    cursor.execute(sql)
    mysql.connection.commit()
    flash("Slot Deleted Successful","danger")
    return redirect('student')
    
    
            
            
            
            
 

@student_bp.route("/course/delete", methods=["POST"])
def delete_course():
    course_code = request.form['course_code']
    if models.course.delete(course_code):
        return jsonify(success=True,message="Successfully deleted")
    else:
        return jsonify(success=False,message="Failed")  
       