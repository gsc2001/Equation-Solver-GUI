from base.equation_solver_base import *

def get_eqns():
    n = int(input("Enter no. of eqns"))
    equations = []
    for i in range(n):
        equation_input = input("Enter {} equation".format(i + 1))
        equations.append((equation_input))
    return equations


def convert_equations(equations):
    for i in range(len(equations)):
        if equations[i][0] == '-':
            equations[i] = '-1' + equations[i][1:]
    print(equations)
    eqs_converted = "_".join(equations)
    eqs_converted = str(len(equations)) + "_" + eqs_converted

    return eqs_converted


def solve_equation(compressed):
    solution = ()
    try:
        solution = solve(compressed)
    except:
        print('Error while solving equation __ try agin please')
    return solution


def get_solution(equations=None):
    if equations == None:
        equations = get_eqns()

    compressed_equation = convert_equations(equations)
    return solve_equation(compressed_equation)




def validata_warn(equations, warnings):
    f = True
    # print(len(equations), len(warnings))

    for i in range(len(equations)):
        equation = equations[i]
        if equation == "":
            warnings[i].set("Can't be empty")
            f = False
            continue
        if check_single_var(equation):
            warnings[i].set('Only single char var allowed')
            f = False
            continue
        if check_decimal(equation):
            warnings[i].set('Decimal point not allowed')
            f = False
            continue
        if check_space(equation):
            warnings[i].set('Spaces not allowed')
            f = False
            continue
        if check_star(equation):
            warnings[i].set('Star not allowed')
            f = False
            continue
        if not check_equal_sign(equation):
            warnings[i].set('Exactly 1 equal sign required')
            f = False
            continue
        if not check_equal_to_constant(equation):
            warnings[i].set("RHS only +ve constant (without '+')")
            f = False
            continue
        warnings[i].set('')
    return f
