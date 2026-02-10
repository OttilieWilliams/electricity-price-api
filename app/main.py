from pathlib import Path
from fastapi import FastAPI, HTTPException
from app.data_loader import load_prices_by_state, mean

def create_app(csv_path):
    app = FastAPI()

    prices_by_state = load_prices_by_state(csv_path)

    @app.get("/prices/mean")
    def mean_price(state: str):
        key = state.strip().upper()
        prices = prices_by_state.get(key)
        if not prices:
            raise HTTPException(status_code=404, detail=f"State '{key}' not found")

        return {"mean_price": mean(prices)}

    return app

app = create_app(csv_path=Path("data/coding_challenge_prices.csv"))
