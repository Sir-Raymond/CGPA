from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_cgpa', methods=['POST'])
def calculate_cgpa():
    if request.method == 'POST':
        num_courses = int(request.form['num_courses'])
        total_credit_points = 0
        total_units = 0
        
        for i in range(num_courses):
            course_unit_key = f'course_unit_{i+1}'
            grade_point_key = f'grade_point_{i+1}'
            
            if course_unit_key in request.form and grade_point_key in request.form \
                    and request.form[course_unit_key] != '' and request.form[grade_point_key] != '':
                course_unit = float(request.form[course_unit_key])
                grade_point = float(request.form[grade_point_key])
                total_credit_points += course_unit * grade_point
                total_units += course_unit
        
        if total_units == 0:
            return "No valid courses entered. Please ensure all fields are filled correctly."
        
        cgpa = total_credit_points / total_units
        return render_template('result.html', cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)
