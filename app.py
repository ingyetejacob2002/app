import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the student_results DataFrame
student_results = pd.DataFrame(columns=["Name", "Math", "Science", "English", "Total Marks", "Average"])

@app.route('/')
def index():
    # Display the student results on the home page
    return render_template('index.html', results=student_results)

@app.route('/add_result', methods=['POST'])
def add_result():
    try:
        # Get data from the form
        name = request.form['name']
        math = int(request.form['math'])
        science = int(request.form['science'])
        english = int(request.form['english'])

        # Calculate total marks and average
        total_marks = math + science + english
        average = total_marks / 3

        # Create a new row of data as a dictionary
        new_data = {
            "Name": name,
            "Math": math,
            "Science": science,
            "English": english,
            "Total Marks": total_marks,
            "Average": average
        }

        # Use pd.concat() to append the new data row to the DataFrame
        global student_results
        student_results = pd.concat([student_results, pd.DataFrame([new_data])], ignore_index=True)

        # Return the updated results page
        return render_template('index.html', results=student_results)

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
