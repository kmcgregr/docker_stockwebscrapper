def load_tickers(file_path: str) -> list[str]:
    """Read a CSV file with one ticker per line.
    Strips whitespace and ignores empty lines.
    Returns a list of ticker strings.
    """
    tickers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                cleaned = line.strip()
                if cleaned:
                    tickers.append(cleaned)
    except FileNotFoundError:
        raise RuntimeError(f"Ticker file not found: {file_path}")
    return tickers

# Example usage: tickers = load_tickers('stockwebscrapper/my_stocks.csv')
