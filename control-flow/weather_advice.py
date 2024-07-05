# Prompt user for weather input
weather = str(input("What's the weather like today? (sunny/rainy/cold): "))
# Provide clothing recommendations based on weather input
if weather.lower() == "sunny":
    print("Recommendation: Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    print("Recommendation: Don't forget your umbrella and a raincoat.")
elif weather.lower() == "cold":
    print("Recommendation: Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
