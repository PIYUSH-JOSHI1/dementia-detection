from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from functools import wraps
import csv
import os
from datetime import datetime
import json

app = Flask(__name__)

# Configure app for production
app.secret_key = os.environ.get('SECRET_KEY', 'dementia_detection_secret_key_2025')

# For production, disable debug mode
app.config['DEBUG'] = os.environ.get('FLASK_ENV') != 'production'

# CSV file paths
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
USERS_CSV = os.path.join(DATA_DIR, 'users.csv')
PATIENTS_CSV = os.path.join(DATA_DIR, 'patients.csv')
TEST_RESULTS_CSV = os.path.join(DATA_DIR, 'test_results.csv')
COGNITIVE_TESTS_CSV = os.path.join(DATA_DIR, 'cognitive_tests.csv')
SPEECH_ANALYSIS_CSV = os.path.join(DATA_DIR, 'speech_analysis.csv')

# Default credentials for quick login
DEFAULT_DOCTOR = {'email': 'doctor@demo.com', 'password': 'doctor123', 'role': 'doctor', 'name': 'Dr. Smith'}
DEFAULT_PATIENT = {'email': 'patient@demo.com', 'password': 'patient123', 'role': 'patient', 'name': 'John Doe', 'patient_id': 'P001'}

# Initialize CSV files if they don't exist
def init_csv_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Users CSV
    if not os.path.exists(USERS_CSV):
        with open(USERS_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['email', 'password', 'role', 'name', 'patient_id', 'created_at'])
            writer.writerow([DEFAULT_DOCTOR['email'], DEFAULT_DOCTOR['password'], 'doctor', DEFAULT_DOCTOR['name'], '', datetime.now().isoformat()])
            writer.writerow([DEFAULT_PATIENT['email'], DEFAULT_PATIENT['password'], 'patient', DEFAULT_PATIENT['name'], DEFAULT_PATIENT['patient_id'], datetime.now().isoformat()])
    
    # Patients CSV
    if not os.path.exists(PATIENTS_CSV):
        with open(PATIENTS_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['patient_id', 'name', 'age', 'gender', 'email', 'baseline_score', 'last_test_date', 'risk_level'])
            writer.writerow(['P001', 'John Doe', '68', 'Male', 'patient@demo.com', '85', '', 'Low'])
    
    # Test Results CSV
    if not os.path.exists(TEST_RESULTS_CSV):
        with open(TEST_RESULTS_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['test_id', 'patient_id', 'test_type', 'score', 'risk_score', 'timestamp', 'details'])
    
    # Cognitive Tests CSV
    if not os.path.exists(COGNITIVE_TESTS_CSV):
        with open(COGNITIVE_TESTS_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['test_id', 'patient_id', 'memory_score', 'attention_score', 'language_score', 'executive_score', 'total_score', 'timestamp'])
    
    # Speech Analysis CSV
    if not os.path.exists(SPEECH_ANALYSIS_CSV):
        with open(SPEECH_ANALYSIS_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['analysis_id', 'patient_id', 'fluency_score', 'coherence_score', 'vocabulary_score', 'pause_analysis', 'total_score', 'timestamp'])

init_csv_files()

# Helper functions
def read_csv(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    return data

def write_csv(filename, data, fieldnames):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def append_csv(filename, row):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# Authentication decorator
def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user' not in session:
                return redirect(url_for('login'))
            if role and session.get('role') != role:
                flash('Access denied. Insufficient permissions.', 'error')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Routes
@app.route('/')
def index():
    if 'user' in session:
        if session['role'] == 'doctor':
            return redirect(url_for('doctor_dashboard'))
        else:
            return redirect(url_for('patient_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        users = read_csv(USERS_CSV)
        user = next((u for u in users if u['email'] == email and u['password'] == password), None)
        
        if user:
            session['user'] = user['email']
            session['role'] = user['role']
            session['name'] = user['name']
            session['patient_id'] = user.get('patient_id', '')
            
            if user['role'] == 'doctor':
                return redirect(url_for('doctor_dashboard'))
            else:
                return redirect(url_for('patient_dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
    
    return render_template('login.html', default_doctor=DEFAULT_DOCTOR, default_patient=DEFAULT_PATIENT)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        age = request.form.get('age')
        gender = request.form.get('gender')
        
        # Validation
        if not all([name, email, password, confirm_password, age, gender]):
            flash('All fields are required.', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return render_template('register.html')
        
        try:
            age = int(age)
            if age < 18 or age > 120:
                flash('Please enter a valid age between 18 and 120.', 'error')
                return render_template('register.html')
        except ValueError:
            flash('Please enter a valid age.', 'error')
            return render_template('register.html')
        
        # Check if email already exists
        users = read_csv(USERS_CSV)
        if any(u['email'] == email for u in users):
            flash('Email already registered. Please use a different email.', 'error')
            return render_template('register.html')
        
        # Generate unique patient ID
        patients = read_csv(PATIENTS_CSV)
        patient_count = len(patients) + 1
        patient_id = f"P{patient_count:03d}"
        
        # Ensure patient ID is unique
        while any(p['patient_id'] == patient_id for p in patients):
            patient_count += 1
            patient_id = f"P{patient_count:03d}"
        
        # Add user to users CSV
        timestamp = datetime.now().isoformat()
        append_csv(USERS_CSV, [email, password, 'patient', name, patient_id, timestamp])
        
        # Add patient to patients CSV
        baseline_score = 85  # Default baseline score
        append_csv(PATIENTS_CSV, [patient_id, name, str(age), gender, email, str(baseline_score), '', 'Low'])
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/patient/dashboard')
@login_required(role='patient')
def patient_dashboard():
    patient_id = session.get('patient_id')
    patients = read_csv(PATIENTS_CSV)
    patient = next((p for p in patients if p['patient_id'] == patient_id), None)
    
    test_results = read_csv(TEST_RESULTS_CSV)
    patient_tests = [t for t in test_results if t['patient_id'] == patient_id]
    
    return render_template('patient_dashboard.html', patient=patient, tests=patient_tests)

@app.route('/doctor/dashboard')
@login_required(role='doctor')
def doctor_dashboard():
    patients = read_csv(PATIENTS_CSV)
    test_results = read_csv(TEST_RESULTS_CSV)
    
    # Enhance patient data with latest test scores
    enhanced_patients = []
    for patient in patients:
        patient_tests = [t for t in test_results if t['patient_id'] == patient['patient_id']]
        patient_copy = patient.copy()
        
        if patient_tests:
            # Sort by timestamp to get latest test
            patient_tests.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
            latest_test = patient_tests[0]
            patient_copy['latest_score'] = latest_test.get('score', 'N/A')
            patient_copy['latest_test_type'] = latest_test.get('test_type', 'N/A')
            patient_copy['latest_risk_score'] = latest_test.get('risk_score', 'N/A')
            patient_copy['total_tests'] = len(patient_tests)
            
            # Calculate average score
            valid_scores = [float(t['score']) for t in patient_tests if t.get('score') and t['score'].replace('.', '').isdigit()]
            patient_copy['average_score'] = sum(valid_scores) / len(valid_scores) if valid_scores else 'N/A'
        else:
            patient_copy['latest_score'] = 'No tests'
            patient_copy['latest_test_type'] = 'N/A'
            patient_copy['latest_risk_score'] = 'N/A'
            patient_copy['total_tests'] = 0
            patient_copy['average_score'] = 'N/A'
        
        enhanced_patients.append(patient_copy)
    
    # Calculate statistics
    total_patients = len(patients)
    high_risk = len([p for p in patients if p.get('risk_level') == 'High'])
    medium_risk = len([p for p in patients if p.get('risk_level') == 'Medium'])
    low_risk = len([p for p in patients if p.get('risk_level') == 'Low'])
    recent_tests = len([t for t in test_results if t.get('timestamp', '').startswith(datetime.now().strftime('%Y-%m-%d'))])
    total_tests = len(test_results)
    
    # Recent activity - tests from last 7 days
    from datetime import timedelta
    week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    recent_activity = [t for t in test_results if t.get('timestamp', '') >= week_ago]
    
    return render_template('doctor_dashboard.html', 
                         patients=enhanced_patients, 
                         total_patients=total_patients,
                         high_risk=high_risk,
                         medium_risk=medium_risk,
                         low_risk=low_risk,
                         recent_tests=recent_tests,
                         total_tests=total_tests,
                         recent_activity=recent_activity)

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'dementia-detection-app'
    })

@app.route('/api/patient-summary/<patient_id>')
@login_required(role='doctor')
def patient_summary_api(patient_id):
    patients = read_csv(PATIENTS_CSV)
    test_results = read_csv(TEST_RESULTS_CSV)
    
    patient = next((p for p in patients if p['patient_id'] == patient_id), None)
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404
    
    # Get patient tests
    patient_tests = [t for t in test_results if t['patient_id'] == patient_id]
    
    # Calculate enhanced data
    if patient_tests:
        patient_tests.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        latest_test = patient_tests[0]
        
        valid_scores = [float(t['score']) for t in patient_tests if t.get('score') and t['score'].replace('.', '').isdigit()]
        average_score = sum(valid_scores) / len(valid_scores) if valid_scores else None
        
        summary_data = {
            'patient_info': patient,
            'latest_score': latest_test.get('score'),
            'latest_test_type': latest_test.get('test_type'),
            'latest_risk_score': latest_test.get('risk_score'),
            'total_tests': len(patient_tests),
            'average_score': average_score,
            'test_history': patient_tests[:5]  # Last 5 tests
        }
    else:
        summary_data = {
            'patient_info': patient,
            'latest_score': None,
            'latest_test_type': None,
            'latest_risk_score': None,
            'total_tests': 0,
            'average_score': None,
            'test_history': []
        }
    
    return jsonify(summary_data)

@app.route('/patient/cognitive-test')
@login_required(role='patient')
def cognitive_test():
    return render_template('cognitive_test.html')

@app.route('/patient/memory-test')
@login_required(role='patient')
def memory_test():
    return render_template('memory_test.html')

@app.route('/patient/speech-analysis')
@login_required(role='patient')
def speech_analysis():
    return render_template('speech_analysis.html')

@app.route('/patient/verbal-fluency')
@login_required(role='patient')
def verbal_fluency():
    return render_template('verbal_fluency.html')

@app.route('/api/submit-cognitive-test', methods=['POST'])
@login_required(role='patient')
def submit_cognitive_test():
    data = request.json
    patient_id = session.get('patient_id')
    
    test_id = f"CT{datetime.now().strftime('%Y%m%d%H%M%S')}"
    timestamp = datetime.now().isoformat()
    
    # Calculate scores
    memory_score = int(data.get('memory_score', 0))
    attention_score = int(data.get('attention_score', 0))
    language_score = int(data.get('language_score', 0))
    executive_score = int(data.get('executive_score', 0))
    total_score = (memory_score + attention_score + language_score + executive_score) / 4
    
    # Append to cognitive tests CSV
    append_csv(COGNITIVE_TESTS_CSV, [test_id, patient_id, memory_score, attention_score, 
                                     language_score, executive_score, total_score, timestamp])
    
    # Calculate risk score
    risk_score = 100 - total_score
    risk_level = 'Low' if risk_score < 30 else 'Medium' if risk_score < 60 else 'High'
    
    # Append to test results CSV
    details = json.dumps({'memory': memory_score, 'attention': attention_score, 
                         'language': language_score, 'executive': executive_score})
    append_csv(TEST_RESULTS_CSV, [test_id, patient_id, 'Cognitive', total_score, 
                                  risk_score, timestamp, details])
    
    # Update patient risk level
    patients = read_csv(PATIENTS_CSV)
    for patient in patients:
        if patient['patient_id'] == patient_id:
            patient['risk_level'] = risk_level
            patient['last_test_date'] = timestamp
    write_csv(PATIENTS_CSV, patients, ['patient_id', 'name', 'age', 'gender', 'email', 
                                       'baseline_score', 'last_test_date', 'risk_level'])
    
    return jsonify({'success': True, 'total_score': total_score, 'risk_score': risk_score, 
                   'risk_level': risk_level})

@app.route('/api/submit-memory-test', methods=['POST'])
@login_required(role='patient')
def submit_memory_test():
    data = request.json
    patient_id = session.get('patient_id')
    
    test_id = f"MT{datetime.now().strftime('%Y%m%d%H%M%S')}"
    timestamp = datetime.now().isoformat()
    
    correct_recalls = int(data.get('correct_recalls', 0))
    false_recalls = int(data.get('false_recalls', 0))
    total_words = int(data.get('total_words', 10))
    memory_score = float(data.get('memory_score', 0))
    
    # Calculate risk score
    risk_score = 100 - memory_score
    risk_level = 'Low' if risk_score < 30 else 'Medium' if risk_score < 60 else 'High'
    
    # Append to test results CSV
    details = json.dumps({
        'correct_recalls': correct_recalls,
        'false_recalls': false_recalls,
        'total_words': total_words,
        'recall_rate': (correct_recalls / total_words * 100) if total_words > 0 else 0
    })
    append_csv(TEST_RESULTS_CSV, [test_id, patient_id, 'Memory', memory_score,
                                  risk_score, timestamp, details])
    
    # Update patient risk level
    patients = read_csv(PATIENTS_CSV)
    for patient in patients:
        if patient['patient_id'] == patient_id:
            patient['risk_level'] = risk_level
            patient['last_test_date'] = timestamp
    write_csv(PATIENTS_CSV, patients, ['patient_id', 'name', 'age', 'gender', 'email',
                                       'baseline_score', 'last_test_date', 'risk_level'])
    
    return jsonify({'success': True, 'memory_score': memory_score, 'risk_score': risk_score,
                   'risk_level': risk_level})

@app.route('/api/submit-speech-analysis', methods=['POST'])
@login_required(role='patient')
def submit_speech_analysis():
    data = request.json
    patient_id = session.get('patient_id')
    
    analysis_id = f"SA{datetime.now().strftime('%Y%m%d%H%M%S')}"
    timestamp = datetime.now().isoformat()
    
    # Calculate scores
    fluency_score = int(data.get('fluency_score', 0))
    coherence_score = int(data.get('coherence_score', 0))
    vocabulary_score = int(data.get('vocabulary_score', 0))
    pause_analysis = data.get('pause_analysis', 'Normal')
    total_score = (fluency_score + coherence_score + vocabulary_score) / 3
    
    # Append to speech analysis CSV
    append_csv(SPEECH_ANALYSIS_CSV, [analysis_id, patient_id, fluency_score, coherence_score,
                                     vocabulary_score, pause_analysis, total_score, timestamp])
    
    # Calculate risk score
    risk_score = 100 - total_score
    risk_level = 'Low' if risk_score < 30 else 'Medium' if risk_score < 60 else 'High'
    
    # Append to test results CSV
    details = json.dumps({'fluency': fluency_score, 'coherence': coherence_score,
                         'vocabulary': vocabulary_score, 'pauses': pause_analysis})
    append_csv(TEST_RESULTS_CSV, [analysis_id, patient_id, 'Speech', total_score,
                                  risk_score, timestamp, details])
    
    return jsonify({'success': True, 'total_score': total_score, 'risk_score': risk_score,
                   'risk_level': risk_level})

@app.route('/api/submit-verbal-fluency', methods=['POST'])
@login_required(role='patient')
def submit_verbal_fluency():
    data = request.json
    patient_id = session.get('patient_id')
    
    test_id = f"VF{datetime.now().strftime('%Y%m%d%H%M%S')}"
    timestamp = datetime.now().isoformat()
    
    total_words = int(data.get('total_words', 0))
    average_score = float(data.get('average_score', 0))
    category_results = data.get('category_results', [])
    
    # Calculate risk score
    risk_score = 100 - average_score
    risk_level = 'Low' if risk_score < 30 else 'Medium' if risk_score < 60 else 'High'
    
    # Append to test results CSV
    details = json.dumps({
        'total_words': total_words,
        'categories': category_results
    })
    append_csv(TEST_RESULTS_CSV, [test_id, patient_id, 'Verbal Fluency', average_score,
                                  risk_score, timestamp, details])
    
    # Update patient risk level
    patients = read_csv(PATIENTS_CSV)
    for patient in patients:
        if patient['patient_id'] == patient_id:
            patient['risk_level'] = risk_level
            patient['last_test_date'] = timestamp
    write_csv(PATIENTS_CSV, patients, ['patient_id', 'name', 'age', 'gender', 'email',
                                       'baseline_score', 'last_test_date', 'risk_level'])
    
    return jsonify({'success': True, 'average_score': average_score, 'risk_score': risk_score,
                   'risk_level': risk_level})

@app.route('/doctor/patient/<patient_id>')
@login_required(role='doctor')
def patient_details(patient_id):
    patients = read_csv(PATIENTS_CSV)
    patient = next((p for p in patients if p['patient_id'] == patient_id), None)
    
    if not patient:
        flash('Patient not found.', 'error')
        return redirect(url_for('doctor_dashboard'))
    
    test_results = read_csv(TEST_RESULTS_CSV)
    patient_tests = [t for t in test_results if t['patient_id'] == patient_id]
    
    cognitive_tests = read_csv(COGNITIVE_TESTS_CSV)
    patient_cognitive = [t for t in cognitive_tests if t['patient_id'] == patient_id]
    
    speech_analyses = read_csv(SPEECH_ANALYSIS_CSV)
    patient_speech = [t for t in speech_analyses if t['patient_id'] == patient_id]
    
    return render_template('patient_details.html', 
                         patient=patient,
                         test_results=patient_tests,
                         cognitive_tests=patient_cognitive,
                         speech_analyses=patient_speech)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
