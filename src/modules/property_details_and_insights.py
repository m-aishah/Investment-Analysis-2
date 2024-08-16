from models import InvestmentOptionsSchema
from modules.filter_investment_options import filter_investment_options
from modules.access_data import fetch_price_list

def gather_property_details(property_id):
    # print("here 1")
    try:
        price_list = fetch_price_list(property_id)
    except Exception as e:
        raise Exception(f"Failed to fetch price list: {e}")
    
    #print("here 2")

    details = []
    if price_list:
        for price_info in price_list:
            payment_plan = price_info['payment_plan']
            details.append({
                'Apartment Type': price_info['apratment_type'],
                'Block': price_info['block'],
                'Floor': price_info['floor'],
                'Interior Area (sqm)': price_info['interior_sqmeter'],
                'Balcony/Terrace Area (sqm)': price_info['balcony_terrace_sqmeter'],
                'Rooftop Area (sqm)': price_info['rooftop_sqmeter'],
                'Total Living Space (sqm)': price_info['total_living_space_sqmeter'],
                'Price': payment_plan['price'],
                'Price Per Square Meter': payment_plan['price'] / price_info['total_living_space_sqmeter'],
                'Payment Plan Start Date': payment_plan['start_date'],
                'Payment Plan Delivery Date': payment_plan['delivery_date'],
                'Installment Payment Plan': payment_plan['installment_payment_plan'],
                'Additional Fees': payment_plan['additional_fees'],
                'Total Amount': payment_plan['total_amount']
            })
    return details

def run_property_details_and_insights(**kwargs):
    #print("here 3")
    parameters = InvestmentOptionsSchema(**kwargs)
    #print("here 4")
    filtered_projects = filter_investment_options(parameters)
    #print("here 5")
    #print(filtered_projects)
    
    property_details = []
    for item in filtered_projects:
        property_id = item['propertyID']
        try:
            details = gather_property_details(property_id)
        except Exception as e:
            details = None
            print(f"Error fetching property details for property ID {property_id}: {e}")
        
        if details and len(details) > 0:
            property_details.append({
                'propertyID': item['propertyID'],
                'Project Name': item['projectName'],
                'Property Developer': item['propertyDeveloper'],
                'Location': item['location'],
                'Purpose': item['purpose'],
                'Completion Date': item['completion_date'],
                'Facilities': ", ".join(item['facilities']),
                'ImageURL': ["https://static.tildacdn.com/stor3335-6430-4635-a664-303033613461/19958823.jpg", "https://optim.tildacdn.one/tild3831-3338-4936-b035-626534353538/-/format/webp/90156560.jpeg", "https://optim.tildacdn.com/stor3830-3761-4335-b033-396166663233/-/format/webp/93188055.jpg", "https://optim.tildacdn.com/stor3465-3132-4464-b562-636266383936/-/format/webp/44491027.jpg"],
                'Property Details': details,
                '360 view': "",
                'Number of Rooms': item['no_of_rooms'],
                'Number of Bathrooms': item['no_of_bathrooms']
            })

            if item['propertyDeveloper'] == 'Dovec Construction':
                property_details[-1]['360 view'] = 'https://360.dovecconstruction.com/'
            if item['propertyDeveloper'] == 'Noyanlar Construction':
                property_details[-1]['360 view'] = 'https://360.noyanlar.com/'

            # print(property_details[-1])
    return {"property_details": property_details}