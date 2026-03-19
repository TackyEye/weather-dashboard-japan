# Tokyo Weather Dashboard

A real-time weather dashboard for Tokyo, Japan powered by the Open-Meteo API.

## Features

- 🌡️ Real-time temperature display
- 📊 24-hour forecast view
- 🔄 Auto-refresh every 5 minutes
- 📱 Responsive mobile-friendly design
- ☁️ Easy cloud deployment

## Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd weather-dashboard-japan
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## Deployment

### Deploy to Vercel (Recommended for simplicity)

1. **Fork/push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo>
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project" and import your GitHub repo
   - Vercel will auto-detect Flask
   - Deploy!

3. **Your dashboard is now live!**

### Alternative: Deploy to Heroku

1. **Install Heroku CLI** and login
   ```bash
   heroku login
   ```

2. **Create Procfile** (add this file):
   ```
   web: gunicorn app:app
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Your app is now live on Heroku!**

## Future Enhancements

- [ ] Multiple city support
- [ ] Historical data charts
- [ ] Weather alerts
- [ ] Dark mode toggle
- [ ] More detailed weather parameters (humidity, wind, etc.)

## Technology Stack

- **Backend**: Flask (Python)
- **API**: Open-Meteo (free, no key required)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Hosting**: Vercel/Netlify/Heroku
