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
