from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.apis import producers, categories, products, sales, update_stock, update_prices

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(producers.router, prefix="")
app.include_router(categories.router, prefix="")
app.include_router(products.router, prefix="")
app.include_router(sales.router, prefix="")
app.include_router(update_stock.router, prefix="")
app.include_router(update_prices.router, prefix="")


@app.get("/")
async def read_root():
    return {"Hello": "World"}