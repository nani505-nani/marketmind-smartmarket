from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random

app = FastAPI(title="MarketMind API")

# Allow the React frontend to talk to this backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Your React app's URL
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
        {"id": 1, "name": "Ergonomic Standing Desk", "category": "Office", "status": "Rising Fast"},
        {"id": 2, "name": "Matcha Whisk Set", "category": "Kitchen", "status": "Steady Growth"},
        {"id": 3, "name": "Portable Solar Charger", "category": "Electronics", "status": "Rising Fast"},
    ]
    
    # Adding dynamic trend scores using our 'AI' function
    for item in trending_items:
        item["trendScore"] = calculate_trend_score(item["name"])
        
    return trending_items

@app.post("/api/analyze")
async def analyze_custom_product(product_name: str):
    # Endpoint to allow users to check a specific product not in the list
    score = calculate_trend_score(product_name)
    return {
        "product": product_name,
        "score": score,
        "recommendation": "Invest" if score > 80 else "Watch closely"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)