# ETF and Stock Prices

## Cleaned Data Table

| Ticker | Exchange | Full Symbol | Price | Type / Sector Note |
| :--- | :--- | :--- | :--- | :--- |
| CHR | TSE | CHR:TSE | $28.32 | Stock |
| GWO | TSE | GWO:TSE | $93.52 | Stock |
| CGX | TSE | CGX:TSE | $12.39 | Stock |
| BB | TSE | BB:TSE | $11.16 | Stock |
| WCP | TSE | WCP:TSE | $18.86 | Stock |
| TLRY | TSE | TLRY:TSE | $5.59 | Stock |
| PXT | TSE | PXT:TSE | $28.36 | Stock |
| AC | TSE | AC:TSE | $28.26 | Stock |
| XMA | TSE | XMA:TSE | $48.67 | ETF (iShares Cdn Materials Sector Index) |
| BEN | NYSE | BEN:NYSE | $33.01 | Stock |
| ACB | TSE | ACB:TSE | $5.40 | Stock |
| OGI | TSE | OGI:TSE | $1.44 | Stock |
| POU | TSE | POU:TSE | $32.21 | Stock |
| ASM | TSE | ASM:TSE | $8.94 | Stock |
| QCLN | NASDAQ | QCLN:NASDAQ | $47.82 | ETF (First Trust NASDAQ Clean Edge Green Energy) |
| VCNX | OTCMKTS | VCNX:OTCMKTS | $1.00 | Stock |
| AMAT | NASDAQ | AMAT:NASDAQ | $444.57 | Stock |
| QQC | TSE | QQC:TSE | $49.31 | ETF (Invesco NASDAQ 100 Index) |
| XUS | TSE | XUS:TSE | $66.17 | ETF (iShares Core S&P 500 Index) |
| XIC | TSE | XIC:TSE | $57.33 | ETF (iShares Core S&P/TSX Capped Composite) |
| XMC | TSE | XMC:TSE | $39.24 | ETF (iShares S&P/TSX Completion Index) |
| XHU | TSE | XHU:TSE | $41.04 | ETF (iShares U.S. High Dividend Index CAD-Hedged) |
| XDIV | TSE | XDIV:TSE | $46.31 | ETF (iShares Core MSCI Canadian Quality Dividend Index) |
| XEQT | TSE | XEQT:TSE | $45.41 | ETF (iShares Core Equity ETF Portfolio) |
| VDY | TSE | VDY:TSE | $77.17 | ETF (Vanguard Canadian High Dividend Yield Index) |
| TGRO | TSE | TGRO:TSE | $29.43 | ETF (TD Growth ETF Portfolio) |
| XEI | TSE | XEI:TSE | $39.75 | ETF (iShares Core S&P/TSX Composite High Dividend Index) |
| IONQ | NYSE | IONQ:NYSE | $39.13 | Stock |
| AKT | TSE | AKT:TSE | $3.81 | Stock |
| HURA | TSE | HURA:TSE | $47.50 | ETF (Horizons Uranium Index ETF) |
| ZEQT | TSE | ZEQT:TSE | $23.39 | ETF (BMO All-Equity ETF Portfolio) |
| CHPS | TSE | CHPS:TSE | $84.14 | ETF (Horizons Global Semiconductor Index ETF) |
| TEC | TSE | TEC:TSE | $62.46 | ETF (TD Global Technology Leaders Index ETF) |

---

## Machine-Readable Formats

### JSON Array Format
```json
[
  {"ticker": "CHR", "exchange": "TSE", "symbol": "CHR:TSE", "price": 28.32, "is_etf": false},
  {"ticker": "GWO", "exchange": "TSE", "symbol": "GWO:TSE", "price": 93.52, "is_etf": false},
  {"ticker": "CGX", "exchange": "TSE", "symbol": "CGX:TSE", "price": 12.39, "is_etf": false},
  {"ticker": "BB", "exchange": "TSE", "symbol": "BB:TSE", "price": 11.16, "is_etf": false},
  {"ticker": "WCP", "exchange": "TSE", "symbol": "WCP:TSE", "price": 18.86, "is_etf": false},
  {"ticker": "TLRY", "exchange": "TSE", "symbol": "TLRY:TSE", "price": 5.59, "is_etf": false},
  {"ticker": "PXT", "exchange": "TSE", "symbol": "PXT:TSE", "price": 28.36, "is_etf": false},
  {"ticker": "AC", "exchange": "TSE", "symbol": "AC:TSE", "price": 28.26, "is_etf": false},
  {"ticker": "XMA", "exchange": "TSE", "symbol": "XMA:TSE", "price": 48.67, "is_etf": true},
  {"ticker": "BEN", "exchange": "NYSE", "symbol": "BEN:NYSE", "price": 33.01, "is_etf": false},
  {"ticker": "ACB", "exchange": "TSE", "symbol": "ACB:TSE", "price": 5.40, "is_etf": false},
  {"ticker": "OGI", "exchange": "TSE", "symbol": "OGI:TSE", "price": 1.44, "is_etf": false},
  {"ticker": "POU", "exchange": "TSE", "symbol": "POU:TSE", "price": 32.21, "is_etf": false},
  {"ticker": "ASM", "exchange": "TSE", "symbol": "ASM:TSE", "price": 8.94, "is_etf": false},
  {"ticker": "QCLN", "exchange": "NASDAQ", "symbol": "QCLN:NASDAQ", "price": 47.82, "is_etf": true},
  {"ticker": "VCNX", "exchange": "OTCMKTS", "symbol": "VCNX:OTCMKTS", "price": 1.00, "is_etf": false},
  {"ticker": "AMAT", "exchange": "NASDAQ", "symbol": "AMAT:NASDAQ", "price": 444.57, "is_etf": false},
  {"ticker": "QQC", "exchange": "TSE", "symbol": "QQC:TSE", "price": 49.31, "is_etf": true},
  {"ticker": "XUS", "exchange": "TSE", "symbol": "XUS:TSE", "price": 66.17, "is_etf": true},
  {"ticker": "XIC", "exchange": "TSE", "symbol": "XIC:TSE", "price": 57.33, "is_etf": true},
  {"ticker": "XMC", "exchange": "TSE", "symbol": "XMC:TSE", "price": 39.24, "is_etf": true},
  {"ticker": "XHU", "exchange": "TSE", "symbol": "XHU:TSE", "price": 41.04, "is_etf": true},
  {"ticker": "XDIV", "exchange": "TSE", "symbol": "XDIV:TSE", "price": 46.31, "is_etf": true},
  {"ticker": "XEQT", "exchange": "TSE", "symbol": "XEQT:TSE", "price": 45.41, "is_etf": true},
  {"ticker": "VDY", "exchange": "TSE", "symbol": "VDY:TSE", "price": 77.17, "is_etf": true},
  {"ticker": "TGRO", "exchange": "TSE", "symbol": "TGRO:TSE", "price": 29.43, "is_etf": true},
  {"ticker": "XEI", "exchange": "TSE", "symbol": "XEI:TSE", "price": 39.75, "is_etf": true},
  {"ticker": "IONQ", "exchange": "NYSE", "symbol": "IONQ:NYSE", "price": 39.13, "is_etf": false},
  {"ticker": "AKT", "exchange": "TSE", "symbol": "AKT:TSE", "price": 3.81, "is_etf": false},
  {"ticker": "HURA", "exchange": "TSE", "symbol": "HURA:TSE", "price": 47.50, "is_etf": true},
  {"ticker": "ZEQT", "exchange": "TSE", "symbol": "ZEQT:TSE", "price": 23.39, "is_etf": true},
  {"ticker": "CHPS", "exchange": "TSE", "symbol": "CHPS:TSE", "price": 84.14, "is_etf": true},
  {"ticker": "TEC", "exchange": "TSE", "symbol": "TEC:TSE", "price": 62.46, "is_etf": true}
]
```

### CSV Format
```csv
ticker,exchange,symbol,price,is_etf
CHR,TSE,CHR:TSE,28.32,false
GWO,TSE,GWO:TSE,93.52,false
CGX,TSE,CGX:TSE,12.39,false
BB,TSE,BB:TSE,11.16,false
WCP,TSE,WCP:TSE,18.86,false
TLRY,TSE,TLRY:TSE,5.59,false
PXT,TSE,PXT:TSE,28.36,false
AC,TSE,AC:TSE,28.26,false
XMA,TSE,XMA:TSE,48.67,true
BEN,NYSE,BEN:NYSE,33.01,false
ACB,TSE,ACB:TSE,5.40,false
OGI,TSE,OGI:TSE,1.44,false
POU,TSE,POU:TSE,32.21,false
ASM,TSE,ASM:TSE,8.94,false
QCLN,NASDAQ,QCLN:NASDAQ,47.82,true
VCNX,OTCMKTS,VCNX:OTCMKTS,1.00,false
AMAT,NASDAQ,AMAT:NASDAQ,444.57,false
QQC,TSE,QQC:TSE,49.31,true
XUS,TSE,XUS:TSE,66.17,true
XIC,TSE,XIC:TSE,57.33,true
XMC,TSE,XMC:TSE,39.24,true
XHU,TSE,XHU:TSE,41.04,true
XDIV,TSE,XDIV:TSE,46.31,true
XEQT,TSE,XEQT:TSE,45.41,true
VDY,TSE,VDY:TSE,77.17,true
TGRO,TSE,TGRO:TSE,29.43,true
XEI,TSE,XEI:TSE,39.75,true
IONQ,NYSE,IONQ:NYSE,39.13,false
AKT,TSE,AKT:TSE,3.81,false
HURA,TSE,HURA:TSE,47.50,true
ZEQT,TSE,ZEQT:TSE,23.39,true
CHPS,TSE,CHPS:TSE,84.14,true
TEC,TSE,TEC:TSE,62.46,true
```