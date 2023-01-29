import urllib.request
import json


# url that retrieves the data
url = "https://api.openbrewerydb.org/breweries?by_state=california&per_page=30"

# retrieving data from the online API
response = urllib.request.urlopen(url)
text = response.read()
text = text.decode('utf-8')
response.close()



# converting data into structured data
data = json.loads(text)

# 2. html file
html_file = open('Breweries.html', 'w', encoding='utf-8')

# write down the beginning part of the html
html_file.write("""
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Breweries</title>
    </head>
    <body style="background-color:powderblue;">
""")

html_file.write('<center><h1 style="color:#A52A2A;" "font-family:verdana" >Breweries in California</h1></center>')

# write down the data for each beer
for breweries in data:

    p = '{} // ({}) // {} // {} // URL: [{}]'.format(breweries['name'], breweries['brewery_type'], breweries['street'], breweries['city'], breweries['website_url'])


    html_file.write('<p style="font-size:120%;">{}</p>'.format(p))

# close html file
html_file.write("""
        </body>
    </html>
    """)


html_file.close()
