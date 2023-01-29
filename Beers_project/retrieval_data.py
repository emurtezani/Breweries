import urllib.request
from pathlib import Path


url_form = 'https://api.openbrewerydb.org/breweries?by_state=california&per_page=30{}&noredirect=true&format=json'

# define the path to the data directory
data_dir_path = Path('./raw_data')

# create the directory if it does not exist
if not data_dir_path.exists():
    data_dir_path.mkdir()

counter = 1
for brewery in url_form:
        # stvori url za
    url = url_form

    # get the text for url
    response = urllib.request.urlopen(url)
    raw_text = response.read()
    text = raw_text.decode('utf-8')
    response.close()

 #  create a unique file name
    file_path = data_dir_path.joinpath(str(counter) + ".json")
    counter = 1

    # save that text to disk in a new file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
