class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    email=models.EmailField(max_length=254,unique=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True,default="/users/default.jpg")
    dietary_restrictions = models.CharField(max_length=100, blank=True)
    favorite_cuisines = models.CharField(max_length=100, blank=True)
    favorite_ingredients = models.CharField(max_length=100, blank=True)
    following = models.ManyToManyField('self', through='Follow', symmetrical=False)
    saved_recipes = models.ManyToManyField('Recipe', related_name='saved_recipes', blank=True)
    def __str__(self):
        return self.name,self.family

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following_users')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    date = models.DateTimeField(auto_now_add=True)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField('Recipe', related_name='wishlisted_recipes', blank=True)

class CookedRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)





class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    email = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
