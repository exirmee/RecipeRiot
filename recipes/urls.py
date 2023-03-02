from django.urls import path



from . import views
from.views import add_favorite,duplicate_recipe,view_recipe,delete_ing,add_ing,category_list,save_recipe,category_detail,search_view,sign_up_view,home,login_view,edit_recipe,add_recipe,delete_recipe,check_username,delete_ins,add_ins

urlpatterns = [

    path('', views.index, name='index'),

    path('cats/', category_list, name='category_list'),
    path('cats/<int:pk>/', category_detail, name='category_detail'),
    path('search/', search_view, name='search'),
    path('signup/', sign_up_view, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('add/',add_recipe , name='add_recipe'),
    path("edit/<int:pk>/", edit_recipe, name="edit_recipe"),
    path('view/<int:pk>/', view_recipe, name='view_recipe'),
    path('delete/<int:pk>/',delete_recipe , name='delete_recipe'),
    path('duplicate/<int:pk>/',duplicate_recipe , name='duplicate_recipe'),
]

htmx_urlpatterns = [
    path('signup/check_username/', check_username, name='check_username'),
    path("save/<int:pk>/", save_recipe, name="save_recipe"),
    path('add-ing/',add_ing,name="add_ing"),
    path('add-ins/',add_ins,name="add_ins"),
    path('delete_ing/<int:pk>/',delete_ing,name="delete_ing"),
    path('delete_ins/<int:pk>/',delete_ins,name="delete_ins"),
    path('add_fav/<int:pk>/',add_favorite,name="add_favorite"),
]


urlpatterns += htmx_urlpatterns