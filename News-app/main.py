import requests
api_key = "54aa957d1d904db0ae64abc542d60f91"
query = input("What type of news are you Interesting today ? :")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-02-22&sortBy=publishedAt&apiKey={api_key}"

r = requests.get(url)
data = r.json()
articals = data["articles"]

for article in articals:
    print(article["title"] , article["url"])
    print("\n ------------------------------------------------\n")