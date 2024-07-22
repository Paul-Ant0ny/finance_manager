from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        profession = request.form['profession']
        salary = float(request.form['salary'])

        if profession and salary > 0:
            housing_cost, transportation_cost, food_cost, healthcare_cost, debt_repayment_cost, savings_cost, discretionary_cost, remaining_savings = 0, 0, 0, 0, 0, 0, 0, 0

            if profession in ["doctor", "architect", "software-developer"]:
                housing_cost = salary * 0.25
            elif profession in ["journalist", "teacher"]:
                housing_cost = salary * 0.20
            else:
                housing_cost = salary * 0.17

            if profession in ["engineer", "nurse", "doctor"]:
                transportation_cost = salary * 0.125
            elif profession in ["architect", "teacher", "lawyer"]:
                transportation_cost = salary * 0.083
            else:
                transportation_cost = salary * 0.10

            if profession in ["journalist", "architect"]:
                food_cost = salary * 0.20
            elif profession in ["pharmacist", "teacher"]:
                food_cost = salary * 0.125
            else:
                food_cost = salary * 0.17

            if profession in ["doctor", "engineer", "lawyer"]:
                healthcare_cost = salary * 0.125
            elif profession in ["teacher", "nurse"]:
                healthcare_cost = salary * 0.10
            else:
                healthcare_cost = salary * 0.11

            if profession in ["pharmacist", "lawyer", "software-developer"]:
                debt_repayment_cost = salary * 0.17
            elif profession in ["teacher", "nurse", "architect"]:
                debt_repayment_cost = salary * 0.067
            else:
                debt_repayment_cost = salary * 0.083

            savings_cost = salary * 0.10
            discretionary_cost = salary * 0.15

            remaining_savings = salary - (housing_cost + transportation_cost + food_cost + healthcare_cost + debt_repayment_cost + savings_cost + discretionary_cost)

            return render_template('index.html', profession=profession, salary=salary, housing_cost=housing_cost, transportation_cost=transportation_cost, food_cost=food_cost, healthcare_cost=healthcare_cost, debt_repayment_cost=debt_repayment_cost, savings_cost=savings_cost, discretionary_cost=discretionary_cost, remaining_savings=remaining_savings)
        else:
            return render_template('index.html', error='Please enter a valid profession and salary.')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)