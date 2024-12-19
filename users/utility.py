import requests


def get_city_and_country_from_pincode(pin_code):
    try:
        # Example: using an API to get city and country from the pin code (adjust for your country/API)
        url = f"https://api.postalpincode.in/pincode/{pin_code}"  # This is specific to India Post API
        response = requests.get(url)
        data = response.json()

        if data[0]["Status"] == "Success":
            city = data[0]["PostOffice"][0]["Division"]
            country = "India"  # You can adjust this depending on the API
            return city, country
        else:
            return None, None
    except Exception as e:
        return None, None
