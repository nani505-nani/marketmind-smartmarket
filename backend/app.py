from pydantic import BaseModel, Field

class ProductAnalysisRequest(BaseModel):
    product_id: str = Field(..., description="The ID of the product")
    quantity: int = Field(..., description="The quantity of the product")

@app.post('/analyze-product')
def analyze_product(request: ProductAnalysisRequest):
    # Fixed to accept body instead of query
    product_id = request.product_id
    quantity = request.quantity
    
    # Your analysis logic here
    return {"product_id": product_id, "quantity": quantity, "message": "Analysis completed successfully."}