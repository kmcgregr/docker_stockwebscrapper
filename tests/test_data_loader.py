import pytest
from src.data_loader import load_tickers

def test_load_tickers(tmp_path):
    file_path = tmp_path / "tickers.csv"
    file_path.write_text("AAPL:NASDAQ\n\nGOOG:NASDAQ\n")
    tickers = load_tickers(str(file_path))
    assert tickers == ["AAPL:NASDAQ", "GOOG:NASDAQ"]
