from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsh",
    database="harsh1"
)
cursor = db.cursor()

# Route to show the form
@app.route('/')

def form():
    
    return render_template('registration.html')

# Route to handle form data
@app.route('/submit', methods=['POST'])

def submit():
    print("h")
    
    name = request.form['name']
    email = request.form['email']

    

    sql = "INSERT INTO registraions (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)
    db.commit()

    return "Data added to database!"

if __name__ == '__main__':
    app.run(debug=True)
