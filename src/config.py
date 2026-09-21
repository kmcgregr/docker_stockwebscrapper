import sys
import yaml
import os

def load_config(path: str = 'config.yaml') -> dict:
    """Load YAML configuration into a dictionary.
    Falls back to hard‑coded defaults if file missing or malformed.
    """
    default = {
        'scraper': {
            'url_template': 'https://www.google.com/finance/beta/quote/{ticker}',
            'selectors': [
                "div.N6SYTe > span[jsname='Pdsbrc'] > span",
                "div.YMlKec.fxKbKc"
            ],
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            },
            'currency_strip': ['CA']
        },
        'schedule': {
            'minutes': 10,
            'daily_at': '17:00',
            'weekly_day': 'monday'
        },
        'persistence': {
            'excel': 'stock_prices.xlsx',
            'markdown': 'Stock_prices.md'
        }
    }
    try:
        with open(path, 'r', encoding='utf-8') as f:
            cfg = yaml.safe_load(f)
    except Exception:
        return default
    # Merge defaults: only overwrite keys present in file
    def merge(d, m):
        for k, v in m.items():
            if isinstance(v, dict) and k in d:
                merge(d[k], v)
            else:
                d[k] = v
    merge(default, cfg)
    return default

if __name__ == '__main__':
    print(load_config())
