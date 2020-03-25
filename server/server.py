from flask import Flask, render_template, redirect, url_for, jsonify
from solver import get_solution
from forms import get_equationform, NumberForm

# init app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'

# route to get number of equations
@app.route('/input_n', methods=['GET', 'post'])
def input_n():
    '''
    Get number of equations
    '''
    n_form = NumberForm()
    if n_form.validate_on_submit():
        n = n_form['number'].data
        return redirect(url_for('input_equations', n=n))
    return render_template('input_n.html', n_form=n_form, back=False)

solution = []

@app.route('/input_eqautions/<n>', methods=['GET', 'POST'])
def input_equations(n):
    '''
    Get equations and store solution
    '''
    global solution
    n = int(n)
    eq_form = get_equationform(n)
    if eq_form.validate_on_submit():
        equations = []
        for i in range(n):
            equations.append(eq_form['Eqn'+str(i+1)].data)
        solution = get_solution(equations)
        # sol = dict(solution)
        # solution_json = jsonify(sol)
        # return solution_json
        return render_template('input_eq.html',eq_form=eq_form,back=True,solved=True,solution=solution)

    return render_template('input_eq.html', eq_form=eq_form,solved=False,back=True)



if __name__ == '__main__':
    app.run(debug=True)
