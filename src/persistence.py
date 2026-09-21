import pandas as pd
import logging

from .config import load_config

logger = logging.getLogger(__name__)

def save_to_excel(rows: list[tuple[str, str]], path: str) -> None:
    """Write rows to an Excel file at path. Overwrites existing file."""
    df = pd.DataFrame(rows, columns=['stock', 'price'])
    df.to_excel(path, index=False)

def save_to_markdown(rows: list[tuple[str, str]], path: str) -> None:
    """Write rows to a Markdown table. Overwrites existing file."""
    header = "| Stock | Price |"
    sep = "|------|-------|"
    lines = [header, sep]
    for stock, price in rows:
        lines.append(f"| {stock} | {price} |")
    content = "\n".join(lines)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Example usage:
# save_to_excel([('AAPL:NASDAQ', '170.00')], 'stock_prices.xlsx')
# save_to_markdown([('AAPL:NASDAQ', '170.00')], 'Stock_prices.md')
