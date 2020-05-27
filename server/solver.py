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
        if equations[i][0] == '-' and equations[i][1].isalpha():
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
