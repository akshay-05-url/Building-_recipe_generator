import requests

API_KEY = "275d58779ccf4e22af03e792e8819fff"
URL = f"https://api.spoonacular.com/recipes/random?number=10&apiKey={API_KEY}"

def get_recipes():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        return data.get("recipes", [])
    except requests.RequestException as e:
        print("Error fetching recipes:", e)
        return []

def display_recipes(recipes):
    for i, recipe in enumerate(recipes, start=1):
        print(f"\nRecipe {i}: {recipe['title']}")
        print(f"Image URL: {recipe['image']}")
        print("Ingredients:")
        for ingredient in recipe["extendedIngredients"]:
            print(f"  - {ingredient['original']}")
        print(f"View Recipe: {recipe['sourceUrl']}")

def main():
    print("Fetching random recipes...\n")
    recipes = get_recipes()
    if recipes:
        display_recipes(recipes)
    else:
        print("No recipes found.")

if __name__ == "__main__":
    main()