from flask import Flask, render_template, request
from recommendation import generate_recommendation
from ai_optimizer import optimize_study_schedule

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    name = request.form['name']
    learning_style = request.form['learning_style']
    
    # Get performance metrics
    performance = {
        'math': int(request.form['math']),
        'science': int(request.form['science']),
        'history': int(request.form['history']),
    }

    # Get subjects and their study times
    subjects = request.form.getlist('subjects')
    study_times = request.form.getlist('study_times')

    # Generate recommendations and optimized schedule
    recommendation = generate_recommendation(learning_style, performance)
    schedule = optimize_study_schedule(subjects, study_times, performance)

    return render_template('plan.html', name=name, recommendation=recommendation, schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
