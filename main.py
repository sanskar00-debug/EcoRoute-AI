from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse # <-- Added for landing page
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import datetime
import uvicorn

from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Setup
DATABASE_URL = "sqlite:///./ecoroute.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BinModel(Base):
    __tablename__ = "smart_bins"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    fill_level = Column(Float, default=0.0)
    last_updated = Column(String, nullable=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="EcoRoute AI Core Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

class TelemetryUpdate(BaseModel):
    bin_id: int
    fill_level: float

# --- NEW BEAUTIFUL LANDING PAGE ROUTE ---
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EcoRoute AI - Core Engine</title>
        <style>
            body {
                background-color: #0f172a;
                color: #f8fafc;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: screen;
                height: 100vh;
            }
            .card {
                background-color: #1e293b;
                padding: 40px;
                border-radius: 16px;
                border: 1px solid #334155;
                text-align: center;
                max-w: 500px;
                box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.3);
            }
            .badge {
                display: inline-block;
                background-color: rgba(52, 211, 153, 0.1);
                color: #34d399;
                padding: 6px 16px;
                border-radius: 9999px;
                font-size: 12px;
                font-weight: bold;
                margin-bottom: 20px;
                border: 1px solid rgba(52, 211, 153, 0.2);
            }
            h1 {
                font-size: 36px;
                margin: 0 0 10px 0;
                color: #34d399;
                font-weight: 800;
            }
            p {
                color: #94a3b8;
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 30px;
            }
            .btn-group {
                display: flex;
                gap: 16px;
                justify-content: center;
            }
            .btn-primary {
                background-color: #10b981;
                color: #0f172a;
                padding: 12px 24px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                transition: background 0.2s;
            }
            .btn-secondary {
                background-color: #334155;
                color: #f8fafc;
                padding: 12px 24px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                border: 1px solid #475569;
            }
            footer {
                margin-top: 40px;
                font-size: 12px;
                color: #475569;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">● Core Service Engine Active</div>
            <h1>EcoRoute AI</h1>
            <p>Next-generation automated municipal waste optimization engine driven by real-time IoT metrics and routing intelligence.</p>
            <div class="btn-group">
                <a href="/docs" class="btn-primary">Interactive API Docs</a>
                <a href="/api/bins" class="btn-secondary" target="_blank">View JSON Data</a>
            </div>
        </div>
        <footer>© 2026 NextGen Hackathon Submission Team Engine</footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/api/bins")
def get_all_bins(db: Session = Depends(get_db)):
    bins = db.query(BinModel).all()
    if not bins:
        dummy_bins = [
            BinModel(id=1, latitude=40.7128, longitude=-74.0060, fill_level=45.0, last_updated=datetime.datetime.now().isoformat()),
            BinModel(id=2, latitude=40.7258, longitude=-74.0100, fill_level=20.0, last_updated=datetime.datetime.now().isoformat()),
            BinModel(id=3, latitude=40.7188, longitude=-73.9980, fill_level=70.0, last_updated=datetime.datetime.now().isoformat()),
        ]
        db.add_all(dummy_bins)
        db.commit()
        bins = db.query(BinModel).all()
    return bins

@app.post("/api/telemetry")
def receive_telemetry(payload: TelemetryUpdate, db: Session = Depends(get_db)):
    db_bin = db.query(BinModel).filter(BinModel.id == payload.bin_id).first()
    if not db_bin:
        db_bin = BinModel(id=payload.bin_id, latitude=40.7128, longitude=-74.0060, fill_level=payload.fill_level, last_updated=datetime.datetime.now().isoformat())
        db.add(db_bin)
    else:
        db_bin.fill_level = payload.fill_level
        db_bin.last_updated = datetime.datetime.now().isoformat()
    db.commit()
    return {"status": "Success"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)