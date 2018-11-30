from django.urls import include, path


app_name='mainapp'
urlpatterns = [
    path('', include('matchingsite.urls')),
]



