from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, SelectField, RadioField


class StudentForm(FlaskForm):
    id = StringField ('ID Number', [validators.DataRequired(), validators.Length(min=9, max=9)])
    first_name = StringField('First Name', [validators.DataRequired(), validators.Length(min=3)])
    last_name = StringField('Last Name', [validators.DataRequired(), validators.Length(min=3)])
    course_code = SelectField('Course', [validators.DataRequired()], choices = ['AB PolSci','BSA','BSCA','BSCE','BSCS','BSEE', 'BSIS', 'BSIT', 'BSStat'])
    year = SelectField('Year', [validators.DataRequired()], choices = ['1','2','3','4','5','Irregular'])
    gender = RadioField('Gender', [validators.DataRequired()], choices = ['Female', 'Male'])
    submit = SubmitField("Submit")

class CourseForm(FlaskForm):
    course_code = StringField ('Course Code', [validators.DataRequired()])
    course_name = StringField('Course Name', [validators.DataRequired()])
    college_code = SelectField('College Code', [validators.DataRequired()], choices = ['CASS','CBAA','CCS','CED','CET', 'CON', 'CSM'])
    submit = SubmitField("Submit")

class CollegeForm(FlaskForm):
    college_code = StringField ('College Code', [validators.DataRequired()])
    college_name = StringField('College Name', [validators.DataRequired()])
    submit = SubmitField("Submit")