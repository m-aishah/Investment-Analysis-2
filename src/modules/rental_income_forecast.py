from models import InvestmentOptionsSchema
from modules.filter_investment_options import filter_investment_options
from modules.access_data import fetch_rental_income

def run_rental_income_forecast(**kwargs):
    parameters = InvestmentOptionsSchema(**kwargs)
    filtered_projects = filter_investment_options(parameters)
    forecast = []
    
    for project in filtered_projects:
        property_id = project['propertyID']
        try:
            rental_income = fetch_rental_income(property_id)
        except Exception as e:
            rental_income = None
            print(f"Error fetching rental income for property ID {property_id}: {e}")
        
        if rental_income:
            forecast.append({
                "propertyID": property_id,
                "projectName": project['projectName'],
                "propertyDeveloper": project['propertyDeveloper'],
                "location": project['location'],
                "purpose": project['purpose'],
                "description": project['description'],
                "rental_income": {
                    'optimistic': rental_income['optimistic'],
                    'pessimistic': rental_income['pessimistic'],
                    'realistic': rental_income['realistic']
                }
            })

    result = {"rental_income_forecast": forecast if len(forecast) > 0 else 'No property found with the given criteria.'}
    return result
