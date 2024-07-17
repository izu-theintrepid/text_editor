import requests

def get_synonyms(word):
    api_url = f"https://api.api-ninjas.com/v1/thesaurus?word={word}"
    api_key = "vtMKY8lbHyey9RkmywvuwA==6HtCnZBzFAwX8prJ"  # Replace with your actual API key

    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == 200:
        data = response.json()
        if "synonyms" in data:
            return data["synonyms"]
        else:
            return f"No synonyms found for the word '{word}'"
    else:
        return f"Error: {response.status_code}, {response.text}"

word = "beautiful"
synonyms = get_synonyms(word)
print(f"Synonyms for '{word}': {synonyms}")
