#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

"""

@author: Christopher
"""
# FOR BACKTESTING IN 2015 HIDE COMPANIES:
DATA_DIR = "data"


def _load_api_key():
    key = os.environ.get("FMP_API_KEY")
    if key:
        return key
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("FMP_API_KEY="):
                    return line.split("=", 1)[1].strip()
    return None


API_KEY = _load_api_key()

companies = [
    
 'MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ATVI', 'AYI', 'ADBE', 
 #'AAP', 
 'AMD', 'AES', 
 #'AET', 
 #'AMG', 
 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', #'ARE', 
 'ALXN', 'ALGN', 'ALLE', 'AGN', 'ADS', 'LNT', 'ALL', 'GOOGL', #'GOOG', 
 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', #'AXP', 
 'AIG', 'AMT',  'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', #'ANDV', 
 'ANSS', 'ANTM', 'AON', 'APA', 'AIV', 'AAPL', 'AMAT', #'APTV', 
 'ADM', 'ARNC', 'AJG', 'AIZ', #'T', 
 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', #'BHGE', 
 'BLL', 'BAC', 'BAX', 'BBT', 'BDX', #'BRK.B', 
 'BBY', 'BIIB', 'BLK', 'HRB', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', #'BHF', 
 'BMY', 'AVGO', #'BF.B', 
 'CHRW', #'CA', 
 'COG', 'CDNS', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CAT', 'CBOE', 'CBRE', 'CBS', 
 'CELG', 'CNC', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHTR', 'CVX', #'CMG', 
 'CB', 'CHD', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CME', 
 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', #'CXO', 
 'COP', 'ED', 'STZ', 'GLW', 'COST', 'COTY', 'CCI', #'CSRA', 
 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', #'DE', 
 'DAL', 'XRAY', 'DVN', 'DLR', #'DFS', 
 'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DOV', 'DWDP', #'DPS', 
 'DTE', 'DUK', 'DRE', #'DXC', 
 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', #'EVHC', 
 'EOG', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'RE', #'ES', 
 'EXC', 'EXPE', 'EXPD', #'ESRX', #'EXR', 
 'XOM', 'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', #'FITB', 
 'FE', 'FISV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FL', 'F', 'FTV', 'FBHS', 'BEN', 
 'FCX', 'GPS', 'GRMN', 'IT', 'GD',  #'GE', #'GGP', 
 'GIS', 'GM', 'GPC', 'GILD', 'GPN', #'GS', 
 'GT', 'GWW', 'HAL', 'HBI', 'HOG', #'HRS', 
 'HIG', 'HAS', 'HCA', 'HCP', 'HP', #'HSIC', 
 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HPQ', 'HUM',  #'HBAN', 
 'HII', 'IDXX',  #'INFO', 
 'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 
 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JBHT', 'JEC', 'SJM', 'JNJ', 'JCI', 'JPM', 
 'JNPR', 'KSU', 'K', #'KEY', 
 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', #'KHC', 
 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LEG', 'LEN', #'LUK', 
 'LLY', 'LNC', 'LKQ', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MRO', 'MPC', 
 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 
 'MET', 'MTD', 'MGM', #'KORS', 
 'MCHP', 'MU', 'MSFT', 'MAA', 'MHK', 'TAP', 'MDLZ', #'MON', #'MNST', 
 'MCO', #'MS', 
 'MSI', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NKTR', 'NTAP', 'NFLX', 'NWL',  #'NFX', 
 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NBL', 'JWN', 'NSC', 'NTRS', 
 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'PCAR', 
# 'PKG', 
 'PH', 'PAYX', 'PYPL', 'PNR', 'PBCT', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 
 'PSX', 'PNW', 'PXD', 'PNC', 'RL', 'PPG', 'PPL', #'PX', 
 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'QCOM', 
 'PWR', 'DGX', 'RRC', 'RJF', 'RTN', 'O', 'RHT', 'REG', 'REGN', 'RF', 'RSG', 
 'RMD', 'RHI', 'ROK', 'COL','ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', # 'SCG', #income statement missing
 'SLB', 'STX', 'SEE', 'SRE', 'SHW', 'SPG', 'SWKS', 'SLG', 'SNA', 'SO', 'LUV', 
 'SWK', 'SBUX', 'STT', 'SRCL', 'SYK', 'STI', #'SIVB', 
 'SYMC', #'SYF', 
 'SNPS', 'SYY', #'TROW', 
 'TTWO', 'TPR', 'TGT', 'TEL', #'FTI', 
 'TXN', 'TXT', 'BK', 'CLX', 'COO', 'HSY', 'MOS', 'TRV', 'DIS', 'TMO', 'TIF',  #'TWX', 
 'TJX', 'TMK', #'TSS', breaks Sharpe, #'TSCO', 
 'TDG', 'TRIP',  #'FOXA', 
 'FOX', 'TSN', 'USB', 'UDR', 'ULTA', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 
 'URI', 'UTX', 'UHS', 'UNM', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VRSK', 'VZ', 
 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', #'WM',  #BS ist von 2018 aber IS und CFS von 2019
 'WAT', 'WEC', 'WFC', 'WELL', 'WDC', 'WU', 'WRK', 'WY', 'WHR', 'WMB', 'WLTW', 
 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', #'XL', 
 'XYL', 'YUM', 'ZBH', #'ZION', 
 'ZTS' 
   
    
]


#FUNCTIONS THAT GRAB ALL THE DATA WE NEED FROM THE COMPANY PROFILES, CASH FLOW STATEMENTS, BALANCE SHEET, AND INCOME STATEMENT
# NOTE: financialmodelingprep's legacy v3 API (nested under "financials"/"profile") was
# retired; these read from the current "stable" API's flat, per-year array format instead.

def read_company_profile(company):
    file = open(f"{DATA_DIR}/company-profile-{company}.txt")
    data = json.load(file)
    profile = data[0]
    sector = str(profile["sector"])
    price = float(profile["price"])
    beta = float(profile["beta"])
    file.close()
    return {"price": price, "sector": sector, "beta": beta}


def read_cash_flow(company, year_start, year_end):
    file = open(f"{DATA_DIR}/cash-flow-{company}.txt")
    data = json.load(file)
    cash_flow = {}
    for ent in data:
        y = int(ent["fiscalYear"])
        if year_start < y <= year_end:
            cash_flow[y] = {
                "dna": float(ent["depreciationAndAmortization"]),
                "capex": float(ent["capitalExpenditure"]),
            }
    file.close()
    return cash_flow


def read_balance_sheet(company, year_start, year_end):
    file = open(f"{DATA_DIR}/balance-sheet-{company}.txt")
    data = json.load(file)
    balance_sheet = {}
    for ent in data:
        y = int(ent["fiscalYear"])
        if year_start < y <= year_end:
            balance_sheet[y] = {
                "cash": float(ent["cashAndCashEquivalents"]),
                "ar": float(ent["netReceivables"]),
                "inv": float(ent["inventory"]),
                "ap": float(ent["accountPayables"]),
                "debt": float(ent["totalDebt"]),
            }
    file.close()
    return balance_sheet


def read_income_statement(company, year_start, year_end):
    file = open(f"{DATA_DIR}/income-statement-{company}.txt")
    data = json.load(file)
    # Sorted ascending so revenue growth can be computed year-over-year.
    entries = sorted(data, key=lambda ent: ent["date"])
    income_statement = {}
    prev_revenue = None
    for ent in entries:
        y = int(ent["fiscalYear"])
        revenue = float(ent["revenue"])
        rvgr = (revenue - prev_revenue) / prev_revenue if prev_revenue else 0.0
        prev_revenue = revenue
        if year_start < y <= year_end:
            income_statement[y] = {
                "rv": revenue,
                "rvgr": rvgr,
                "ebit%": float(ent["ebit"]) / revenue,
                "shares": float(ent["weightedAverageShsOut"]),
            }
    file.close()
    return income_statement


def latest_available_year(company):
    file = open(f"{DATA_DIR}/income-statement-{company}.txt")
    data = json.load(file)
    file.close()
    return max(int(ent["fiscalYear"]) for ent in data)