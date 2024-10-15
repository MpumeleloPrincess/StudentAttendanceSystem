from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for students (can replace with database later)
students = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def registeration():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        student_number = request.form['student_number']
        
        # Add student data to in-memory list
        students.append({
            'name': name,
            'surname': surname,
            'student_number': student_number
        })

        # Redirect to home page after registration
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/view_students')
def view_students():
    return render_template('view_students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)





