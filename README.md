## ⚙️ How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-recipe-generator.git
cd ai-recipe-generator
```

### 2. Install the required libraries

Use pip to install the necessary Python packages: 

openai may ask for payment try Spoonacular API

```bash
pip install openai requests
```

### 3. Add your API keys

Update the following variables in the Python script:

```python
SPOONACULAR_API_KEY = "your-spoonacular-api-key"
openai.api_key = "your-openai-api-key"
```

💡 **Security tip:** You can set `openai.api_key` using environment variables:

```bash
export OPENAI_API_KEY="your-key-here"
```

Then in Python:

```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```

### 4. Run the script

```bash
python recipe_ai_generator.py
```

### 5. Preview

```bash

Welcome to the AI Recipe Generator with Prompt Structuring!

Enter ingredients separated by commas:
> chicken, garlic, tomatoes

Choose the prompt style to generate the recipe:
1. Simple
2. Detailed
3. Creative
4. Quick and Healthy
5. Custom prompt (write your own)

Enter the number of your choice:
> 2

--- Prompt used for AI ---
Using the following ingredients: chicken, garlic, tomatoes, write a detailed and easy-to-follow cooking recipe. Include the dish name, cooking time, servings, ingredients list with quantities, and numbered step-by-step instructions.

Generating recipe...

Dish Name: Garlic Tomato Chicken Delight

Cooking Time: 40 minutes  
Servings: 4

Ingredients:
- 500g chicken breast, diced
- 3 cloves garlic, minced
- 2 large tomatoes, chopped
- 1 tablespoon olive oil
- Salt and pepper to taste
- 1 teaspoon dried oregano
- 1/2 cup chicken broth

Instructions:
1. Heat olive oil in a skillet over medium heat.
2. Add minced garlic and sauté for 1-2 minutes until fragrant.
3. Add the diced chicken and cook until lightly browned on all sides.
4. Stir in chopped tomatoes, oregano, salt, and pepper.
5. Pour in chicken broth and simmer for 20 minutes until the sauce thickens.
6. Serve hot with rice or crusty bread.

Tips: Add fresh basil for a more aromatic touch.

Would you like to see a Spoonacular API generated recipe for comparison? (y/n):
> y

--- Spoonacular Recipe ---

Dish Name: Tomato Garlic Chicken

Description:
A savory and easy-to-make chicken dish using fresh garlic and tomatoes...

Cooking Time: 35 minutes  
Servings: 4

Procedure:
1. Heat a pan and cook garlic until golden.
2. Add chicken and sear all sides.
3. Toss in tomatoes and cook until soft.
4. Simmer until chicken is fully cooked.
5. Serve warm with pasta or salad.

Tips: You can customize this recipe by adding extra herbs or sides of your choice.


```
---

## 🧰 Libraries Used

| Library    | Purpose                                   | Install via pip        |
| ---------- | ----------------------------------------- | ---------------------- |
| `openai`   | Connects to OpenAI GPT model              | `pip install openai`   |
| `requests` | Makes HTTP requests to Spoonacular API    | `pip install requests` |
| `re`       | Cleans HTML from Spoonacular summaries    | *(built-in)*           |
| `os`       | Loads environment variables (for API key) | *(built-in)*           |

---

## ✨ Features

* 🧠 **AI-generated recipes** from ingredients using GPT-4o-mini
* 🍽️ **Spoonacular real recipes** for comparison
* ✍️ Choose from multiple **prompt styles**:

  * Simple
  * Detailed
  * Creative
  * Quick & Healthy
  * Custom user prompt
* ✅ Step-by-step instructions with cooking time & servings
* 🌍 Optionally customize recipes by region or preference

---

## 🔒 Notes on API Keys

* Do **NOT** commit your API keys to GitHub.
* Consider using a `.env` file or environment variables to secure your keys.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🤝 Contributions

Pull requests are welcome! If you find a bug or want a new feature, open an issue.

---

## 📬 Contact

Made with ❤️ by Sripada Akshay.
Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/akshay-sripada-175b96292?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
