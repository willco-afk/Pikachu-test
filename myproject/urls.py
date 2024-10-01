from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from .views import index, submit_favorite, page2_view, get_all_pokemon  # Import your views here

urlpatterns = [
    path('admin/', admin.site.urls),  # Access the admin panel at /admin
    path('', index, name='index'),  # Home page points to your index view
    path('submit/', submit_favorite, name='submit_favorite'),  # Path for form submission
    path('page2/', page2_view, name='page2'),  # Path for page2
    path('get_all_pokemon/', get_all_pokemon, name='get_all_pokemon'),  # Path for getting all Pokémon
]

# Serve static files from the root directory if needed
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files from the models folder in the root directory
urlpatterns += [
    path('models/<path:path>', serve, {'document_root': settings.BASE_DIR / 'models'}),
]