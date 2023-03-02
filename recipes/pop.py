from recipes.models import Recipe, RecipeCategory


def create_recipe(name, date, serves, difficulty, timetoprepare, intro, steps, outro, image, cat_names):
    recipe = Recipe()
    recipe.name = name
    recipe.date = date
    recipe.serves = serves
    recipe.difficulty = difficulty
    recipe.timetoprepare = timetoprepare
    recipe.intro = intro
    recipe.steps = steps
    recipe.outro = outro
    recipe.image = image
    recipe.save()
    # Create RecipeCategory objects and add them to the cat field of the Recipe object
    categories = []
    for cat_name in cat_names:
        cat, created = RecipeCategory.objects.get_or_create(name=cat_name)
        categories.append(cat)
    recipe.cat.set(categories)
    recipe.cat.set(categories)
create_recipe(" Bolognese", "2022-01-01", 4, "2", 30, "This classic dish is a favorite of many", "1. Cook spaghetti as per package instructions. 2. In a pan, sauté onions and garlic. 3. Add ground beef and cook until browned. 4. Add canned tomatoes and let simmer for 15 minutes. 5. Serve spaghetti with bolognese sauce on top", "Add grated cheese and parsley for garnish", "recipe_images/spaghetti_bolognese.jpg", ["Italian", "Main Dish"])