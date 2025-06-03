import requests
import csv

API_KEY = "0dfd8665c23d4546a8290af2ca26354a"
SEARCH_URL = "https://api.spoonacular.com/recipes/findByIngredients"
INFO_URL = "https://api.spoonacular.com/recipes/{id}/information"

DIET_OPTIONS = [
    "none", "vegetarian", "vegan", "gluten free", "ketogenic", "pescetarian", "paleo"
]

def get_user_ingredients():
    while True:
        user_input = input("Enter at least 5 ingredients (comma-separated): ").strip()
        ingredients = [ing.strip() for ing in user_input.split(",") if ing.strip()]
        if len(ingredients) < 5:
            print("❌ Please enter at least 5 ingredients.")
        else:
            return ingredients

def get_user_filters():
    print("\nSelect a dietary preference:")
    for i, option in enumerate(DIET_OPTIONS, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Choose an option (1-{}): ".format(len(DIET_OPTIONS))))
            if 1 <= choice <= len(DIET_OPTIONS):
                diet = DIET_OPTIONS[choice - 1]
                diet = None if diet == "none" else diet
                break
        except ValueError:
            pass
        print("❌ Invalid choice. Please try again.")

    try:
        max_time = int(input("Maximum prep time in minutes (or press Enter to skip): ") or 0)
    except ValueError:
        max_time = 0

    return diet, max_time if max_time > 0 else None

def fetch_recipe_ids(ingredients):
    params = {
        "ingredients": ",".join(ingredients),
        "number": 10,
        "apiKey": API_KEY,
        "ranking": 1,
        "ignorePantry": True
    }
    try:
        response = requests.get(SEARCH_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error fetching recipes:", e)
        return []

def fetch_recipe_details(recipe_id):
    try:
        response = requests.get(INFO_URL.format(id=recipe_id), params={"apiKey": API_KEY})
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def display_recipes(recipes, diet_filter=None, time_filter=None):
    filtered = []
    print(f"\n🧾 Top Recipes:\n")
    for recipe in recipes:
        info = fetch_recipe_details(recipe["id"])
        if not info:
            continue

        if diet_filter and diet_filter not in (diet.lower() for diet in info.get("diets", [])):
            continue
        if time_filter and info.get("readyInMinutes", 0) > time_filter:
            continue

        filtered.append(info)
        if len(filtered) == 5:
            break

    if not filtered:
        print("❌ No recipes matched your filters.")
        return []

    for i, r in enumerate(filtered, 1):
        print(f"{i}. {r['title']}")
        print(f"   🕒 {r['readyInMinutes']} minutes | 👨‍🍳 {r['servings']} servings")
        print(f"   🔗 {r['sourceUrl']}")
        print(f"   🥕  Used ingredients: {', '.join([ing['name'] for ing in recipe['usedIngredients']])}")
        print(f"   🚫  Missing ingredients: {', '.join([ing['name'] for ing in recipe['missedIngredients']])}")
        print(f"   Recipe ID: {recipe['id']}")
        print()

    return filtered

def save_to_csv(recipes, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Ready In (min)", "Servings", "Source URL"])
        for recipe in recipes:
            writer.writerow([recipe["title"], recipe["readyInMinutes"], recipe["servings"], recipe["sourceUrl"]])
    print(f"✅ Recipes saved to '{filename}'.")

def save_to_txt(recipes, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for r in recipes:
            file.write(f"Title: {r['title']}\n")
            file.write(f"Ready In: {r['readyInMinutes']} minutes\n")
            file.write(f"Servings: {r['servings']}\n")
            file.write(f"Link: {r['sourceUrl']}\n\n")
    print(f"✅ Recipes saved to '{filename}'.")

def ask_save_format(recipes):
    print("\n💾 Choose file format to save:")
    print("0. Skip saving")
    print("1. CSV (.csv)")
    print("2. Text File (.txt)")

    choice = input("Your choice: ").strip()
    if choice == "1":
        filename = input("Enter filename (without extension): ") + ".csv"
        save_to_csv(recipes, filename)
    elif choice == "2":
        filename = input("Enter filename (without extension): ") + ".txt"
        save_to_txt(recipes, filename)
    else:
        print("Skipping save.")

def main():
    print("🍽️  Welcome to the Smart Recipe Generator!")
    ingredients = get_user_ingredients()
    diet, max_time = get_user_filters()

    print("\n🔍 Searching recipes...")
    recipe_matches = fetch_recipe_ids(ingredients)
    final_recipes = display_recipes(recipe_matches, diet_filter=diet, time_filter=max_time)

    if final_recipes:
        ask_save_format(final_recipes)

if __name__ == "__main__":
    main()