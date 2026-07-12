#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Christopher
"""

import os
import sys
import requests
import json
from utils import companies, API_KEY, DATA_DIR

def get_balance_sheet(company):
    url = "https://financialmodelingprep.com/stable/balance-sheet-statement"
    resp = requests.get(url, params={"symbol": company, "limit": 5, "apikey": API_KEY})
    resp = resp.json()
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(f"{DATA_DIR}/balance-sheet-{company}.txt", "w") as file:
        json.dump(resp, file, indent=2)


tickers = sys.argv[1:] if len(sys.argv) > 1 else companies
for company in tickers:
    get_balance_sheet(company)
