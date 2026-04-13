from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtform.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField('Task Name',validators=[DataRequired()])
    desc = StringField('yask desc',validators=[DataRequired()])
    submit = SubmitField('submit')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete Task')