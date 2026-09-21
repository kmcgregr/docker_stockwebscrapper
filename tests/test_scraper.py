from src.scraper import TickerScraper
from unittest import mock
import requests

# Simple example of monkeypatching requests
# In real tests, we'd use responses or httpretn
@mock.patch('src.scraper.requests.get')
def test_fetch_price(mock_get, tmp_path):
    # Mock HTML that contains the first selector
    html = """\
    <html><body>
    <div class='N6SYTe'><span jsname='Pdsbrc'><span>123.45</span></span></div>
    </body></html>
    """
    mock_resp = mock.Mock()
    mock_resp.content = html.encode('utf-8')
    mock_resp.status_code = 200
    mock_get.return_value = mock_resp

    scraper = TickerScraper()
    price = scraper.fetch_price('AAPL:NASDAQ')
    assert price == '123.45'
