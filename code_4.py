import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
   isdata = df(df['year']) and (df['iso_a3'].str.lower() == country_code)
   
   if len(isdata) > 0: 
    mean_price = isdata['dollar_price'].mean()
    return round(mean_price,2)
   return None

def get_big_mac_price_by_country(country_code):
    isdata = df[df['iso_a3'].str.lower() == country_code]
    
    if len(isdata) > 0:
        mean_price = isdata['dollar_price'].mean()
        return round(mean_price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    isdata = df[df['year']==year]
    if len(isdata) > 0:
        cheapest_row = isdata.loc[isdata['dollar_price'].idxmin()]
        return f"{cheapest_row['country_name']}({cheapest_row['iso_a3']}): {cheapest_row['dollar_price']:.2}"
    return None

def get_the_most_expensive_big_mac_price_by_year(year):
    isdata = df[df['year']==year]
    if len(isdata) > 0:
        expensive_row = isdata.loc[isdata['dollar_price'].idxmax()]
        return f"{expensive_row['country_name']}({expensive_row['iso_a3']}): {expensive_row['dollar_price']:.2}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year)
    print(get_big_mac_price_by_country)
    print(get_the_cheapest_big_mac_price_by_year)
    print(get_the_most_expensive_big_mac_price_by_year)