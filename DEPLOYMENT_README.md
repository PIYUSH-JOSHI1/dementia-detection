# 🧠 Dementia Detection System

An AI-powered early detection system for dementia using cognitive assessments, memory tests, and speech analysis.

## Features

- **Patient Registration & Management**: Secure patient registration with profile management
- **Multiple Assessment Types**:
  - Cognitive Assessment (memory, attention, language, executive function)
  - Memory Tests (word recall and recognition)
  - Speech Analysis (fluency, coherence, vocabulary)
  - Verbal Fluency Tests
- **Interactive Dashboards**:
  - Patient dashboard with progress tracking and detailed test results
  - Doctor dashboard with patient overview and risk assessment
- **Enhanced Test Details**: Comprehensive test result analysis with recommendations
- **Progress Visualization**: Charts and graphs showing cognitive health trends
- **Risk Assessment**: Automated risk level calculation and alerts

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Charts**: Chart.js
- **Data Storage**: CSV files
- **Deployment**: Render

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dementia-detection-flask
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

### Default Login Credentials

**Doctor Account:**
- Email: doctor@demo.com
- Password: doctor123

**Patient Account:**
- Email: patient@demo.com
- Password: patient123

## Deployment on Render

### Step-by-Step Deployment Instructions

1. **Prepare Your Repository**:
   - Push your code to GitHub
   - Ensure all required files are present (see files list below)

2. **Create Render Account**:
   - Go to [render.com](https://render.com)
   - Sign up for a free account
   - Connect your GitHub account

3. **Deploy the Application**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: dementia-detection-app
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free

4. **Environment Variables** (Optional):
   - Add `FLASK_ENV=production`
   - Add `SECRET_KEY` (Render can auto-generate this)

5. **Deploy**:
   - Click "Create Web Service"
   - Wait for deployment to complete (5-10 minutes)

### Required Files for Deployment

- `requirements.txt` - Python dependencies
- `Procfile` - Process file for web server
- `runtime.txt` - Python version specification
- `render.yaml` - Render configuration (optional)
- `app.py` - Main application file
- `templates/` - HTML templates
- `static/` - CSS, JS, and image files
- `data/` - CSV data files

### Post-Deployment

1. **Test the Application**:
   - Visit your Render app URL
   - Test registration functionality
   - Test login with demo credentials
   - Verify dashboard functionality

2. **Monitor**:
   - Check Render dashboard for logs
   - Monitor application performance
   - Set up health checks if needed

## File Structure

```
dementia-detection-flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Render process configuration
├── runtime.txt           # Python version
├── render.yaml           # Render service configuration
├── data/                 # CSV data files
│   ├── users.csv
│   ├── patients.csv
│   ├── test_results.csv
│   ├── cognitive_tests.csv
│   └── speech_analysis.csv
├── templates/            # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── patient_dashboard.html
│   ├── doctor_dashboard.html
│   ├── cognitive_test.html
│   ├── memory_test.html
│   ├── speech_analysis.html
│   ├── verbal_fluency.html
│   └── patient_details.html
└── static/              # Static files
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

## API Endpoints

- `GET /` - Home page (redirects to appropriate dashboard)
- `GET/POST /login` - User authentication
- `GET/POST /register` - Patient registration
- `GET /logout` - User logout
- `GET /patient/dashboard` - Patient dashboard
- `GET /doctor/dashboard` - Doctor dashboard
- `GET /patient/cognitive-test` - Cognitive assessment
- `GET /patient/memory-test` - Memory test
- `GET /patient/speech-analysis` - Speech analysis
- `GET /patient/verbal-fluency` - Verbal fluency test
- `POST /api/submit-cognitive-test` - Submit cognitive test results
- `POST /api/submit-memory-test` - Submit memory test results
- `GET /api/patient-summary/<patient_id>` - Get patient summary data
- `GET /doctor/patient/<patient_id>` - Patient details page

## Security Features

- Session-based authentication
- Role-based access control (patient/doctor)
- Password validation
- Input sanitization
- CSRF protection (Flask built-in)

## Troubleshooting

### Common Issues

1. **Application not starting**:
   - Check logs in Render dashboard
   - Verify all dependencies are in requirements.txt
   - Check Python version compatibility

2. **CSV file errors**:
   - Ensure data directory exists
   - Check file permissions
   - Verify CSV file structure

3. **Static files not loading**:
   - Check static file paths
   - Verify Flask static configuration

### Support

For deployment issues, check:
- Render documentation: https://render.com/docs
- Flask documentation: https://flask.palletsprojects.com/
- Project issues on GitHub

## License

This project is for educational and demonstration purposes.