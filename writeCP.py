#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Christopher
"""

#write company profile
#https://financialmodelingprep.com/stable/profile

import os
import sys
import requests
import json
from utils import companies, API_KEY, DATA_DIR

def get_company_profile(company):
    url = "https://financialmodelingprep.com/stable/profile"
    resp = requests.get(url, params={"symbol": company, "apikey": API_KEY})
    resp = resp.json()
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(f"{DATA_DIR}/company-profile-{company}.txt", "w") as file:
        json.dump(resp, file, indent=2)


tickers = sys.argv[1:] if len(sys.argv) > 1 else companies
for company in tickers:
    get_company_profile(company)
