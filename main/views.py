# myapp/views.py
from django.shortcuts import render,redirect
import datetime,random
from .forms import UserDataForm
from .models import User
from decouple import config
import requests
import json

def home(request):
    current_time = datetime.datetime.now()
    weather_data = None  # Initialize weather_data
    error_message = None  # Initialize error_message

    # Replace with the city for which you want weather data
    city = 'NewYork'

    try:
        api_key = config('WEATHER_API_KEY')
    except Exception as e:
        print(f"Error getting API key: {e}")
        api_key = ''  # Set a default value or handle the error accordingly

    url = f'https://api.openweathermap.org/data/2.5/weather?lat=28.61&lon=77.20&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            weather_data = response.json();
            # Process weather data
        except json.decoder.JSONDecodeError:
            error_message = "Error decoding JSON response"
    elif response.status_code == 401:
        error_message = "Error: Unauthorized. Check your API key."
    else:
        error_message = f"Error: {response.status_code}. {response.text}"


    # Example: List of random quotes
    quotes = [
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "It always seems impossible until it's done. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
    ]

    random_quote = random.choice(quotes)

    return render(request, 'home.html', {'current_time': current_time, 'random_quote': random_quote,'weather_data': weather_data})

def user_data(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('success')  # Redirect to a success page or any other page
    else:
        form = UserDataForm()

    return render(request, 'user_form.html', {'form': form})

def display_data(request):
    user_data_list = User.objects.all()  # Retrieve all user data from the database
    return render(request, 'display_data.html', {'user_data_list': user_data_list})

def success(request):
    return render(request, 'success.html')