import pandas as pd 
from bs4 import BeautifulSoup
import lxml

with open("paper2table.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "lxml")  
title = soup.title.string
print("Title:", title)

for div in soup.find_all("div"):
    children = [child for child in div.children if child.name]
    if children and children[0].name == "p" and "table 2" in children[0].text.lower():
        table = div.find("table")
        if table:
            # Use pandas to read the table from the HTML
            df_list = pd.read_html(str(table))
            if df_list:
                df_list[0].to_csv("paper2_output.csv", index=False)
        break