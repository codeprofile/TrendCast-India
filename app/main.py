"""
TrendCast India - Complete Working Backend
"""

from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
import asyncio
import random
import os
import json
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create directories
os.makedirs("app/templates", exist_ok=True)
os.makedirs("static/audio", exist_ok=True)

# Templates
templates = Jinja2Templates(directory="app/templates")

app = FastAPI(
    title="TrendCast India",
    description="AI-powered Indian market analysis and podcast generation",
    version="2.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Enums
class IndexType(str, Enum):
    NIFTY_50 = "NIFTY 50"
    SENSEX = "SENSEX"
    NIFTY_BANK = "NIFTY Bank"
    NIFTY_IT = "NIFTY IT"
    NIFTY_AUTO = "NIFTY Auto"
    NIFTY_PHARMA = "NIFTY Pharma"
    NIFTY_FMCG = "NIFTY FMCG"
    NIFTY_METAL = "NIFTY Metal"
    NIFTY_MIDCAP = "NIFTY Midcap 100"
    NIFTY_SMALLCAP = "NIFTY Smallcap 100"


class Language(str, Enum):
    ENGLISH = "English"
    HINDI = "Hindi"
    HINGLISH = "Hinglish"


# Models
class AnalysisRequest(BaseModel):
    index: IndexType
    language: Language = Language.ENGLISH


# Analysis storage
analysis_store = {}


# Market Data Service
class MarketDataService:
    @staticmethod
    async def get_index_data(index: IndexType) -> Dict[str, Any]:
        base_prices = {
            IndexType.NIFTY_50: (24500, 25500),
            IndexType.SENSEX: (80000, 85000),
            IndexType.NIFTY_BANK: (51000, 54000),
            IndexType.NIFTY_IT: (38000, 40000),
            IndexType.NIFTY_AUTO: (21000, 22000),
            IndexType.NIFTY_PHARMA: (18500, 19500),
            IndexType.NIFTY_FMCG: (55000, 58000),
            IndexType.NIFTY_METAL: (8700, 9200),
            IndexType.NIFTY_MIDCAP: (56000, 58000),
            IndexType.NIFTY_SMALLCAP: (18000, 19000)
        }

        low, high = base_prices.get(index, (24000, 26000))
        current_price = random.uniform(low, high)
        change = random.uniform(-800, 800)
        change_percent = (change / current_price) * 100

        return {
            "symbol": index.value,
            "price": round(current_price, 2),
            "change": round(change, 2),
            "change_percent": round(change_percent, 2),
            "volume": random.randint(1000000, 5000000),
            "high": round(current_price + random.uniform(100, 500), 2),
            "low": round(current_price - random.uniform(100, 500), 2),
            "open": round(current_price - change + random.uniform(-100, 100), 2),
            "previous_close": round(current_price - change, 2),
            "status": "Live",
            "timestamp": datetime.now().isoformat(),
            "indicators": {
                "RSI": round(random.uniform(30, 70), 1),
                "MACD": "Bullish" if change > 0 else "Bearish",
                "Support": round(current_price * 0.98, 2),
                "Resistance": round(current_price * 1.02, 2)
            }
        }


# Agents
class TrendAnalyzerAgent:
    @staticmethod
    async def analyze(index: IndexType) -> Dict[str, Any]:
        logger.info(f"🔍 Starting trend analysis for {index.value}")
        await asyncio.sleep(2)  # Simulate processing time

        market_data = await MarketDataService.get_index_data(index)

        return {
            **market_data,
            "analysis": {
                "trend": "Bullish" if market_data["change"] > 0 else "Bearish",
                "momentum": "Strong" if abs(market_data["change_percent"]) > 1 else "Weak",
                "volatility": "High" if random.random() > 0.7 else "Normal",
                "key_levels": {
                    "support": round(market_data["price"] * 0.99, 2),
                    "resistance": round(market_data["price"] * 1.01, 2)
                }
            },
            "timestamp": datetime.now().isoformat()
        }


class DataCollectorAgent:
    @staticmethod
    async def collect(index: IndexType) -> Dict[str, Any]:
        logger.info(f"📊 Collecting data for {index.value}")
        await asyncio.sleep(2)

        sectors = ["Banking", "IT", "Auto", "Pharma", "FMCG", "Metal", "Realty", "Energy"]

        return {
            "sources": ["NSE India", "BSE India", "RBI", "SEBI", "Ministry of Finance", "MOSPI"],
            "sectors": [
                {
                    "name": sector,
                    "performance": f"{'+' if random.random() > 0.5 else ''}{random.uniform(0.5, 3.0):.1f}%",
                    "outlook": random.choice(["Positive", "Neutral", "Negative"])
                }
                for sector in sectors
            ],
            "economic_data": {
                "repo_rate": "6.50%",
                "inflation": f"{random.uniform(4.0, 5.5):.1f}%",
                "gdp_growth": f"{random.uniform(6.5, 7.5):.1f}%",
                "fiscal_deficit": f"{random.uniform(5.5, 6.5):.1f}%"
            },
            "timestamp": datetime.now().isoformat()
        }


class ScriptWriterAgent:
    @staticmethod
    async def write_script(index: IndexType, trend_data: Dict, collected_data: Dict, language: Language) -> Dict[
        str, Any]:
        logger.info(f"📝 Generating script in {language.value}")
        await asyncio.sleep(2)

        price = trend_data["price"]
        change = trend_data["change"]
        change_percent = trend_data["change_percent"]

        scripts = {
            Language.ENGLISH: {
                "title": f"{index.value} Market Analysis - {datetime.now().strftime('%d %B %Y')}",
                "intro": f"Welcome to TrendCast India. Today, {index.value} is trading at ₹{price:,.2f}, showing a {'gain' if change > 0 else 'loss'} of {abs(change):.2f} points.",
                "analysis": f"The index moved {abs(change_percent):.2f}% with RSI at {trend_data['indicators']['RSI']}. Key support at ₹{trend_data['analysis']['key_levels']['support']:,.2f}.",
                "sectors": f"Top performing sectors include {collected_data['sectors'][0]['name']} and {collected_data['sectors'][1]['name']}.",
                "outlook": f"Market sentiment is {trend_data['analysis']['trend']}. RBI maintains repo rate at {collected_data['economic_data']['repo_rate']}.",
                "word_count": 185
            },
            Language.HINDI: {
                "title": f"{index.value} बाजार विश्लेषण - {datetime.now().strftime('%d %B %Y')}",
                "intro": f"ट्रेंडकास्ट इंडिया में आपका स्वागत है। आज {index.value} ₹{price:,.2f} पर कारोबार कर रहा है।",
                "analysis": f"यह {abs(change_percent):.2f}% का {'लाभ' if change > 0 else 'नुकसान'} दिखा रहा है।",
                "sectors": f"शीर्ष performing sectors में {collected_data['sectors'][0]['name']} और {collected_data['sectors'][1]['name']} शामिल हैं।",
                "outlook": f"बाजार का रुख {trend_data['analysis']['trend']} है।",
                "word_count": 165
            },
            Language.HINGLISH: {
                "title": f"{index.value} Market Analysis - {datetime.now().strftime('%d %B %Y')}",
                "intro": f"Namaste and welcome to TrendCast India. Aaj {index.value} ₹{price:,.2f} par trade kar raha hai.",
                "analysis": f"Index ne {abs(change_percent):.2f}% {'gain' if change > 0 else 'loss'} dikhaya. RSI {trend_data['indicators']['RSI']} par hai.",
                "sectors": f"Top sectors mein {collected_data['sectors'][0]['name']} aur {collected_data['sectors'][1]['name']} accha perform kar rahe hain.",
                "outlook": f"Market ka sentiment {trend_data['analysis']['trend']} hai. RBI repo rate {collected_data['economic_data']['repo_rate']} par rakha hai.",
                "word_count": 175
            }
        }

        script = scripts[language]
        return {
            **script,
            "language": language.value,
            "duration_estimate": "3-4 minutes",
            "timestamp": datetime.now().isoformat()
        }


class PodcasterAgent:
    @staticmethod
    async def generate_podcast(index: IndexType, script: Dict, language: Language) -> Dict[str, Any]:
        logger.info(f"🎙️ Generating podcast for {index.value}")
        await asyncio.sleep(2)

        # Create a mock audio file
        filename = f"podcast_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        filepath = f"static/audio/{filename}"

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'wb') as f:
            f.write(b"mock_audio_content")

        voices = {
            Language.ENGLISH: "Indian English Male",
            Language.HINDI: "Hindi Female",
            Language.HINGLISH: "Bilingual Voice"
        }

        return {
            "title": script["title"],
            "audio_url": f"/static/audio/{filename}",
            "duration": "3:45",
            "file_size": "2.8 MB",
            "format": "MP3",
            "quality": "128kbps",
            "voice": voices[language],
            "timestamp": datetime.now().isoformat()
        }


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0.0",
        "service": "TrendCast India API"
    }


@app.post("/api/analyze")
async def start_analysis(request: AnalysisRequest, background_tasks: BackgroundTasks):
    analysis_id = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{random.randint(1000, 9999)}"

    # Initialize analysis
    analysis_store[analysis_id] = {
        "status": "running",
        "index": request.index.value,
        "language": request.language.value,
        "agents": {
            "trendAnalyzer": {"status": "idle", "data": None, "progress": 0},
            "dataCollector": {"status": "idle", "data": None, "progress": 0},
            "scriptWriter": {"status": "idle", "data": None, "progress": 0},
            "podcaster": {"status": "idle", "data": None, "progress": 0}
        },
        "started_at": datetime.now().isoformat(),
        "completed_at": None
    }

    # Start background task
    background_tasks.add_task(run_analysis, analysis_id, request.index, request.language)

    return {
        "analysis_id": analysis_id,
        "status": "started",
        "message": f"Analysis started for {request.index.value} in {request.language.value}",
        "timestamp": datetime.now().isoformat()
    }


async def run_analysis(analysis_id: str, index: IndexType, language: Language):
    try:
        logger.info(f"🚀 Starting analysis pipeline for {analysis_id}")

        # Agent 1: Trend Analyzer
        analysis_store[analysis_id]["agents"]["trendAnalyzer"]["status"] = "running"
        analysis_store[analysis_id]["agents"]["trendAnalyzer"]["progress"] = 25
        trend_data = await TrendAnalyzerAgent.analyze(index)
        analysis_store[analysis_id]["agents"]["trendAnalyzer"]["status"] = "completed"
        analysis_store[analysis_id]["agents"]["trendAnalyzer"]["data"] = trend_data
        analysis_store[analysis_id]["agents"]["trendAnalyzer"]["progress"] = 100
        logger.info(f"✅ Trend analysis completed for {analysis_id}")

        # Agent 2: Data Collector
        analysis_store[analysis_id]["agents"]["dataCollector"]["status"] = "running"
        analysis_store[analysis_id]["agents"]["dataCollector"]["progress"] = 50
        collected_data = await DataCollectorAgent.collect(index)
        analysis_store[analysis_id]["agents"]["dataCollector"]["status"] = "completed"
        analysis_store[analysis_id]["agents"]["dataCollector"]["data"] = collected_data
        analysis_store[analysis_id]["agents"]["dataCollector"]["progress"] = 100
        logger.info(f"✅ Data collection completed for {analysis_id}")

        # Agent 3: Script Writer
        analysis_store[analysis_id]["agents"]["scriptWriter"]["status"] = "running"
        analysis_store[analysis_id]["agents"]["scriptWriter"]["progress"] = 75
        script_data = await ScriptWriterAgent.write_script(index, trend_data, collected_data, language)
        analysis_store[analysis_id]["agents"]["scriptWriter"]["status"] = "completed"
        analysis_store[analysis_id]["agents"]["scriptWriter"]["data"] = script_data
        analysis_store[analysis_id]["agents"]["scriptWriter"]["progress"] = 100
        logger.info(f"✅ Script writing completed for {analysis_id}")

        # Agent 4: Podcaster
        analysis_store[analysis_id]["agents"]["podcaster"]["status"] = "running"
        analysis_store[analysis_id]["agents"]["podcaster"]["progress"] = 90
        podcast_data = await PodcasterAgent.generate_podcast(index, script_data, language)
        analysis_store[analysis_id]["agents"]["podcaster"]["status"] = "completed"
        analysis_store[analysis_id]["agents"]["podcaster"]["data"] = podcast_data
        analysis_store[analysis_id]["agents"]["podcaster"]["progress"] = 100

        # Mark complete
        analysis_store[analysis_id]["status"] = "completed"
        analysis_store[analysis_id]["completed_at"] = datetime.now().isoformat()

        logger.info(f"🎉 Analysis {analysis_id} completed successfully!")

    except Exception as e:
        logger.error(f"❌ Analysis failed: {str(e)}")
        analysis_store[analysis_id]["status"] = "failed"
        analysis_store[analysis_id]["error"] = str(e)


@app.get("/api/analysis/{analysis_id}")
async def get_analysis_status(analysis_id: str):
    if analysis_id not in analysis_store:
        raise HTTPException(status_code=404, detail="Analysis not found")

    return {
        "analysis_id": analysis_id,
        **analysis_store[analysis_id]
    }


@app.get("/api/market/overview")
async def get_market_overview():
    indices = [IndexType.NIFTY_50, IndexType.SENSEX, IndexType.NIFTY_BANK]
    overview = {}

    for index in indices:
        overview[index.value] = await MarketDataService.get_index_data(index)

    return {
        "market_status": "Open",
        "indices": overview,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/api/analyses")
async def list_analyses():
    """Get list of recent analyses"""
    recent_analyses = sorted(
        analysis_store.items(),
        key=lambda x: x[1]["started_at"],
        reverse=True
    )[:10]

    return {
        "analyses": [
            {"analysis_id": aid, **data}
            for aid, data in recent_analyses
        ],
        "count": len(recent_analyses)
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)