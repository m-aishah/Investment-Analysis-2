from models import InvestmentOptionsSchema
from modules.access_data import fetch_available_projects

def filter_investment_options(parameters: InvestmentOptionsSchema):
    if parameters.location:
        locations = parameters.location.split(', ')
        projects_data = []
        try:      
            for location in locations:
                projects_data.extend(fetch_available_projects(
                    location=location,
                    min_price=parameters.budget_min,
                    max_price=parameters.budget_max,
                    # purpose='Residential' if parameters.family_size else None
                ))
        except Exception as e:
            raise Exception(f"Failed to fetch projects data: {e}")
    else:
        try:
            projects_data = fetch_available_projects(
                location=parameters.location,
                min_price=parameters.budget_min,
                max_price=parameters.budget_max,
                # purpose='Residential' if parameters.family_size else None
            )
            print("projects_data", projects_data)
        except Exception as e:
            raise Exception(f"Failed to fetch projects data: {e}")
    
    filtered_projects = []

    for project in projects_data:
        for property in project['property_types']:
            if (property['price'] >= parameters.budget_min and
                property['price'] <= parameters.budget_max and
                (property['total_area_sqmeter'] >= parameters.size_min if parameters.size_min else True) and
                (property['total_area_sqmeter'] <= parameters.size_max if parameters.size_max else True) and
                (property['no_of_rooms'] >= parameters.bedrooms_min if parameters.bedrooms_min else True) and
                (property['no_of_rooms'] <= parameters.bedrooms_max if parameters.bedrooms_max else True) and
                (property['no_of_bathrooms'] >= parameters.bathrooms_min if parameters.bathrooms_min else True) and
                (property['no_of_bathrooms'] <= parameters.bathrooms_max if parameters.bathrooms_max else True) and
                ((property['type']).lower() == parameters.property_type.lower() if parameters.property_type else True)):
                filtered_projects.append({
                    'projectID': project['projectID'],
                    'projectName': project['projectName'],
                    'propertyDeveloper': project['propertyDeveloper'],
                    'location': project['location'],
                    'description': project['description'],
                    'purpose': project['purpose'],
                    'start_date': project['start_date'],
                    'completion_date': project['completion_date'],
                    'facilities': project['facilities'],
                    'no_of_installments': project['no_of_installments'],
                    'no_of_properties': project['no_of_properties'],
                    'percentage_sold': project['percentage_sold'],
                    'propertyID': property['propertyID'],
                    'no_of_rooms': property['no_of_rooms'],
                    'type': property['type'],
                    'total_area_sqmeter': property['total_area_sqmeter'],
                    'no_of_bathrooms': property['no_of_bathrooms'],
                    'price': property['price'],
                    'ImageURL': project['image_url'][0]
                })

    if not filtered_projects:
        return []

    if parameters.sort_by and parameters.sort_by in filtered_projects[0]:
        filtered_projects = sorted(filtered_projects, key=lambda x: x[parameters.sort_by])

    
    return filtered_projects