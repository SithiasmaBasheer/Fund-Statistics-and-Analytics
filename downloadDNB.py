# Import libraries
import requests

# Set the URL you want to download from
url = 'https://statistiek.api.dnb.nl/api/dataset/resourcecsv?id=66e96c68-6f2d-4529-b0d4-740b1e7a1f84'

# Connect to the URL
response = requests.get(url, allow_redirects=True,verify=False)
print (response)

# Write the download file to csv
open('c:/Summary balance sheet of pension funds by type.csv', 'wb').write(response.content)