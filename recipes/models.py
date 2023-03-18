from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from django_quill.fields import QuillField


    

class ParentCats(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = ResizedImageField(size=[850, 310], quality=80,force_format='WebP',crop=['middle', 'center'], upload_to='recipe_images/',default="/recipe_images/default.jpg",blank=True, null=True,help_text='Enter ------')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'parent categories'

class Units(models.Model):
    name=models.CharField(max_length=20)
    sign=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Units'

class RecipeCats(models.Model):
    name = models.CharField(max_length=255)
    desc=models.TextField(null=True)
    image = ResizedImageField(size=[430, 290], quality=80,force_format='WebP',crop=['middle', 'center'], upload_to='cats_images/',default="/cats/default.jpg",blank=True, null=True)
    parent_categories = models.ForeignKey(ParentCats,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'recipe categories'

#this class is responsible for ingredients table in database
class RecipeIngredients(models.Model):
    ingredient = models.CharField(max_length=100)
    value=models.DecimalField(decimal_places=1,max_digits=20,default=1, null=True)
    unit=models.ForeignKey(Units, on_delete=models.RESTRICT, null=True)
    image = ResizedImageField(size=[850, 310], quality=80,force_format='WebP',crop=['middle', 'center'], upload_to='ingredient_images/',default="/ingredient_images/default.jpg",blank=True, null=True)
    def __str__(self):
        return self.ingredient
    class Meta:
        verbose_name_plural = 'Recipe Ingredient'

#this class is responsible for instructions table in database
class RecipeInstructions(models.Model):
    instruction = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(blank=True,null=True)
    image = ResizedImageField(size=[850, 310], quality=80,force_format='WebP',crop=['middle', 'center'], upload_to='instructions_images/',blank=True, null=True)
    def __str__(self):
        return self.instruction
    class Meta:
        verbose_name_plural = 'Recipe Instructions'


#this clas is responsible for recipes table in database
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    chef=models.CharField(max_length=100,default="common",help_text="recipe's chef name (e.g. Chef John)",null=True,blank=True)
    status=models.BooleanField(default=False,help_text="is this recipe ready to be published?")
    name=models.CharField(max_length=300,help_text='Recipe Name (e.g. Pasta)')
    privacy=models.BooleanField(default=False,help_text='is this recipe private?')
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    serves = models.IntegerField(default=1 ,help_text='serves (e.g. 4 people)',null=True,blank=True)
    difficulty = models.IntegerField(default=1 ,help_text='difficulty level (e.g. Easy)',null=True,blank=True)
    timetoprepare=models.IntegerField(default=1 ,validators=[MinValueValidator(1), MaxValueValidator(1000)],help_text='time to prepare (e.g. 30 minutes)',null=True,blank=True)
    intro = models.TextField(help_text='an introduction for the recipe',blank=True)
    outro = models.TextField(help_text='add some notes for the recipe',blank=True)
    image = ResizedImageField(size=[850, 300], quality=80,force_format='WebP',crop=['middle', 'center'], upload_to='recipe_images/',default="default/default-recipe.jpg",blank=True, null=True,help_text='choose an image for the recipe')
    cat=models.ManyToManyField(RecipeCats,blank=True,help_text='Select categories for recipe (hold ctrl to select more than one recipe)')
    ingredients = models.ManyToManyField(RecipeIngredients,blank=True,help_text='Select ingredients for recipe (hold ctrl to select more than one recipe)')
    instructions = models.ManyToManyField(RecipeInstructions,blank=True,help_text='Select instructions for recipe (hold ctrl to select more than one recipe)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Recipe'
    
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('recipe_detail', args=[str(self.id)])



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}'s favorite: {self.recipe}"

# This class represents the ratings and reviews for a recipe, where every user can rate and review each recipe.
class RecipeReview(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('denied', 'Denied')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft')
        # ForeignKey to link the recipe to the rating
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    # ForeignKey to link the user to the rating
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    # An integer field for the rating, with a validator to restrict it to values between 1 and 5
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # A text field for the review
    review = models.TextField(blank=True)
    image = ResizedImageField(size=[1080, 720], quality=80,force_format='WebP',crop=['middle', 'center'], upload_to='review_images/',blank=True, null=True)
    # A date field to keep track of when the rating was created
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # A string representation of the model, showing the recipe name and the user who submitted the rating and review
    def __str__(self):
        return f'{self.recipe.name} - {self.user.username}'
