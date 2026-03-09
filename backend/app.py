from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random
import os

app = FastAPI(title="MarketMind API")

# Allow the React frontend to talk to this backend (CORS)
allow_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for a Product
class Product(BaseModel):
    id: int
    name: str
    category: str
    trendScore: int
    status: str

# Data model for product analysis request
class ProductAnalysisRequest(BaseModel):
    product_name: str

# Mock Database / Trend Analysis Logic
def calculate_trend_score(product_name: str):
    """
    This is where your AI model would live. 
    In a real app, you'd use a library like Scikit-learn or PyTorch 
    to analyze search volume and social data here.
    """
    return random.randint(50, 99)

@app.get("/api/trends", response_model=List[Product])
async def get_trending_products():
    # In a real app, this data would come from a database like PostgreSQL or MongoDB
    trending_items = [
        Product(id=1, name="Ergonomic Standing Desk", category="Office", trendScore=calculate_trend_score("Ergonomic Standing Desk"), status="Rising Fast"),
        Product(id=2, name="Matcha Whisk Set", category="Kitchen", trendScore=calculate_trend_score("Matcha Whisk Set"), status="Steady Growth"),
        Product(id=3, name="Portable Solar Charger", category="Electronics", trendScore=calculate_trend_score("Portable Solar Charger"), status="Rising Fast"),
    ]
    
    return trending_items

@app.post("/api/analyze")
async def analyze_custom_product(request: ProductAnalysisRequest):
    # Endpoint to allow users to check a specific product not in the list
    score = calculate_trend_score(request.product_name)
    return {
        "product": request.product_name,
        "score": score,
        "recommendation": "Invest" if score > 80 else "Watch closely"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)