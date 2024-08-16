import json
from models import InvestmentOptionsSchema

def filter_investment_options(parameters: InvestmentOptionsSchema):
    # Convert the projects_data string to a list of dictionaries
    try:
        projects_data = json.loads(parameters.projects_data.replace("'", '"'))
        # print(f"projects_data: {projects_data}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse projects data: {e}")
    
    filtered_projects = []

    for property in projects_data:
            print(property)
            if (property['price'] >= parameters.budget_min and
                property['price'] <= parameters.budget_max and
                (property['total_area_sqmeter'] >= parameters.size_min if parameters.size_min else True) and
                (property['total_area_sqmeter'] <= parameters.size_max if parameters.size_max else True) and
                (property['no_of_rooms'] >= parameters.bedrooms_min if parameters.bedrooms_min else True) and
                (property['no_of_rooms'] <= parameters.bedrooms_max if parameters.bedrooms_max else True) and
                (property['no_of_bathrooms'] >= parameters.bathrooms_min if parameters.bathrooms_min else True) and
                (property['no_of_bathrooms'] <= parameters.bathrooms_max if parameters.bathrooms_max else True) and
                ((property['type']).lower() == parameters.property_type.lower() if parameters.property_type else True)):
                try:
                    filtered_projects.append({
                        'projectID': property['projectID'],
                        'projectName': property['projectName'],
                        'propertyDeveloper': property['propertyDeveloper'],
                        'location': property['location'],
                        'description': property['description'],
                        'purpose': property['purpose'],
                        'start_date': property['start_date'],
                        'completion_date': property['completion_date'],
                        'facilities': property['facilities'],
                        'no_of_installments': property['no_of_installments'],
                        'no_of_properties': property['no_of_properties'],
                        'percentage_sold': property['percentage_sold'],
                        'propertyID': property['propertyID'],
                        'no_of_rooms': property['no_of_rooms'],
                        'total_area_sqmeter': property['total_area_sqmeter'],
                        'no_of_bathrooms': property['no_of_bathrooms'],
                        'price': property['price'],
                        'interior_sqmeter': property['interior_sqmeter'],
                        'balcony_terrace_sqmeter': property['balcony_terrace_sqmeter'],
                        'rooftop_sqmeter': property['rooftop_sqmeter'],
                        'total_living_space_sqmeter': property['total_living_space_sqmeter'],
                        'payment_plan': property['payment_plan'],
                        'VAT': property['VAT'],
                        'stamp_duty': property['stamp_duty'],
                        'title_deed_transfer': property['title_deed_transfer'],
                        'lawyer_fees': property['lawyer_fees'],
                        'price': property['price'],
                        'ImageURL OR VideoURL': property['ImageURL'] or property['VideoURL'],
                        # 'ImageURL': property['image_url'][0] if property['image_url'] else None
                    })
                except Exception as e:
                     print("Error filtering properties: ", e)

    if not filtered_projects:
        return []

    if parameters.sort_by and parameters.sort_by in filtered_projects[0]:
        filtered_projects = sorted(filtered_projects, key=lambda x: x[parameters.sort_by])

    return filtered_projects
