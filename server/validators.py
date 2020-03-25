from wtforms.validators import ValidationError
import re
def check_decimal(form,field):
    if '.' in field.data:
        raise ValidationError('No decimal allowed')

def check_LHS_constant(form,field):
    if re.search('\d+[+\-*\/=]',field.data):
        raise ValidationError('LHS should not contain any constant')

def check_single_var(form,field):
    input = field.data
    for i in range(1, len(input)):
        if input[i].isalpha():
            if input[i - 1].isalpha():
                raise ValidationError('Only Single Character variable allowed')
                break


def check_equal_sign(form,field):
    input  = field.data
    if input.count('=') != 1:
        raise ValidationError('Equation should have exacltly on equal to sign')


def check_space(form, field):
    input = field.data
    if ' ' in input:
        raise ValidationError('No spaces allowed')


def check_star(form,field):
    input = field.data
    if '*' in input:
        raise ValidationError('No stars allowed inside equations')


def check_equal_to_constant(form,field):
    input = field.data
    flag = int()
    for i in range(len(input)):
        if input[i] == '=':
            flag = i
            break
    for i in range(flag + 1, len(input)):
        if not input[i].isdigit():
            raise ValidationError('RHS should only be a +ve constant')
            break
