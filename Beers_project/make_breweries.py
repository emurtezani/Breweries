import json
from pathlib import Path
from docx import Document

brewdata_form_normal = "{name} / {brewery_type} / {street} / {city}. / URL: [{website_url}]."
brewdata_form_html = "<p style='font-size:120%;'> {name} / {brewery_type} / {street} / {city}. / URL: [{website_url}].</p>\n"

# define the path to the data directory
data_dir_path = Path('./raw_data')

# open word file
doc = Document()

# open html file
html_file = open('Brewery.html', 'w', encoding='utf-8')

# write the beginning part of the html
html_file.write("""
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Brewery</title>
    </head>
    <body style="background-color:powderblue;">
""")

html_file.write('<center><h1 style="color:#A52A2A;" "font-family:verdana" >Breweries in California</h1></center>')

for file_path in data_dir_path.iterdir():

    # skip all directories and files that do not have an extension .json
    if file_path.is_dir() or file_path.suffix.lower() != '.json':
        continue

        # load data from jsona
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)



    name = data [0] ['name']
    brewery_type = data [0] ['brewery_type']
    street =  data [0] ['street']
    city = data [0] ['city']
    website_url = data [0] ['website_url']

# make plain text for Word and add it as a paragraph to the document
    brewdata_unit_word = brewdata_form_normal.format(
        name=name,
        brewery_type=brewery_type,
        street=street,
        city=city,
        website_url=website_url
    )
    doc.add_paragraph(brewdata_unit_word)


    # create text enriched with html tags and add write it to the html file
    brewdata_unit_html = brewdata_form_html.format(
        name=name,
        brewery_type=brewery_type,
        street=street,
        city=city,
        website_url=website_url
    )
    html_file.write(brewdata_unit_html)


# save docx file
doc.save('./Brewery.docx')

# close html file
html_file.write("""
    </body>
</html>
""")
html_file.close()
