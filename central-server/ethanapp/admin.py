from django.contrib import admin

# Register your models here.
from .movieModel import Movie, MoviePerson
from .personModel import Person

class MoviePersonInline(admin.TabularInline):
    model = MoviePerson
    extra = 5

class MoviePersonList(admin.ModelAdmin):
    inlines = [MoviePersonInline]
    list_display = ["name"]
    search_fields = ["name"]

class PersonMovieList(admin.ModelAdmin):
    inlines = [MoviePersonInline]
    list_display = ["title"] 
    search_fields = ["title"]
    
admin.site.register(Person, MoviePersonList)
admin.site.register(Movie, PersonMovieList)
