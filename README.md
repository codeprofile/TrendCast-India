
# 🎙️ TrendCast-India

> **भारतीय बाजार की धड़कन, आपकी आवाज़ में**  
> *India's Market Pulse, In Your Voice*

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

An intelligent, multi-agent AI system that autonomously monitors Indian stock market indices, extracts verified data from official financial sources (RBI, SEBI, NSE, BSE), and generates professional podcast episodes in multiple Indian languages explaining market movements with data-backed justifications.



https://github.com/user-attachments/assets/9b57f11d-35e0-4baf-a8c2-6776c435394b



---





## 🌟 Features

### 🤖 **Multi-Agent AI Architecture**
- **Trend Analyzer Agent** - Analyzes Indian market indices with technical indicators
- **Data Collector Agent** - Scrapes official Indian sources (RBI, SEBI, NSE, BSE, Ministry of Finance)
- **Script Writer Agent** - Generates contextual podcast scripts with LLM
- **Podcaster Agent** - Converts scripts to natural-sounding audio in Indian languages

### 📊 **Indian Market Focus**
- **Major Indices**: NIFTY 50, SENSEX, NIFTY Bank, NIFTY IT
- **Sectoral Coverage**: Auto, Pharma, FMCG, Metal, Midcap, Smallcap
- **Indian-Specific Data**: FII/DII flows, INR/USD rates, India VIX, GST collections
- **Official Sources**: 100% verified data from RBI, SEBI, NSE, BSE

### 🌐 **Multi-Language Support**
- **English** - For urban, English-speaking investors
- **Hindi** - For Hindi-speaking retail investors
- **Hinglish** - Popular mix for bilingual audience
- **Coming Soon**: Tamil, Telugu, Marathi, Gujarati, Bengali

### 🎨 **Modern Tech Stack**
- **Backend**: FastAPI (Python) - High-performance async API
- **Frontend**: Vanilla HTML/CSS/JS - No framework dependencies
- **Real-time**: WebSocket support for live updates
- **Scalable**: Ready for cloud deployment

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/codeprofile/TrendCast-India
cd trendcast-india

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt

# Copy environment variables
cp .env.example .env
# Edit .env and add your API keys (optional for demo)

# Run the application
cd backend
python main.py
```

### Access the Application
Open your browser and navigate to:
```
http://localhost:8000
```

---

## 📖 Usage

### Web Interface

1. **Select Market Index** - Choose from NIFTY 50, SENSEX, or sectoral indices
2. **Choose Language** - Select English, Hindi, or Hinglish
3. **Click Analyze** - Watch the AI agents work in real-time
4. **Review Results** - See trend data, economic indicators, and generated script
5. **Download Podcast** - Get the audio file for offline listening


## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     TrendCast India                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │   Frontend   │───▶│  FastAPI     │───▶│   Agents     │ │
│  │ HTML/CSS/JS  │◀───│   Backend    │◀───│   Pipeline   │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
│                                                  │          │
│                                                  ▼          │
│  ┌────────────────────────────────────────────────────┐    │
│  │              Agent 1: Trend Analyzer           │    │
│  │  • NSE/BSE price data                          │    │
│  │  • Technical indicators (RSI, MACD, etc.)      │    │
│  │  • FII/DII flows                               │    │
│  │  • India VIX                                   │    │
│  └────────────────────────────────────────────────────┘    │
│                          ▼                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │             Agent 2: Data Collector            │    │
│  │  • RBI: Repo rate, inflation                   │    │
│  │  • SEBI: Regulations, FPI data                 │    │
│  │  • Ministry of Finance: GST, fiscal deficit    │    │
│  │  • MOSPI: GDP, IIP, PMI                        │    │
│  └────────────────────────────────────────────────────┘    │
│                          ▼                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │              Agent 3: Script Writer            │    │
│  │  • LLM-powered script generation               │    │
│  │  • Multi-language support                      │    │
│  │  • Context-aware analysis                      │    │
│  │  • Source attribution                          │    │
│  └────────────────────────────────────────────────────┘    │
│                          ▼                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │               Agent 4: Podcaster               │    │
│  │  • Text-to-Speech (Indian voices)              │    │
│  │  • Audio quality optimization                  │    │
│  │  • Multi-format export (MP3, AAC)              │    │
│  │  • Distribution (RSS, Spotify, YouTube)        │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
trendcast-india/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── trend_analyzer.py   # Market analysis agent
│   │   ├── data_collector.py   # Data scraping agent
│   │   ├── script_writer.py    # Script generation agent
│   │   └── podcaster.py        # Audio generation agent
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py          # Pydantic data models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── nse_api.py          # NSE data fetching
│   │   ├── rbi_scraper.py      # RBI data scraping
│   │   ├── llm_service.py      # LLM integration
│   │   └── tts_service.py      # Text-to-Speech
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py          # Helper functions
│   └── requirements.txt
├── frontend/
│   └── static/
│       └── index.html          # Single-page frontend
├── tests/
│   ├── test_agents.py
│   ├── test_api.py
│   └── test_integration.py
├── audio/                      # Generated podcast files
├── logs/                       # Application logs
├── docs/
│   ├── SETUP.md               # Detailed setup guide
│   ├── API.md                 # API documentation
│   └── DEPLOYMENT.md          # Deployment guide
├── .env.example               # Environment variables template
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# API Keys (required for production)
GOOGLE_API_KEY=your_openai_key_here
ELEVENLABS_API_KEY=your_elevenlabs_key_here

# Application Settings
APP_ENV=development
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=True

# Data Sources
NSE_API_URL=https://www.nseindia.com
BSE_API_URL=https://www.bseindia.com
RBI_URL=https://www.rbi.org.in
SEBI_URL=https://www.sebi.gov.in

# Rate Limiting
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_PERIOD=3600

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/trendcast.log
```

---



## 🙏 Acknowledgments

- **NSE India** - For market data access
- **RBI** - For economic indicators
- **SEBI** - For regulatory information
- **Google ADK** - For LLM capabilities
- **ElevenLabs** - For voice synthesis technology
- **FastAPI Community** - For the amazing framework

---




<div align="center">

**Made with ❤️ in India for Indian Investors**

</div>
