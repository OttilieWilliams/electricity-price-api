from pathlib import Path
from fastapi.testclient import TestClient

from app.main import create_app


def test_mean_price_ok(tmp_path: Path):
    csv_path = tmp_path / "prices.csv"
    csv_path.write_text(
        "state,price,timestamp\n"
        "Vic,10.0,2025-06-24 00:00:00\n"
        "VIC,30.0,2025-06-24 00:30:00\n"
        "NSW,999.0,2025-06-24 00:00:00\n",
        encoding="utf-8",
    )

    client = TestClient(create_app(csv_path=csv_path))
    r = client.get("/prices/mean?state=VIC")

    assert r.status_code == 200
    assert r.json()["mean_price"] == 20.0


def test_unknown_state_404(tmp_path: Path):
    csv_path = tmp_path / "prices.csv"
    csv_path.write_text(
        "state,price,timestamp\n"
        "VIC,10.0,2025-06-24 00:00:00\n",
        encoding="utf-8",
    )

    client = TestClient(create_app(csv_path=csv_path))
    r = client.get("/prices/mean?state=QLD")

    assert r.status_code == 404

