from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging

# Set up logging
logger = logging.getLogger(__name__)

# In-memory list to store favorite Pokémon
favorite_pokemons = []

def index(request):
    return render(request, 'index.html')  # Render the index.html

@csrf_exempt  # Disable CSRF for testing purposes
def submit_favorite(request):
    if request.method == 'POST':
        favorite_pokemon = request.POST.get('favorite_pokemon')
        
        # Log the favorite Pokémon for backend confirmation
        logger.info(f"Favorite Pokémon submitted: {favorite_pokemon}")
        
        # Store in memory
        favorite_pokemons.append(favorite_pokemon)
        
        # Return a simple confirmation message
        return HttpResponse("Favorite Pokémon saved successfully.")
    
    return HttpResponse("Invalid request", status=400)

def get_all_pokemon(request):
    # Return the list of favorite Pokémon, or a message if none have been submitted
    return HttpResponse('<br>'.join(favorite_pokemons) if favorite_pokemons else "No Pokémon submitted.")

def page2_view(request):
    return render(request, 'page2.html')  # Render the page2.html