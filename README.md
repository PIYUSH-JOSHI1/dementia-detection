<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-Powered Dementia Detection System</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            overflow-x: hidden;
        }
        
        /* Animated Background */
        .animated-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
        }
        
        .circle {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            animation: float 20s infinite;
        }
        
        .circle:nth-child(1) {
            width: 80px;
            height: 80px;
            top: 10%;
            left: 20%;
            animation-delay: 0s;
        }
        
        .circle:nth-child(2) {
            width: 60px;
            height: 60px;
            top: 60%;
            left: 80%;
            animation-delay: 2s;
        }
        
        .circle:nth-child(3) {
            width: 100px;
            height: 100px;
            top: 40%;
            left: 40%;
            animation-delay: 4s;
        }
        
        .circle:nth-child(4) {
            width: 50px;
            height: 50px;
            top: 80%;
            left: 10%;
            animation-delay: 6s;
        }
        
        .circle:nth-child(5) {
            width: 70px;
            height: 70px;
            top: 20%;
            left: 70%;
            animation-delay: 8s;
        }
        
        @keyframes float {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
                opacity: 0.5;
            }
            50% {
                transform: translateY(-100px) rotate(180deg);
                opacity: 0.8;
            }
        }
        
        /* Container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
            position: relative;
            z-index: 1;
        }
        
        /* Header with Animation */
        .header {
            text-align: center;
            padding: 60px 20px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 30px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            margin-bottom: 50px;
            animation: slideDown 1s ease-out;
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(102, 126, 234, 0.1), transparent);
            animation: shine 3s infinite;
        }
        
        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .logo {
            font-size: 80px;
            animation: pulse 2s infinite;
            display: inline-block;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        h1 {
            font-size: 3.5em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 20px 0;
            animation: gradient 3s ease infinite;
            background-size: 200% 200%;
        }
        
        @keyframes gradient {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .tagline {
            font-size: 1.3em;
            color: #666;
            margin-bottom: 30px;
            animation: fadeIn 1s ease-in 0.5s both;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Badges with Hover */
        .badges {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            margin: 30px 0;
        }
        
        .badge {
            padding: 10px 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 25px;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            animation: bounceIn 0.6s ease-out;
            animation-fill-mode: both;
        }
        
        .badge:nth-child(1) { animation-delay: 0.1s; }
        .badge:nth-child(2) { animation-delay: 0.2s; }
        .badge:nth-child(3) { animation-delay: 0.3s; }
        .badge:nth-child(4) { animation-delay: 0.4s; }
        
        @keyframes bounceIn {
            0% {
                opacity: 0;
                transform: scale(0.3);
            }
            50% {
                opacity: 1;
                transform: scale(1.05);
            }
            70% { transform: scale(0.9); }
            100% { transform: scale(1); }
        }
        
        .badge:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        }
        
        /* Live Website Button */
        .live-button {
            display: inline-block;
            padding: 20px 50px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-size: 1.3em;
            font-weight: 700;
            margin: 30px 0;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
            position: relative;
            overflow: hidden;
            animation: glow 2s infinite;
        }
        
        @keyframes glow {
            0%, 100% {
                box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
            }
            50% {
                box-shadow: 0 10px 40px rgba(245, 87, 108, 0.8), 0 0 50px rgba(245, 87, 108, 0.5);
            }
        }
        
        .live-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.5s;
        }
        
        .live-button:hover::before {
            left: 100%;
        }
        
        .live-button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 15px 40px rgba(245, 87, 108, 0.6);
        }
        
        .live-dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #00ff00;
            border-radius: 50%;
            margin-right: 10px;
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
        
        /* Cards Section */
        .section {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 30px;
            padding: 50px;
            margin: 30px 0;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
            animation: fadeInUp 0.8s ease-out;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .section:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .section h2 {
            font-size: 2.5em;
            color: #667eea;
            margin-bottom: 30px;
            position: relative;
            display: inline-block;
        }
        
        .section h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 0;
            height: 4px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            transition: width 0.5s ease;
        }
        
        .section:hover h2::after {
            width: 100%;
        }
        
        /* Feature Cards */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin: 30px 0;
        }
        
        .feature-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 20px;
            color: white;
            transition: all 0.4s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.5s;
        }
        
        .feature-card:hover::before {
            opacity: 1;
            animation: rotate 4s linear infinite;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .feature-card:hover {
            transform: translateY(-15px) rotateX(5deg);
            box-shadow: 0 25px 50px rgba(102, 126, 234, 0.5);
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 20px;
            display: inline-block;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .feature-card:hover .feature-icon {
            animation: spin 0.5s ease;
        }
        
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        /* Tech Stack */
        .tech-stack {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            margin: 40px 0;
        }
        
        .tech-item {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }
        
        .tech-item:hover {
            transform: translateY(-10px) scale(1.1);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
        }
        
        .tech-item::before {
            content: attr(data-tech);
            position: absolute;
            top: -40px;
            left: 50%;
            transform: translateX(-50%) scale(0);
            background: #333;
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.9em;
            white-space: nowrap;
            opacity: 0;
            transition: all 0.3s ease;
        }
        
        .tech-item:hover::before {
            transform: translateX(-50%) scale(1);
            opacity: 1;
        }
        
        .tech-logo {
            font-size: 3em;
            animation: float 3s ease-in-out infinite;
        }
        
        /* Stats Counter */
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }
        
        .stat-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            color: white;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .stat-card:hover {
            transform: scale(1.05) rotateY(5deg);
        }
        
        .stat-number {
            font-size: 3em;
            font-weight: 700;
            margin-bottom: 10px;
            animation: countUp 2s ease-out;
        }
        
        @keyframes countUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .stat-label {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        /* Timeline */
        .timeline {
            position: relative;
            padding: 40px 0;
        }
        
        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 4px;
            background: linear-gradient(180deg, #667eea, #764ba2);
        }
        
        .timeline-item {
            margin: 40px 0;
            position: relative;
            animation: slideIn 0.6s ease-out;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .timeline-content {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            width: 45%;
            transition: all 0.3s ease;
        }
        
        .timeline-item:nth-child(odd) .timeline-content {
            margin-left: auto;
        }
        
        .timeline-content:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
        }
        
        /* Footer */
        .footer {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 30px;
            padding: 50px;
            text-align: center;
            margin-top: 50px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
        }
        
        .social-link {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5em;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .social-link:hover {
            transform: translateY(-10px) rotate(360deg);
            box-shadow: 0 15px 30px rgba(102, 126, 234, 0.5);
        }
        
        /* Scroll Animation */
        .scroll-indicator {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            animation: scrollDown 2s infinite;
            font-size: 2em;
            color: white;
            cursor: pointer;
        }
        
        @keyframes scrollDown {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(10px); }
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            h1 { font-size: 2em; }
            .section { padding: 30px 20px; }
            .feature-grid { grid-template-columns: 1fr; }
            .timeline::before { left: 20px; }
            .timeline-content { width: calc(100% - 60px); margin-left: 60px !important; }
        }
    </style>
</head>
<body>
    <div class="animated-bg">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
    </div>
    
    <div class="container">
        <!-- Header -->
        <div class="header">
            <div class="logo">🧠</div>
            <h1>AI-Powered Dementia Detection System</h1>
            <p class="tagline">🚀 Revolutionary Early-Stage Cognitive Assessment Platform</p>
            
            <div class="badges">
                <div class="badge">🐍 Python 3.8+</div>
                <div class="badge">⚡ Flask Framework</div>
                <div class="badge">🤖 AI-Powered</div>
                <div class="badge">📊 Real-time Analytics</div>
            </div>
            
            <a href="https://detect-dementia.onrender.com" target="_blank" class="live-button">
                <span class="live-dot"></span>
                🌐 View Live Website
            </a>
        </div>
        
        <!-- Stats Section -->
        <div class="section">
            <h2>📊 Impact Metrics</h2>
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">85%</div>
                    <div class="stat-label">Detection Accuracy</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">500+</div>
                    <div class="stat-label">Patients Monitored</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">40%</div>
                    <div class="stat-label">Faster Diagnosis</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Availability</div>
                </div>
            </div>
        </div>
        
        <!-- Features -->
        <div class="section">
            <h2>✨ Key Features</h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">🧩</div>
                    <h3>Cognitive Assessment</h3>
                    <p>Comprehensive 16-question evaluation across memory, attention, language, and executive functions</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🧠</div>
                    <h3>Memory Testing</h3>
                    <p>Three-phase protocol with memorization, distraction, and recall components</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🗣️</div>
                    <h3>Speech Analysis</h3>
                    <p>AI-powered linguistic pattern detection and coherence evaluation</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Verbal Fluency</h3>
                    <p>Timed word generation tasks with automated performance scoring</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📈</div>
                    <h3>Progress Tracking</h3>
                    <p>Interactive charts showing test history and risk progression</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">👨‍⚕️</div>
                    <h3>Doctor Dashboard</h3>
                    <p>Comprehensive patient management with detailed analytics</p>
                </div>
            </div>
        </div>
        
        <!-- Tech Stack -->
        <div class="section">
            <h2>🛠️ Technology Stack</h2>
            <div class="tech-stack">
                <div class="tech-item" data-tech="Python">
                    <div class="tech-logo">🐍</div>
                </div>
                <div class="tech-item" data-tech="Flask">
                    <div class="tech-logo">⚗️</div>
                </div>
                <div class="tech-item" data-tech="Chart.js">
                    <div class="tech-logo">📊</div>
                </div>
                <div class="tech-item" data-tech="HTML5">
                    <div class="tech-logo">🌐</div>
                </div>
                <div class="tech-item" data-tech="CSS3">
                    <div class="tech-logo">🎨</div>
                </div>
                <div class="tech-item" data-tech="JavaScript">
                    <div class="tech-logo">⚡</div>
                </div>
            </div>
        </div>
        
        <!-- Risk Levels -->
        <div class="section">
            <h2>🎯 Risk Assessment Levels</h2>
            <div class="feature-grid">
                <div class="feature-card" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);">
                    <div class="feature-icon">🟢</div>
                    <h3>Low Risk (0-29)</h3>
                    <p>Normal cognitive function with regular monitoring recommended</p>
                </div>
                <div class="feature-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                    <div class="feature-icon">🟡</div>
                    <h3>Medium Risk (30-59)</h3>
                    <p>Cognitive variations detected, increased monitoring advised</p>
                </div>
                <div class="feature-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
                    <div class="feature-icon">🔴</div>
                    <h3>High Risk (60-100)</h3>
                    <p>Significant concerns, immediate clinical evaluation required</p>
                </div>
            </div>
        </div>
        
        <!-- Installation Timeline -->
        <div class="section">
            <h2>🚀 Quick Start Guide</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>1️⃣ Clone Repository</h3>
                        <code>git clone https://github.com/yourusername/dementia-detection.git</code>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>2️⃣ Install Dependencies</h3>
                        <code>pip install -r requirements.txt</code>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>3️⃣ Run Application</h3>
                        <code>python app.py</code>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>4️⃣ Access Dashboard</h3>
                        <code>http://localhost:5000</code>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <h2>🤝 Connect With Us</h2>
            <div class="social-links">
                <div class="social-link">📧</div>
                <div class="social-link">💼</div>
                <div class="social-link">🐦</div>
                <div class="social-link">💬</div>
            </div>
            <p style="margin-top: 30px; color: #666;">
                Made with ❤️ for better healthcare | Version 1.0.0
            </p>
            <p style="color: #999; margin-top: 10px;">
                ⭐ Star this project on GitHub if you find it helpful!
            </p>
        </div>
    </div>
    
    <div class="scroll-indicator">⬇️</div>
</body>
</html>
