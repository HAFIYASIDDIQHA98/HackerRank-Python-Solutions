def weather_report():
    # Mock database
    city_data = {
        "hyderabad": "32°C, Sunny",
        "bangalore": "24°C, Pleasant",
        "delhi": "18°C, Foggy"
    }
    
    city = input("Enter City Name (Hyderabad/Bangalore/Delhi): ").lower()
    
    # Using .get() for safe access
    report = city_data.get(city, "City not found in our database.")
    print(f"Weather Report: {report}")

weather_report()
