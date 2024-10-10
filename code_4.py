import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
 country_code = country_code.upper
 query = f"(date >= '{year}-01-01' & date <= '{year}-12-31' & iso_a3 == '{country_code})"
 isdata = df.query(query)
 mean = isdata['dollar_price'].mean()
 return round(mean,2)


def get_big_mac_price_by_country(country_code):
     country_code = country_code.upper()     #good on this one 
     query = f"(iso_a3 == '{country_code}')"
     isdata = df.query(query)
     mean = isdata['dollar_price'].mean()
     return round(mean,2)


def get_the_cheapest_big_mac_price_by_year(year):
    year = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"  
    isdata = df.query(year)
    min = isdata['dollar_price'].idxmin()
    data = isdata.loc[min]
    name = f"{data['name']}({data['iso_a3']}): ${round(data['dollar_price'],2)}"
    return name

def get_the_most_expensive_big_mac_price_by_year(year):
    year = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"  
    isdata = df.query(year)
    max = isdata['dollar_price'].idxmax()
    data = isdata.loc[max]
    name = f"{data['name']}({data['iso_a3']}): ${round(data['dollar_price'],2)}"
    return name


if __name__ == "__main__":
    year = 2000
    country_code = 'chn'

    #print(get_big_mac_price_by_year(year,country_code))

    print(f"The price of country for {country_code} is: ${get_big_mac_price_by_country(country_code)}")

    print(get_the_cheapest_big_mac_price_by_year(year))
    print(get_the_most_expensive_big_mac_price_by_year(year))



    #Chat-GPT (Version 4.0). (2024, October 9). “How to fix a function to take year and country_code as arguments in Python.” Generated using OpenAI Chat-GPT. https://chat.openai.com/
    # I was trying to figure out a way to get the print for print(get_big_mac_price_by_year(year,country_code)), but i was unsuccesfull.


