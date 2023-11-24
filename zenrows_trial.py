# pip install zenrows

from zenrows import ZenRowsClient

client = ZenRowsClient("fc4e4214f9fe8843c4841de7eda9e595cd18cdf9")
url = "https://www.tripadvisor.com/"

response = client.get(url)

print(response.text)

# How would I save the output to a json file?
