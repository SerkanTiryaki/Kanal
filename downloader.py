# Import modules

import pandas as pd
import urllib.request


# ---------------------
def url_to_json(i, url, file_path):
	'''
		Args:
			-- i : number of json
			-- url : a URL address of a given json.
			-- file_path : where to save the final json.
	'''
	
	filename = 'tr-{}.json'.format(i)
	full_path = '{}{}'.format(file_path, filename)
	urllib.request.urlretrieve(url, full_path)
	
	print('{} saved.'.format(filename))
	
	return None
# ---------------------

# Set Constants
FILENAME = 'link.csv'
FILE_PATH = 'json/'

# Read List of URLs as Pandas DataFrame
urls = pd.read_csv(FILENAME)

# Save json to directory by iterating though the list

for i, url in enumerate(urls.values):
	url_to_json(i, url[0], FILE_PATH)
    
    
    