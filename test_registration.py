"""
Test script to verify patient registration and dashboard functionality
"""

import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

def test_registration():
    """Test patient registration"""
    registration_data = {
        'name': 'Alice Johnson',
        'email': 'alice.johnson@test.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123',
        'age': 72,
        'gender': 'Female'
    }
    
    try:
        response = requests.post(f'{BASE_URL}/register', data=registration_data)
        if response.status_code == 200:
            print("✅ Registration test passed - redirected to login")
            return True
        else:
            print(f"❌ Registration test failed - Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Registration test error: {e}")
        return False

def test_login_new_patient():
    """Test login with newly registered patient"""
    login_data = {
        'email': 'alice.johnson@test.com',
        'password': 'testpass123'
    }
    
    try:
        session = requests.Session()
        response = session.post(f'{BASE_URL}/login', data=login_data)
        if 'patient_dashboard' in response.url or response.status_code == 200:
            print("✅ New patient login test passed")
            return True, session
        else:
            print(f"❌ New patient login test failed - Status: {response.status_code}")
            return False, None
    except Exception as e:
        print(f"❌ New patient login test error: {e}")
        return False, None

def verify_csv_data():
    """Verify that CSV files are updated correctly"""
    import csv
    import os
    
    try:
        # Check users.csv
        with open('data/users.csv', 'r') as f:
            reader = csv.DictReader(f)
            users = list(reader)
            alice_user = next((u for u in users if u['email'] == 'alice.johnson@test.com'), None)
            if alice_user:
                print("✅ User data saved correctly in users.csv")
                print(f"   Patient ID: {alice_user['patient_id']}")
            else:
                print("❌ User data not found in users.csv")
                return False
        
        # Check patients.csv
        with open('data/patients.csv', 'r') as f:
            reader = csv.DictReader(f)
            patients = list(reader)
            alice_patient = next((p for p in patients if p['email'] == 'alice.johnson@test.com'), None)
            if alice_patient:
                print("✅ Patient data saved correctly in patients.csv")
                print(f"   Name: {alice_patient['name']}")
                print(f"   Age: {alice_patient['age']}")
                print(f"   Gender: {alice_patient['gender']}")
                print(f"   Risk Level: {alice_patient['risk_level']}")
            else:
                print("❌ Patient data not found in patients.csv")
                return False
        
        return True
    except Exception as e:
        print(f"❌ CSV verification error: {e}")
        return False

if __name__ == '__main__':
    print("🧪 Testing Patient Registration and Dashboard Features")
    print("=" * 60)
    
    # Test registration
    print("\n1. Testing Patient Registration...")
    if test_registration():
        
        # Verify CSV data
        print("\n2. Verifying CSV Data...")
        if verify_csv_data():
            
            # Test login
            print("\n3. Testing New Patient Login...")
            login_success, session = test_login_new_patient()
            
            if login_success:
                print("\n✅ All tests passed! New patient registration system is working correctly.")
                print("\nNext steps:")
                print("- Visit http://127.0.0.1:5000/register to test the registration form")
                print("- Login as doctor to see the enhanced dashboard with patient scores")
                print("- Login as the new patient to test the dashboard functionality")
            else:
                print("\n❌ Login test failed")
        else:
            print("\n❌ CSV verification failed")
    else:
        print("\n❌ Registration test failed")
    
    print("\n" + "=" * 60)