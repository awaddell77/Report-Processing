import requests
url = 'http://#unknown/vertex-restapi/v1/addresslookup'
payload = "{\n    \"postalAddress\": {\n        \"streetAddress1\": \"<string>\",\n        \"streetAddress2\": \"<string>\",\n        \"city\": \"<string>\",\n        \"mainDivision\": \"<string>\",\n        \"subDivision\": \"<string>\",\n        \"postalCode\": \"<string>\",\n        \"country\": \"<string>\"\n    },\n    \"asOfDate\": \"<date>\",\n    \"lookupId\": \"<string>\"\n}"
headers = {
  'Content-Type': 'application/json'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout='undefined')
print(response.text)