import os
import openai #pip install openai
import requests #pip install requests
import re

# Set your API keys here
SPOONACULAR_API_KEY = "**************************" # Replace with your actual Spoonacular API key
# You can set your OpenAI API key as an environment variable for security
OPENAI_API_KEY = os.getenv("sk-***********************************************************************")  # Replace with your actual OpenAI API key
openai.api_key = "sk-***********************************************************************" # Replace with your actual OpenAI API key

def get_spoonacular_recipe(ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "ingredients": ingredients,
        "number": 1,
        "ranking": 1,
        "ignorePantry": True
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    recipes = response.json()
    if not recipes:
        return None
    return recipes[0]

def get_spoonacular_recipe_details(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "includeNutrition": False
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html).strip()

def format_spoonacular_recipe(recipe_info):
    name = recipe_info.get("title", "No title")
    description = clean_html(recipe_info.get("summary", ""))
    cooking_time = recipe_info.get("readyInMinutes", "N/A")
    servings = recipe_info.get("servings", "N/A")

    steps = []
    instructions = recipe_info.get("analyzedInstructions", [])
    if instructions and len(instructions) > 0:
        for step in instructions[0].get("steps", []):
            steps.append(step.get("step", ""))
    else:
        plain_instructions = recipe_info.get("instructions", "")
        if plain_instructions:
            steps = [plain_instructions]

    output = []
    output.append(f"Dish Name: {name}")
    output.append(f"\nDescription:\n{description}\n")
    output.append(f"Cooking Time: {cooking_time} minutes")
    output.append(f"Servings: {servings}\n")
    output.append("Procedure:")
    for i, step in enumerate(steps, 1):
        output.append(f"{i}. {step}")
    output.append("\nTips: You can customize this recipe by adding extra herbs or sides of your choice.")
    return "\n".join(output)

def generate_prompt(ingredients, style):
    base_prompt = f"Using the following ingredients: {ingredients}, "
    if style == "simple":
        base_prompt += "please generate a simple cooking recipe. Include the dish name, cooking time, servings, ingredients list, and step-by-step instructions."
    elif style == "detailed":
        base_prompt += "write a detailed and easy-to-follow cooking recipe. Include the dish name, cooking time, servings, ingredients list with quantities, and numbered step-by-step instructions."
    elif style == "creative":
        base_prompt += "invent a creative and delicious recipe. Include the dish name, ingredients with amounts, cooking time, servings, and detailed step-by-step instructions."
    elif style == "quick":
        base_prompt += "generate a quick and healthy recipe. Include all recipe details with estimated cooking time under 30 minutes."
    else:
        # Allow freeform prompt
        base_prompt = style

    return base_prompt

def get_ai_generated_recipe(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful cooking assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=700,
    )
    return response.choices[0].message.content.strip()

def main():
    print("Welcome to the AI Recipe Generator with Prompt Structuring!\n")
    ingredients = input("Enter ingredients separated by commas:\n").strip()

    print("\nChoose the prompt style to generate the recipe:")
    print("1. Simple")
    print("2. Detailed")
    print("3. Creative")
    print("4. Quick and Healthy")
    print("5. Custom prompt (write your own)")

    style_choice = input("Enter the number of your choice:\n").strip()
    style_map = {
        "1": "simple",
        "2": "detailed",
        "3": "creative",
        "4": "quick",
    }

    if style_choice in style_map:
        style = style_map[style_choice]
    elif style_choice == "5":
        style = input("Enter your custom prompt. Use {ingredients} as a placeholder for the ingredients:\n")
        style = style.replace("{ingredients}", ingredients)
    else:
        print("Invalid choice, defaulting to simple style.")
        style = "simple"

    prompt = generate_prompt(ingredients, style)

    print("\n--- Prompt used for AI ---")
    print(prompt)
    print("\nGenerating recipe...\n")

    try:
        ai_recipe = get_ai_generated_recipe(prompt)
        print(ai_recipe)
    except Exception as e:
        print(f"Error generating AI recipe: {e}")

    # Optional: Compare with Spoonacular API recipe
    compare = input("\nWould you like to see a Spoonacular API generated recipe for comparison? (y/n): ").strip().lower()
    if compare == 'y':
        try:
            recipe = get_spoonacular_recipe(ingredients)
            if not recipe:
                print("No Spoonacular recipes found for those ingredients.")
                return
            details = get_spoonacular_recipe_details(recipe["id"])
            print("\n--- Spoonacular Recipe ---\n")
            print(format_spoonacular_recipe(details))
        except Exception as e:
            print(f"Error fetching Spoonacular recipe: {e}")

if __name__ == "__main__":
    main()