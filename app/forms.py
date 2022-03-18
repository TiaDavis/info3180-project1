from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email

class AddProperty(FlaskForm):
    propertytitle = StringField("Property Title", validators=[DataRequired()])
    numberofrooms = StringField("No. of Rooms", validators=[DataRequired()])
    numberofbathrooms = StringField("No. of Bathrooms", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()], render_kw={"rows": "3"})
    Type = SelectField("Property Type", choices=['House', 'Apartment'])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Illegal file.')])