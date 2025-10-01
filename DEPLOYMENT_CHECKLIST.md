# 🚀 Render Deployment Checklist

## Pre-Deployment Steps

### ✅ Files Required
- [ ] `app.py` - Main Flask application
- [ ] `requirements.txt` - Python dependencies (Flask, gunicorn, python-dotenv)
- [ ] `Procfile` - Contains: `web: gunicorn app:app`
- [ ] `runtime.txt` - Contains: `python-3.11.5`
- [ ] `render.yaml` - Render configuration (optional but recommended)
- [ ] `templates/` folder with all HTML files
- [ ] `static/` folder with CSS and JS files
- [ ] `data/` folder with CSV files

### ✅ Code Modifications for Production
- [ ] Updated app.py to use environment variables
- [ ] Changed secret key to use `os.environ.get('SECRET_KEY')`
- [ ] Updated file paths to use absolute paths
- [ ] Added health check endpoint `/health`
- [ ] Modified debug mode for production
- [ ] Updated port configuration

### ✅ Repository Preparation
- [ ] Push all changes to GitHub
- [ ] Remove unnecessary files (Next.js files, test files)
- [ ] Ensure .gitignore is properly configured
- [ ] Verify all CSV files are committed with initial data

## Deployment Steps on Render

### 1. Create Render Account
- [ ] Go to https://render.com
- [ ] Sign up for free account
- [ ] Connect GitHub account

### 2. Create Web Service
- [ ] Click "New +" → "Web Service"
- [ ] Select your GitHub repository
- [ ] Choose repository branch (usually main/master)

### 3. Configure Service
```
Name: dementia-detection-app
Environment: Python 3
Region: Choose closest to your users
Branch: main (or master)
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

### 4. Environment Variables (Optional)
```
FLASK_ENV=production
SECRET_KEY=[auto-generate or set your own]
```

### 5. Advanced Settings
- [ ] Instance Type: Free (for development)
- [ ] Health Check Path: `/health`
- [ ] Auto-Deploy: Yes (recommended)

### 6. Deploy
- [ ] Click "Create Web Service"
- [ ] Wait for build to complete (5-10 minutes)
- [ ] Monitor build logs for any errors

## Post-Deployment Testing

### ✅ Basic Functionality
- [ ] Application loads without errors
- [ ] Home page redirects to login
- [ ] Login page displays correctly
- [ ] Static files (CSS/JS) load properly

### ✅ Authentication Testing
- [ ] Doctor login works (doctor@demo.com / doctor123)
- [ ] Patient login works (patient@demo.com / patient123)
- [ ] Registration form works
- [ ] Logout functionality works

### ✅ Dashboard Testing
- [ ] Patient dashboard displays correctly
- [ ] Doctor dashboard shows patient data
- [ ] Charts and graphs render properly
- [ ] Test details modal works

### ✅ New Features Testing
- [ ] Patient registration creates new accounts
- [ ] New patient data appears in doctor dashboard
- [ ] Enhanced test details modal functions
- [ ] Download functionality works

## Monitoring and Maintenance

### ✅ Set Up Monitoring
- [ ] Check Render dashboard for metrics
- [ ] Monitor application logs
- [ ] Set up alerts for downtime (if needed)

### ✅ Performance Optimization
- [ ] Monitor response times
- [ ] Check memory usage
- [ ] Optimize if needed (upgrade plan if necessary)

## Troubleshooting Common Issues

### Build Failures
- Check `requirements.txt` for correct dependencies
- Verify Python version in `runtime.txt`
- Check build logs for specific error messages

### Application Won't Start
- Verify `Procfile` has correct start command
- Check for syntax errors in `app.py`
- Ensure all required environment variables are set

### Static Files Not Loading
- Verify Flask static file configuration
- Check file paths in templates
- Ensure static files are committed to repository

### Database/CSV Issues
- Verify data folder structure
- Check file permissions
- Ensure CSV files have correct headers

## Success Criteria

Your deployment is successful when:
- [ ] Application loads at your Render URL
- [ ] All login functionality works
- [ ] Dashboards display correctly with data
- [ ] New user registration works
- [ ] Test functionalities work properly
- [ ] No console errors in browser

## Your Render URL
Once deployed, your app will be available at:
`https://[your-app-name].onrender.com`

## Support Resources
- Render Documentation: https://render.com/docs
- Flask Documentation: https://flask.palletsprojects.com/
- GitHub Issues: [Your repository URL]/issues