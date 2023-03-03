import ast,os
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Recipe,RecipeCats,ParentCats,RecipeIngredients,Units,RecipeInstructions,Favorite,RecipeReview
from django.shortcuts import render, get_object_or_404,redirect
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm,RecipeForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

#this function runs every time a Recipe creat or edit and make a resized copy of recipe image 
@login_required
@receiver(post_save, sender=Recipe)
def resize_image(sender, instance, **kwargs):
    size = (950, 850)
    quality = 80
    original_image = Image.open(instance.image.path)
    original_width, original_height = original_image.size  
    
    if original_width / original_height < size[0] / size[1]:
        resize_ratio = size[0] / original_width
        new_height = int(original_height * resize_ratio)
        cropped_image = original_image.resize((size[0], new_height), Image.ANTIALIAS)
        cropped_image = cropped_image.crop((0, (new_height - size[1]) / 2, size[0], (new_height + size[1]) / 2))
    else:
        resize_ratio = size[1] / original_height
        new_width = int(original_width * resize_ratio)
        cropped_image = original_image.resize((new_width, size[1]), Image.ANTIALIAS)
        cropped_image = cropped_image.crop(((new_width - size[0]) / 2, 0, (new_width + size[0]) / 2, size[1]))

    filename, extension = os.path.splitext(os.path.basename(instance.image.path))
    resized_image_path = os.path.join(os.path.dirname(instance.image.path), '{}_{}{}'.format(filename, 'mobile', extension))

    cropped_image.save(resized_image_path, format='WebP', quality=quality)
    print(resized_image_path)


#view for detail recipe page ../recipes/<pk>
#view for listing all recipes ../recipes/
def index(request): 
    """View function for recipe index page ."""
    recipe_count = Recipe.objects.filter(privacy=False,status=True).count()
    recipe_list = Recipe.objects.filter(privacy=False,status=True)
    if not request.user.is_authenticated:
        favorites = ()
    else:
        favorites=Favorite.objects.filter(user=request.user).values_list('recipe', flat=True)
    paginator = Paginator(recipe_list, 12)
    page = request.GET.get('page')
    recipe_list = paginator.get_page(page)
    # Render the HTML template index.html with the data in the context variable
    template=loader.get_template('recipes/recipe_list.html')
    contex={
        'recipe_count':recipe_count,
        'recipe_list':recipe_list,
        'favorites':favorites,
    }
    return HttpResponse(template.render(contex,request))

#check username is available or not with HTMX
def check_username(request):
    username = request.POST.get('username')
    if User.objects.filter(username=username).exists():
        return HttpResponse('<div style="color:red;">this user name is already taken.</div>')
    else:
        return HttpResponse('<div style="color:green;">this user name is available.</div>')
    
#view for listing all categories
def category_list(request):
    categories = RecipeCats.objects.all()
    parent_category = ParentCats.objects.all()
    contex={'categories': categories,'parent_category':parent_category}
    return render(request, 'recipes/category_list.html',contex )

#view for detail category page ../recipes/category/<pk>
def category_detail(request,pk):
    category = get_object_or_404(RecipeCats,pk=pk)
    recipes = Recipe.objects.filter(cat=category ,privacy=False,status=True)
    recipe_count = Recipe.objects.filter(cat=category).count()
    related_categories = RecipeCats.objects.filter(recipe__in=recipes).exclude(pk=pk).distinct()
    parent_category = ParentCats.objects.all()
    contex={'category': category, 'recipe_list': recipes,'recipe_count':recipe_count,'related_categories':related_categories,'parent_category':parent_category}
    return render(request, 'recipes/category_detail.html', contex)

#view for search page ../search
def search_view(request):
    query = request.GET.get('q')
    if query:
        # Use case-insensitive search
        recipe_count = Recipe.objects.filter(privacy=False,status=True,name__icontains=query).count()
        recipes = Recipe.objects.filter(privacy=False,status=True,name__icontains=query)
        paginator = Paginator(recipes, 12)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        q=query
    else:
        recipes = Recipe.objects.filter(privacy=False,status=True)
        recipe_count = Recipe.objects.filter(privacy=False,status=True).count()
        paginator = Paginator(recipes, 12)
        page = request.GET.get('page')
        recipes= paginator.get_page(page)
        q=query
    return render(request, 'search.html', {'recipes': recipes,'recipe_count':recipe_count,'q':q})

#view for user signup page ../signup
def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

#view for user login page ../login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request, request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

#view for user profile page ../recipes/profile/<pk>
@login_required(login_url="/login")
def home(request):
    recipes = Recipe.objects.filter(author=request.user.id)
    favorite_recipes= Recipe.objects.filter(favorite__user=request.user)
    favorites = Favorite.objects.filter(user=request.user).values_list('recipe', flat=True)

    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',favorite_recipes)
    return render(request, 'home.html', {"recipes": recipes,'favorite_recipes':favorite_recipes,'favorites':favorites})

#view for creating recipe page ../recipes/add_recipe
@login_required(login_url="/login")
def add_recipe(request):
    if request.method == 'POST':
        name='new recipe'
        recipe =Recipe.objects.create(name=name,author=request.user)
        recipe.save()
        return redirect(f'edit_recipe', pk=recipe.pk)
    else:
        return HttpResponseBadRequest('Only POST requests are allowed')

#view for edit recipe page ../recipes/edit_recipe/<pk>
#edit just own user recipe 
@login_required(login_url="/login")
def edit_recipe(request,pk):
    user=request.user
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author == user:
        r=RecipeForm(request.POST, request.FILES,instance=recipe)
        ingredients=recipe.ingredients.all()
        instructions=recipe.instructions.all()
        parent_categories= ParentCats.objects.all()  
        all_cats=RecipeCats.objects.all()
        categories = recipe.cat.all()
        units=Units.objects.all()
        context = {'r':r,'units':units,'recipe': recipe,'categories': categories,'all_cats':all_cats,'instructions':instructions,'ingredients':ingredients,'parent_categories':parent_categories}
        return render(request, 'recipes/edit_recipe.html', context)
    else:
        return redirect('home')

    
#view for detail recipe page ../recipes/recipe/<pk>
def view_recipe(request,pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.privacy == True and request.user != recipe.author:
        return redirect('home')
    elif recipe.status == False and request.user != recipe.author:
        return redirect('home')
    else:
        ingredients=recipe.ingredients.all()
        instructions=recipe.instructions.all()
        categories = recipe.cat.all()
        reviews=RecipeReview.objects.filter(recipe=recipe)
        context = {'recipe': recipe,'categories': categories,'instructions':instructions,'ingredients':ingredients,'reviews':reviews}
        return render(request, 'recipes/view_recipe.html', context)


# modify the view to update the image field
@login_required(login_url="/login")
def save_recipe(request, pk):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=pk)
        name = request.POST.get('name')
        serves = request.POST.get('serves')
        difficulty = request.POST.get('difficulty')
        timetoprepare = request.POST.get('timetoprepare')
        intro = request.POST.get('intro')
        outro = request.POST.get('outro')
        cat = request.POST.get('cat')
        if request.POST.get('privacy') == 'true':
            privacy = True
        else:
            privacy = False
        recipe.name = name
        if request.FILES.get('image'):
            recipe.image = request.FILES['image']
        recipe.serves = serves
        recipe.difficulty = difficulty
        recipe.timetoprepare = timetoprepare
        recipe.intro = intro
        recipe.outro = outro
        recipe.privacy = privacy
        if cat:
            categories = ast.literal_eval(cat)
            categories = RecipeCats.objects.filter(name__in=categories)
            recipe.cat.set(categories)
            recipe.status = True
            recipe.save()
            return HttpResponse("Recipe saved successfully")
        else:
            recipe.status = True
            recipe.save()
            return HttpResponse("Recipe saved successfully")
    else:
        return HttpResponse("not allowed")


#this view gets a recipe id and duplicated it for current user
#view for duplicate recipe page ../recipes/duplicate_recipe/<pk>
@login_required(login_url="/login")
def duplicate_recipe(request,pk):
    if request.method == 'POST':
        user=request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        # make a clone of recipe
        duplicated_recipe = recipe
        # Remove the `id` field so that a new `id` is generated for the duplicate record
        duplicated_recipe.id = None
        duplicated_recipe.author = user
        duplicated_recipe.name=recipe.name + ' copy'
        #save duplicated recipe
        duplicated_recipe.save()
        #redirect duplicated_recipe to edit_recipe view
        return redirect(f'edit_recipe', pk=duplicated_recipe.pk)
    
    else:
        return HttpResponseBadRequest("not allowed")

#view for delete recipe page ../recipes/delete_recipe/<pk>
#make this view secure with csrf token
#only delete recipe if user is owner of recipe
@login_required(login_url="/login")
def delete_recipe(request,pk):
    if request.method == 'POST':
        user=request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        if recipe.author == user:
            recipe.delete()
            #check for HTTP_REFERER in request.META to redirect to previous page
            if 'HTTP_REFERER' in request.META:
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return redirect('home')
        else:
            return redirect('home')
    else:
        return HttpResponseBadRequest("not allowed")

#view for delete recipe page ../recipes/delete_recipe/<pk>
@login_required(login_url="/login")
def add_ing(request):
    if request.method == 'POST':
        user=request.user
        pk=request.POST.get('recipe_id')
        recipe = get_object_or_404(Recipe, pk=pk)
        if recipe.author == user:
            ingredient=request.POST.get('ingredient')
            value=request.POST.get('value')
            unit=Units.objects.get(pk=int(request.POST.get('unit')))
            ing=RecipeIngredients.objects.create(ingredient=ingredient,value=value,unit=unit)   
            ing.save()
            recipe_ing=Recipe.objects.get(pk=int(request.POST.get('recipe_id')))
            recipe_ing.ingredients.add(ing.id)
            recipe_ing.save()
            return render(request,'recipes/partials/ingredient.html',{'ing':ing})
    else:
        return HttpResponseBadRequest("not allowed")

#view for delete recipe page ../recipes/delete_recipe/<pk>
@login_required(login_url="/login")
def add_ins(request):
    if request.method == 'POST':
        user=request.user
        pk=request.POST.get('recipe_id')
        recipe = get_object_or_404(Recipe, pk=pk)
        if recipe.author == user:
            instruction=request.POST.get('instruction')
            order=request.POST.get('order')
            #image=request.POST.get('image')
            ins=RecipeInstructions.objects.create(instruction=instruction,order=order)   
            ins.save()
            recipe_ins=Recipe.objects.get(pk=int(request.POST.get('recipe_id')))
            recipe_ins.instructions.add(ins.id)
            recipe_ins.save()
            return render(request,'recipes/partials/instruction.html',{'ins':ins})
    else:
        return HttpResponseBadRequest("not allowed")
    

#view for delete ingridients page ../recipes/delete_recipe/<pk>
@login_required(login_url="/login")
def delete_ing(request,pk):
    if request.method == 'POST':
        ing=RecipeIngredients.objects.get(pk=pk)   
        ing.delete()
        return HttpResponse()
    else:
        return HttpResponseBadRequest("not allowed")    

#view for delete ingridients page ../recipes/delete_recipe/<pk>
@login_required(login_url="/login")
def delete_ins(request,pk):
    if request.method == 'POST':
        ins=RecipeInstructions.objects.get(pk=pk)   
        ins.delete()
        return HttpResponse()
    else:
        return HttpResponseBadRequest("not allowed")    



@login_required
def add_favorite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    user=request.user
    favorite=Favorite.objects.filter(recipe=recipe, user=user)
    if favorite:
        message=("♡")
        favorite=Favorite.objects.get(recipe=recipe, user=user)
        favorite.delete()
    else:
        message=("♥")
        favorite=Favorite.objects.create(recipe=recipe, user=user)
        favorite.save()
    # Add an HX-Trigger header with showAlert as its value
    # Return the response
    #return response
    return HttpResponse(message)

@login_required
def add_review(request, pk):
    
    recipe=get_object_or_404(Recipe, pk=pk)
    user=request.user
    rating=request.POST.get('rating')
    review=request.POST.get('review')
    if request.FILES.get('image'):
        image = request.FILES['image']
    else:
        image=None
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",user,review,recipe,rating)
    review_obj=RecipeReview.objects.create(recipe=recipe, user=user,rating=rating,review=review,image=image)
    review_obj.save()

    return HttpResponse(user)
