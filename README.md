# AI Tool for Early-Stage Dementia Detection

A Flask-based web application for early detection of dementia using AI-powered cognitive assessments, speech analysis, and memory tests.

## Features

### Patient Features
- **Cognitive Tests**: Comprehensive assessments for memory, attention, language, and executive function
- **Memory Tests**: Specialized memory recall and recognition tasks with three-phase testing
- **Speech Analysis**: AI-powered analysis of speech patterns, fluency, and coherence
- **Verbal Fluency Tests**: Timed word generation tasks across multiple categories
- **Progress Tracking**: Interactive charts showing test history and risk scores over time
- **Performance Visualization**: Line charts, pie charts, and trend analysis

### Doctor Features
- **Patient Dashboard**: Overview of all patients with filtering and search capabilities
- **Detailed Reports**: Access comprehensive test results and analysis
- **Risk Assessment**: View AI-generated risk scores and clinical recommendations
- **Longitudinal Tracking**: Monitor patient progress over time with interactive charts
- **Data Visualization**: Performance trends, risk progression, cognitive domain analysis
- **Clinical Recommendations**: Automated suggestions based on risk levels

### Risk Scoring System
- **Multi-dimensional Analysis**: Combines scores from cognitive, memory, speech, and fluency tests
- **Dynamic Risk Levels**: Automatically categorizes patients as Low, Medium, or High risk
- **Baseline Comparison**: Tracks deviations from individual baseline performance
- **Trend Analysis**: Identifies patterns and progression over time

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Data Visualization**: Chart.js
- **Data Storage**: CSV files (no database required)
- **AI Analysis**: Built-in scoring algorithms based on clinical research

## Installation

1. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Run the application:
\`\`\`bash
python app.py
\`\`\`

3. Access the application at `http://localhost:5000`

## Default Login Credentials

### Doctor Login
- Email: `doctor@demo.com`
- Password: `doctor123`

### Patient Login
- Email: `patient@demo.com`
- Password: `patient123`

## File Structure

\`\`\`
dementia-detection-flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── data/                 # CSV data storage
│   ├── users.csv
│   ├── patients.csv
│   ├── test_results.csv
│   ├── cognitive_tests.csv
│   └── speech_analysis.csv
├── static/
│   ├── css/
│   │   └── style.css     # Common styles
│   └── js/
│       └── main.js       # Common JavaScript
└── templates/
    ├── base.html         # Base template
    ├── login.html        # Login page
    ├── patient_dashboard.html    # Patient dashboard with charts
    ├── doctor_dashboard.html     # Doctor dashboard with analytics
    ├── cognitive_test.html       # Cognitive assessment
    ├── memory_test.html          # Memory test
    ├── speech_analysis.html      # Speech analysis
    ├── verbal_fluency.html       # Verbal fluency test
    └── patient_details.html      # Detailed patient reports
\`\`\`

## Features Based on Research

This application implements evidence-based techniques from current dementia detection research:

- **Multimodal Assessment**: Combines cognitive tests, speech analysis, and memory tasks
- **Risk Scoring**: AI-powered risk assessment with clinical referral recommendations
- **Longitudinal Tracking**: Baseline comparison and progress monitoring
- **Data Visualization**: Interactive charts for trend analysis and performance tracking
- **Accessible Interface**: User-friendly design for elderly users
- **Vernacular Support**: Framework ready for multiple language integration

## Assessment Types

### 1. Cognitive Assessment (16 questions)
- Memory: Word recall, personal memory, pattern recognition
- Attention: Calculation, spelling, logic problems
- Language: Vocabulary, comprehension, categorization, fluency
- Executive Function: Planning, judgment, visuospatial skills

### 2. Memory Test (3 phases)
- Memorization: 60-second word study period
- Distraction: 5 simple questions to create delay
- Recall: Recognition test with distractors

### 3. Speech Analysis (6 tasks)
- Description tasks for fluency assessment
- Narrative tasks for coherence evaluation
- Vocabulary richness analysis
- Pause pattern detection

### 4. Verbal Fluency (3 categories)
- Timed word generation (60 seconds per category)
- Category-based and letter-based tasks
- Automatic scoring and performance analysis

## Risk Scoring Algorithm

The system calculates risk scores based on:
- Test performance across multiple domains
- Deviation from baseline scores
- Consistency across different test types
- Temporal trends and progression patterns

**Risk Levels:**
- **Low Risk** (0-29): Normal cognitive function
- **Medium Risk** (30-59): Some cognitive variations, monitoring recommended
- **High Risk** (60-100): Significant concerns, clinical evaluation recommended

## Data Visualization

### Patient Dashboard
- Progress line chart showing score trends
- Test type distribution pie chart
- Risk score trend analysis

### Doctor Dashboard
- Risk distribution doughnut chart
- Age distribution bar chart
- Patient-specific performance trends
- Cognitive domain radar charts
- Risk progression over time

## Future Enhancements

- Integration with speech recognition APIs for real-time analysis
- Machine learning models for improved risk prediction
- Support for Indian languages (Hindi, Tamil, Bengali, etc.)
- Mobile application version
- Integration with clinical databases
- Advanced data visualization and analytics
- Export reports to PDF
- Multi-language interface

## Clinical Validation

This tool is designed as a screening instrument and should not replace comprehensive clinical evaluation. All high-risk cases should be referred to qualified healthcare professionals for thorough assessment.

## License

This project is developed for educational and research purposes.
