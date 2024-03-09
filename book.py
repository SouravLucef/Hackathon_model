from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['fname']
    email = request.form['email_id']
    date = request.form['edate']
    time = request.form['appt']
    address = request.form['address']
    
    # Process the data as needed
    # For now, just print it
    print("Name:", name)
    print("Email:", email)
    print("Date:", date)
    print("Time:", time)
    print("Address:", address)

    # You can return a response if needed
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
