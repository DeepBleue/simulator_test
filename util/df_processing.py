import pandas as pd




def db_A_preprocess(df):
    df['체결시간'] = pd.to_datetime(df['체결시간'])
    df = df.sort_values(by='체결시간', ignore_index=True)
    df['time_diff'] = df['체결시간'].diff().dt.total_seconds()
    df['현재가'] = pd.to_numeric(df['현재가'].astype(str).str.replace('+','').str.replace('-',''), errors='coerce')
    df = df.dropna()
    
    time_val = df['time_diff'].values
    chaegul_data = df[['현재가','거래량']].values
    
    
    return time_val, chaegul_data
    