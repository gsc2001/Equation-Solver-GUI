from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, Regexp, Email
import validators as vl


class NumberForm(FlaskForm):
    '''
    Form for inputing number of equations
    '''
    number = IntegerField('No. of Equations:', validators=[DataRequired('Enter a integer please')])


def get_equationform(n):
    '''
    Function will return object of equation form
    '''
    class EquationForm(FlaskForm):
        '''
        Form for inputing Equation
        '''
        for i in range(n):
            locals()["Eqn"+str(i+1)] = StringField('EQUATION '+str(i+1) + ':',
                    validators=[DataRequired('Please Enter'),vl.check_decimal,vl.check_star,vl.check_equal_sign,
                    vl.check_equal_to_constant,vl.check_space,vl.check_single_var
                    ,vl.check_LHS_constant])

    form= EquationForm()
    return form
