import requests

def fetch_available_projects(location=None, min_price=None, max_price=None, purpose=None):
    url = "http://127.0.0.1:5000/projects/available_projects"
    params = {
        "location": location,
        "min_price": min_price,
        "max_price": max_price,
        "purpose": purpose
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch projects data: {response.status_code} - {response.text}")
    

def fetch_rental_income(property_id):
    url = f"http://127.0.0.1:5000/projects/available_projects/{property_id}/rental_income"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch rental income data: {response.status_code} - {response.text}")

def fetch_price_list(property_id):
    url = f"http://127.0.0.1:5000/projects/available_projects/{property_id}/price_list"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch price list data: {response.status_code} - {response.text}")