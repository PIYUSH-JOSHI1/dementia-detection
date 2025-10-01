"""
Script to add sample test data for demonstration
"""

import csv
import json
from datetime import datetime, timedelta
import random

def add_sample_test_data():
    """Add sample test results for the default patient"""
    
    # Sample test data for P001 (John Doe)
    sample_tests = [
        {
            'test_id': 'CT20241001001',
            'patient_id': 'P001',
            'test_type': 'Cognitive',
            'score': '82.5',
            'risk_score': '17.5',
            'timestamp': (datetime.now() - timedelta(days=7)).isoformat(),
            'details': json.dumps({'memory': 85, 'attention': 78, 'language': 84, 'executive': 83})
        },
        {
            'test_id': 'MT20241001002',
            'patient_id': 'P001',
            'test_type': 'Memory',
            'score': '76.0',
            'risk_score': '24.0',
            'timestamp': (datetime.now() - timedelta(days=5)).isoformat(),
            'details': json.dumps({'correct_recalls': 8, 'false_recalls': 2, 'total_words': 10, 'recall_rate': 80.0})
        },
        {
            'test_id': 'SA20241001003',
            'patient_id': 'P001',
            'test_type': 'Speech Analysis',
            'score': '88.3',
            'risk_score': '11.7',
            'timestamp': (datetime.now() - timedelta(days=3)).isoformat(),
            'details': json.dumps({'fluency_score': 90, 'coherence_score': 85, 'vocabulary_score': 90, 'pause_analysis': 'Normal'})
        },
        {
            'test_id': 'CT20241001004',
            'patient_id': 'P001',
            'test_type': 'Cognitive',
            'score': '79.8',
            'risk_score': '20.2',
            'timestamp': (datetime.now() - timedelta(days=1)).isoformat(),
            'details': json.dumps({'memory': 82, 'attention': 75, 'language': 81, 'executive': 81})
        }
    ]
    
    # Add to test_results.csv
    with open('data/test_results.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for test in sample_tests:
            writer.writerow([
                test['test_id'],
                test['patient_id'],
                test['test_type'],
                test['score'],
                test['risk_score'],
                test['timestamp'],
                test['details']
            ])
    
    # Update patient's last test date and risk level
    patients = []
    with open('data/patients.csv', 'r') as f:
        reader = csv.DictReader(f)
        patients = list(reader)
    
    # Update P001's data
    for patient in patients:
        if patient['patient_id'] == 'P001':
            patient['last_test_date'] = sample_tests[-1]['timestamp']
            patient['risk_level'] = 'Low'  # Based on latest good scores
    
    # Write back to patients.csv
    with open('data/patients.csv', 'w', newline='') as f:
        fieldnames = ['patient_id', 'name', 'age', 'gender', 'email', 'baseline_score', 'last_test_date', 'risk_level']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)
    
    print("✅ Sample test data added successfully!")
    print(f"Added {len(sample_tests)} test results for patient P001")
    print("This will demonstrate:")
    print("- Test history on patient dashboard")
    print("- Progress charts")
    print("- Enhanced test details modal")
    print("- Doctor dashboard with patient scores")

if __name__ == '__main__':
    add_sample_test_data()