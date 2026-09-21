import pandas as pd
from src.persistence import save_to_excel, save_to_markdown
import os

def test_persistence(tmp_path):
    rows = [('AAPL:NASDAQ', '123.45'), ('GOOG:NASDAQ', '67.89')]
    excel_path = tmp_path / 'prices.xlsx'
    md_path = tmp_path / 'prices.md'
    save_to_excel(rows, str(excel_path))
    save_to_markdown(rows, str(md_path))
    assert os.path.exists(excel_path)
    assert os.path.exists(md_path)
    df = pd.read_excel(str(excel_path))
    assert list(df['stock']) == ['AAPL:NASDAQ', 'GOOG:NASDAQ']
    md = md_path.read_text()
    assert '| AAPL:NASDAQ | 123.45 |' in md
