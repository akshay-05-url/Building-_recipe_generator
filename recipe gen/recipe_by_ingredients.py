import requests

API_KEY = "0dfd8665c23d4546a8290af2ca26354a"
SEARCH_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def get_user_ingredients():
    while True:
        user_input = input("Enter at least 5 ingredients you have (comma-separated): ").strip()
        ingredients = [ing.strip() for ing in user_input.split(",") if ing.strip()]
        if len(ingredients) < 5:
            print("Please enter at least 5 ingredients.")
        else:
            return ingredients

def fetch_recipes(ingredients):
    params = {
        "ingredients": ",".join(ingredients),
        "number": 10,
        "apiKey": API_KEY,
        "ranking": 1,  # maximize used ingredients
        "ignorePantry": True
    }
    try:
        response = requests.get(SEARCH_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching recipes:", e)
        return []

def display_recipes(recipes):
    if not recipes:
        print("No recipes found for those ingredients.")
        return

    print(f"\nFound {len(recipes)} recipes:\n")
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe['title']}")
        print(f"   Used ingredients: {', '.join([ing['name'] for ing in recipe['usedIngredients']])}")
        print(f"   Missing ingredients: {', '.join([ing['name'] for ing in recipe['missedIngredients']])}")
        print(f"   Recipe ID: {recipe['id']}")
        print(f"   More info: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']}\n")

def main():
    ingredients = get_user_ingredients()
    print("\nSearching recipes...")
    recipes = fetch_recipes(ingredients)
    display_recipes(recipes)

if __name__ == "__main__":
    main()
