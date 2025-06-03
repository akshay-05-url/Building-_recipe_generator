const API_KEY = "275d58779ccf4e22af03e792e8819fff";
const recipeListEl = document.getElementById("recipe-list");

function createRecipeItem(recipe) {
  const li = document.createElement("li");
  li.className = "recipe-item";

  const img = document.createElement("img");
  img.src = recipe.image;
  img.alt = `Image of ${recipe.title}`;

  const title = document.createElement("h2");
  title.textContent = recipe.title;

  const ingredients = document.createElement("p");
  ingredients.innerHTML = `
    <strong>Ingredients:</strong> ${recipe.extendedIngredients
      .map(ingredient => ingredient.original)
      .join(", ")}
  `;

  const link = document.createElement("a");
  link.href = recipe.sourceUrl;
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = "View Recipe";

  li.append(img, title, ingredients, link);
  return li;
}

function displayRecipes(recipes) {
  recipeListEl.innerHTML = "";
  recipes.forEach(recipe => {
    const recipeItem = createRecipeItem(recipe);
    recipeListEl.appendChild(recipeItem);
  });
}

async function getRecipes() {
  try {
    const response = await fetch(
      `https://api.spoonacular.com/recipes/random?number=10&apiKey=${API_KEY}`
    );
    const data = await response.json();
    return data.recipes;
  } catch (error) {
    console.error("Failed to fetch recipes:", error);
    recipeListEl.innerHTML = "<p>Error loading recipes. Please try again later.</p>";
    return [];
  }
}

async function init() {
  const recipes = await getRecipes();
  displayRecipes(recipes);
}

init();
