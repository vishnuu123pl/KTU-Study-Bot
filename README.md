# 🎓 KTU Study Bot V3

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Pyrogram-2.x-green?style=for-the-badge" alt="Pyrogram"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
</p>

<p align="center">
  <strong>A feature-rich Telegram bot for KTU (APJ Abdul Kalam Technological University) B.Tech students</strong><br>
  Access study materials, previous year questions, model papers, video resources, and more — organized by branch, scheme, and semester.
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-commands">Commands</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Environment Variables](#️-environment-variables)
- [🐳 Docker Deployment](#-docker-deployment)
- [☁️ Cloud Deployment](#️-cloud-deployment)
- [🛠️ Admin Commands](#️-admin-commands)
- [📱 User Features](#-user-features)
- [🗂️ Project Structure](#️-project-structure)
- [🔧 Configuration](#-configuration)
- [📊 Database Schema](#-database-schema)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

### 🎯 Core Features

| Feature | Description |
|---------|-------------|
| 📚 **Study Materials** | Access comprehensive notes for all subjects, organized by semester |
| 📝 **Previous Year Questions (PYQ)** | Browse and download subject-wise previous year question papers |
| 📖 **Model Papers** | Download model exam papers for better exam preparation |
| 🎥 **Video Resources** | Direct links to helpful educational video content |
| 🔎 **Smart Search** | Quick subject search using `/search` command with inline results |
| 📈 **Trending Requests** | View most requested subjects and materials in real-time |
| 💾 **PostgreSQL Database** | Robust database integration for persistent data storage |
| 📊 **Analytics Dashboard** | Admin analytics for tracking popular subjects and user requests |

### 🏫 Academic Coverage

| Category | Details |
|----------|---------|
| **Branches** | CSE, ECE, EEE, Mechanical, Civil, ICE |
| **Schemes** | 2019 Scheme, 2024 Scheme (Latest) |
| **Semesters** | Complete coverage from Semester 1 to Semester 8 |
| **Subjects** | 100+ subjects with comprehensive material coverage |

### 🎛️ Advanced Features

- **🔐 Admin Panel** - Complete resource management system
- **📤 File Upload System** - Easy-to-use upload interface for admins
- **📢 Broadcast System** - Send announcements to all registered users
- **📊 User Analytics** - Track user engagement and popular content
- **🗑️ Resource Management** - Add, list, delete resources effortlessly
- **📩 Request System** - Users can request missing materials
- **📈 Trending Analysis** - Shows top 10 most requested subjects
- **🔔 Log Channel** - Automatic logging of new users and activities
- **↩️ Smart Navigation** - Intuitive back button for seamless browsing
- **💬 Interactive UI** - Beautiful inline keyboard buttons for easy interaction

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Telegram Bot API                        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Pyrogram Client Layer                     │
│           (Async handlers with plugin system)               │
└─────────────────────────────────────────────────────────────┘
                            │
           ┌────────────────┼────────────────┐
           ▼                ▼                ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  Plugins │    │ Database │    │   Web    │
    │  System  │───▶│  Models  │    │  Server  │
    └──────────┘    └──────────┘    └──────────┘
           │                │                │
           │                ▼                │
           │         ┌─────────────┐         │
           │         │ PostgreSQL  │         │
           │         │  (asyncpg)  │         │
           │         └─────────────┘         │
           │                                 │
           ▼                                 ▼
    ┌──────────────┐              ┌─────────────────┐
    │   Subject    │              │  Flask Health   │
    │     Data     │              │   Check Server  │
    │   (Python)   │              │   (Port 8000)   │
    └──────────────┘              └─────────────────┘
```

**Technology Stack:**
- **Backend**: Python 3.11+, Pyrogram, asyncpg
- **Database**: PostgreSQL (with async connection pooling)
- **Web Server**: Flask (for health checks)
- **Containerization**: Docker support
- **Deployment**: Railway, Koyeb, Render, Fly.io compatible

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- PostgreSQL database (local or cloud-hosted like Supabase)
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Telegram API credentials from [my.telegram.org](https://my.telegram.org)

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/KTU-Study-Bot-V3.git
cd KTU-Study-Bot-V3

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env with your credentials (see Environment Variables section)

# 4. Ensure PostgreSQL database is running and accessible
# Database tables will be created automatically on first run

# 5. Start the bot
python web.py
```

The bot will start running and the Flask health check server will be available at `http://localhost:8000`.

### Verify Installation

```bash
# Check if bot is responding
curl http://localhost:8000

# Expected response: "KTU Study Bot is running!"
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Telegram Bot Configuration
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_bot_token_from_botfather

# Admin Configuration
ADMINS=123456789,987654321  # Comma-separated user IDs

# Database Configuration
DATABASE_URL=postgresql://username:password@host:port/database

# Logging Configuration (Optional)
LOG_CHANNEL=-1001234567890  # Your log channel ID (bot must be admin)
```

### How to Get These Values

| Variable | Where to Get | Instructions |
|----------|--------------|--------------|
| `API_ID` | [my.telegram.org](https://my.telegram.org) | Login → API Development Tools → Create App |
| `API_HASH` | [my.telegram.org](https://my.telegram.org) | Same as above, you'll get both API_ID and API_HASH |
| `BOT_TOKEN` | [@BotFather](https://t.me/BotFather) | Send `/newbot` and follow the instructions |
| `ADMINS` | [@userinfobot](https://t.me/userinfobot) | Send any message to get your Telegram user ID |
| `DATABASE_URL` | Your PostgreSQL provider | See [Database Setup](#-database-setup) below |
| `LOG_CHANNEL` | Your Telegram channel | Create a channel, add bot as admin, get channel ID |

### 📊 Database Setup

#### Option 1: Supabase (Recommended for Beginners - Free Tier Available)

```bash
1. Go to https://supabase.com and create a free account
2. Create a new project
3. Go to Project Settings → Database
4. Find "Connection String" under "Connection Pooling"
5. Copy the connection string (format: postgresql://...)
6. Add it to your .env file as DATABASE_URL
```

**Example Supabase URL:**
```
postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres
```

#### Option 2: Railway (Easy Setup)

```bash
1. Go to https://railway.app
2. Create new project → Add PostgreSQL
3. Copy the DATABASE_URL from the Connect tab
4. Add to your .env file
```

#### Option 3: Local PostgreSQL

```bash
# Install PostgreSQL locally
sudo apt-get install postgresql postgresql-contrib  # Ubuntu/Debian
brew install postgresql  # macOS

# Create database
sudo -u postgres createdb ktu_study_bot

# Your DATABASE_URL will be:
DATABASE_URL=postgresql://postgres:password@localhost:5432/ktu_study_bot
```

---

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
# Build the Docker image
docker build -t ktu-study-bot .

# Run the container
docker run -d \
  --name ktu-bot \
  -e API_ID=your_api_id \
  -e API_HASH=your_api_hash \
  -e BOT_TOKEN=your_bot_token \
  -e ADMINS=your_user_id \
  -e DATABASE_URL=your_database_url \
  -e LOG_CHANNEL=your_log_channel \
  -p 8000:8000 \
  ktu-study-bot

# View logs
docker logs -f ktu-bot

# Stop the container
docker stop ktu-bot

# Remove the container
docker rm ktu-bot
```

### Docker Compose (Recommended)

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  bot:
    build: .
    environment:
      - API_ID=${API_ID}
      - API_HASH=${API_HASH}
      - BOT_TOKEN=${BOT_TOKEN}
      - ADMINS=${ADMINS}
      - DATABASE_URL=${DATABASE_URL}
      - LOG_CHANNEL=${LOG_CHANNEL}
    ports:
      - "8000:8000"
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---

## ☁️ Cloud Deployment

### 🟢 Free Platforms

#### 1. **Koyeb** (Recommended - Easiest Setup)

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com)

**Manual Setup:**

```bash
1. Create account at https://www.koyeb.com
2. Click "Create App" → "Deploy from GitHub"
3. Connect your repository
4. Configure:
   - Build: Dockerfile
   - Port: 8000
   - Health Check: /
5. Add environment variables:
   API_ID, API_HASH, BOT_TOKEN, ADMINS, DATABASE_URL, LOG_CHANNEL
6. Deploy!
```

**Features:**
- ✅ Free tier with 2 services
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Zero downtime deployments

---

#### 2. **Railway** (Developer-Friendly)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

**Quick Deploy:**

```bash
1. Go to https://railway.app
2. Click "Start a New Project" → "Deploy from GitHub"
3. Select your repository
4. Railway auto-detects settings from Procfile
5. Add environment variables in Variables tab
6. Click Deploy
```

**Built-in PostgreSQL:**
```bash
1. In your Railway project, click "New"
2. Select "Database" → "PostgreSQL"
3. Copy DATABASE_URL from Variables tab
4. Add to your bot service environment variables
```

**Features:**
- ✅ $5/month free credits
- ✅ Built-in PostgreSQL
- ✅ Automatic deployments on git push
- ✅ Easy to use CLI

---

#### 3. **Render** (Reliable and Simple)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

**Setup Steps:**

```bash
1. Go to https://render.com
2. Create "New Web Service"
3. Connect GitHub repository
4. Configure:
   - Build Command: pip install -r requirements.txt
   - Start Command: python web.py
5. Add environment variables
6. Create PostgreSQL database (separate service)
7. Deploy
```

**Prevent Sleep (Important for Free Tier):**
```bash
# Add UptimeRobot to ping your service every 5 minutes
# URL to ping: https://your-app.onrender.com/
```

**Features:**
- ✅ Free tier available
- ✅ Automatic SSL certificates
- ✅ PostgreSQL support
- ⚠️ Free tier sleeps after 15 min inactivity

---

#### 4. **Fly.io** (Best for Docker)

**Installation:**

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Launch app
fly launch

# Set secrets
fly secrets set \
  API_ID=your_api_id \
  API_HASH=your_api_hash \
  BOT_TOKEN=your_bot_token \
  ADMINS=your_user_id \
  DATABASE_URL=your_database_url \
  LOG_CHANNEL=your_log_channel

# Deploy
fly deploy

# Check status
fly status

# View logs
fly logs
```

**Features:**
- ✅ 3 shared VMs free
- ✅ Excellent Docker support
- ✅ Global deployment
- ✅ Always-on (no sleep)

---

### 💳 Paid Platforms

| Platform | Starting Price | Best For | Notes |
|----------|---------------|----------|-------|
| **Heroku** | $7/month | Beginners, reliability | Uses `Procfile` (already configured) |
| **DigitalOcean** | $6/month | Full control | App Platform or Droplets |
| **AWS Lightsail** | $3.50/month | AWS ecosystem | Requires AWS knowledge |
| **VPS (Contabo, Hetzner)** | $4-6/month | Best value | Full server control, SSH required |

#### Heroku Deployment

```bash
# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login
heroku login

# Create app
heroku create ktu-study-bot

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set \
  API_ID=your_api_id \
  API_HASH=your_api_hash \
  BOT_TOKEN=your_bot_token \
  ADMINS=your_user_id \
  LOG_CHANNEL=your_log_channel

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

---

## 🛠️ Admin Commands

All admin commands are restricted to user IDs listed in the `ADMINS` environment variable.

### Resource Management

```bash
# View admin help panel
/admin

# Upload resources
/upload <category> <year> <branch> <semester> <subject>
# Example: /upload notes 2024 cse sem1 maths
# Then send PDF files (can send multiple files)
# Use /done when finished

# End upload session
/done

# Delete resources
/delete <category> <year> <branch> <semester> <subject>
# Example: /delete notes 2024 cse sem1 maths

# List all resource keys
/list

# View statistics
/stats
```

### Analytics & Monitoring

```bash
# View top requested subjects
/topreq

# Access trending requests (also available to users)
# Click "📈 Trending" button in main menu
```

### User Management

```bash
# Broadcast message to all users
/broadcast Your message here

# Example:
/broadcast 📢 New materials added for Semester 3!
```

### Upload Workflow Example

```
Admin: /upload notes 2024 cse sem1 maths
Bot: ✅ Upload session started. Send PDF files.

Admin: [Sends PDF file: Chapter1.pdf]
Bot: ✅ Saved! Send more or /done

Admin: [Sends PDF file: Chapter2.pdf]
Bot: ✅ Saved! Send more or /done

Admin: /done
Bot: ✅ Session ended. 2 files uploaded.
```

---

## 📱 User Features

### Getting Started

```
1. Start the bot: /start
2. Choose "📚 Get Notes / PYQ"
3. Select Scheme (2019 or 2024)
4. Choose Semester (1-8)
5. Select your Branch
6. Pick a Subject
7. Choose resource type (Notes/PYQ/Model/Video)
8. Download files!
```

### Search Feature

```bash
# Quick search for any subject
/search data structures

# Search by code
/search ma101

# Partial matches work
/search circuit
```

### Request Missing Materials

```
1. Navigate to any subject
2. If material not available, click "📩 Request"
3. Request sent directly to admins
4. Get notified when added!
```

### View Trending

```
1. Click "📈 Trending Requests" from main menu
2. See top 10 most requested subjects
3. Helps you know what others are looking for
```

---

## 🗂️ Project Structure

```
KTU-Study-Bot-V3/
│
├── bot.py                      # Pyrogram client setup and initialization
├── web.py                      # Flask server + bot launcher
├── config.py                   # Environment variables configuration
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
├── Dockerfile                  # Docker container configuration
├── Procfile                    # For Heroku/Railway deployment
├── start.sh                    # Shell startup script
├── .env.example                # Sample environment file template
├── .gitignore                  # Git ignore rules
│
├── database/                   # Database layer
│   ├── __init__.py
│   ├── db.py                   # PostgreSQL connection pool & schema
│   └── models.py               # Database operations (CRUD)
│
├── data/                       # Subject data by branch
│   ├── __init__.py             # Exports combined DATA dictionary
│   ├── cse.py                  # Computer Science subjects
│   ├── ece.py                  # Electronics & Communication subjects
│   ├── eee.py                  # Electrical & Electronics subjects
│   ├── me.py                   # Mechanical Engineering subjects
│   ├── civil.py                # Civil Engineering subjects
│   └── ice.py                  # Instrumentation & Control subjects
│
└── plugins/                    # Modular plugin system
    ├── start.py                # /start command & welcome screen
    ├── help.py                 # /help command
    ├── about.py                # About section
    ├── scheme.py               # Scheme selection (2019/2024)
    ├── semester.py             # Semester selection (1-8)
    ├── branch.py               # Branch selection handler
    ├── subject.py              # Subject listing by semester
    ├── resources.py            # Resource type selection
    ├── filesender.py           # File delivery system
    ├── search.py               # /search command & subject finder
    ├── request.py              # User request system
    ├── trending.py             # Trending requests display
    ├── back.py                 # Navigation back button
    ├── admin.py                # Admin panel & commands
    ├── admin_upload.py         # Resource upload system
    ├── broadcast.py            # Broadcast messaging
    ├── analytics.py            # /topreq analytics command
    ├── getid.py                # Helper utilities
    ├── replay.py               # Replay/refresh handlers
    └── sanan.py                # Additional utilities
```

### Plugin System

The bot uses Pyrogram's plugin architecture for modular command handling:

```python
# plugins/ directory structure
├── start.py          → /start command
├── admin.py          → /admin, /list, /stats
├── admin_upload.py   → /upload, /done, /delete
├── search.py         → /search command
├── broadcast.py      → /broadcast command
└── ...
```

Each plugin is automatically loaded and contains specific handlers for commands or callback queries.

---

## 🔧 Configuration

### Adding New Subjects

Edit the respective branch file in `data/` directory:

```python
# data/cse.py
CSE = {
    "sem1": [
        "ma101 | Engineering Mathematics I",
        "ph110 | Engineering Physics",
        # Add more subjects here
    ],
    "sem2": [
        # Semester 2 subjects
    ],
    # ... up to sem8
}
```

### Customizing Bot Messages

Edit message templates in plugin files:

```python
# plugins/start.py
START_TEXT = """
🎓 Your Custom Welcome Message Here
"""

# Customize buttons
START_BUTTONS = InlineKeyboardMarkup([...])
```

### Database Configuration

The database schema is automatically created on first run. Tables include:

- `users` - Stores registered user IDs
- `resources` - Stores uploaded resource metadata
- `requests` - Tracks user resource requests

---

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY
);
```

### Resources Table
```sql
CREATE TABLE resources (
    id SERIAL PRIMARY KEY,
    category TEXT,           -- 'notes', 'pyq', 'model', 'video'
    year TEXT,              -- '2019', '2024'
    branch TEXT,            -- 'cse', 'ece', etc.
    semester TEXT,          -- 'sem1', 'sem2', etc.
    subject TEXT,           -- Subject name
    file_id TEXT,           -- Telegram file ID
    file_name TEXT          -- Original filename
);
```

### Requests Table
```sql
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    category TEXT,
    branch TEXT,
    semester TEXT,
    subject TEXT
);
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Add Study Materials**
   - Upload notes, PYQs, or model papers for any subject
   - Contact admins through the bot

2. **Report Issues**
   - Found a bug? [Open an issue](../../issues)
   - Include steps to reproduce and screenshots if possible

3. **Code Contributions**
   ```bash
   # Fork the repository
   # Create a feature branch
   git checkout -b feature/amazing-feature
   
   # Make your changes
   # Commit your changes
   git commit -m "Add amazing feature"
   
   # Push to your fork
   git push origin feature/amazing-feature
   
   # Open a Pull Request
   ```

4. **Documentation**
   - Improve README
   - Add code comments
   - Write tutorials

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Test your changes before submitting PR
- Update documentation if needed

### Subject Data Contribution

To add subjects for a new scheme or branch:

```python
# Create or edit data/<branch>.py
BRANCH_NAME = {
    "sem1": [
        "code | Subject Name",
        # Add all semester 1 subjects
    ],
    "sem2": [...],
    # ... continue for all semesters
}
```

---

## 🐛 Troubleshooting

### Common Issues

**1. Database Connection Error**
```bash
# Check if DATABASE_URL is correct
echo $DATABASE_URL

# Test PostgreSQL connection
psql $DATABASE_URL
```

**2. Bot Not Responding**
```bash
# Check if bot token is valid
# Verify BOT_TOKEN in .env

# Check logs
docker logs ktu-bot
# or
tail -f bot.log
```

**3. Admin Commands Not Working**
```bash
# Verify your user ID in ADMINS
# Get your ID from @userinfobot
# Ensure it matches the ID in .env
```

**4. Files Not Uploading**
```bash
# Ensure bot is admin in LOG_CHANNEL
# Check file size (Telegram limit: 50MB)
# Verify database connection
```

---

## 📈 Roadmap

- [ ] Multi-language support
- [ ] Integration with more branches (MBA, MCA, etc.)
- [ ] Video lecture playlists
- [ ] Exam countdown timer
- [ ] Study group creation feature
- [ ] Assignment submission system
- [ ] Grade calculator
- [ ] Syllabus PDF generation
- [ ] Notification system for new uploads
- [ ] Mobile app version

---

## 🔒 Security & Privacy

- User IDs are stored securely in PostgreSQL
- Admin commands are restricted by user ID verification
- Database credentials should never be committed to git
- Use environment variables for all sensitive data
- Regular backups recommended for production deployments

---

## 🌟 Acknowledgments

- **KTU Students** - For testing and feedback
- **Pyrogram** - Excellent MTProto framework
- **Telegram Bot API** - Powerful bot platform
- **Contributors** - Everyone who helped improve this project

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 KTU Study Bot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 💬 Support & Contact

- **Telegram**: [Contact Developer](https://t.me/yourusername)
- **Issues**: [GitHub Issues](../../issues)
- **Pull Requests**: [Contributions Welcome](../../pulls)
- **Email**: your.email@example.com

---

## ⭐ Show Your Support

If this project helped you or your classmates, please:
- ⭐ **Star** this repository
- 🍴 **Fork** it to contribute
- 📢 **Share** with fellow students
- 💬 **Provide feedback** through issues

---

<p align="center">
  <strong>🎓 Built with ❤️ for KTU Students</strong><br>
  <sub>Helping students access quality educational resources easily</sub>
</p>

<p align="center">
  <a href="#-table-of-contents">Back to Top ⬆️</a>
</p>
