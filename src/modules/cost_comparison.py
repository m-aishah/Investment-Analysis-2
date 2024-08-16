from typing import List, Dict
from models import InvestmentOptionsSchema
from modules.filter_investment_options import filter_investment_options
# from modules.access_data import fetch_price_list, fetch_rental_income, fetch_available_projects

def format_property_data(property, rental_income=None, price_list=None):
    # Extracting price data
    project_name = property['projectName']
    property_type = property['purpose']
    total_price = property['price']
    additional_fees = property['VAT'] + property['stamp_duty'] + property['title_deed_transfer'] + property['lawyer_fees']
    total_cost_including_fees = total_price + additional_fees
    
    # Extracting rental income data (using 'realistic' scenario)
    # rental_data_realistic = rental_income.get('realistic', {})
    # gross_rental_yield = rental_data_realistic.get('annual_net_rental_yield', 0)
    # net_rental_yield = rental_data_realistic.get('ROI', 0)
    
    # Constructing formatted data
    formatted_data = {
        "propertyID": property['propertyID'],
        "projectName": project_name,
        "Property": property_type,
        "Location": property['location'],
        "Price per Square Meter": f"€{property['price'] / property['total_area_sqmeter']:.0f}",
        "Total Price": f"€{total_price:,}",
        "Additional Fees": f"€{(additional_fees):,}",
        "Total Cost Including Fees": f"€{total_cost_including_fees:,}",
       # "Price to Income Ratio": f"{gross_rental_yield:.2f}",
       # "Mortgage as Percentage of Income": f"{net_rental_yield:.2f}%",
       # "Loan Affordability Index": f"{total_price / net_rental_yield:.2f}",
       # "Gross Rental Yield": f"{gross_rental_yield:.2f}%",
       # "Net Rental Yield": f"{net_rental_yield:.2f}%",
       # "ROI": f"{rental_data_realistic.get('ROI', 0)}%",
        "Total Area (sqm)": property['total_area_sqmeter'],
        "Number of Rooms": f"{property['no_of_rooms']} bedrooms, {property['no_of_bathrooms']} bathrooms",
        "Facilities and Amenities": ', '.join(property['facilities']),
        "Estimated Completion Date": property['completion_date'],
        "Developer Track Record": "Excellent" if property['percentage_sold'] >= 70 or property['propertyDeveloper'] == "Dovec" else "Good"
    }
    
    return formatted_data

def run_cost_comparison_module(**props):
    try:
        parameters = InvestmentOptionsSchema(**props)
    except Exception as e:
        return {"error": str(e)}

    properties = filter_investment_options(parameters)
    if not properties:
        return {"message": "No properties found matching the criteria."}
    comparison_data = []
    for property in properties:
        property_id = property['propertyID']
        
    #    try:
    #         price_list = fetch_price_list(property_id)[0]
    #         rental_income = fetch_rental_income(property_id)
    #     except Exception as e:
    #         print(f"error: Failed to fetch data for property ID {property_id}: {str(e)}")
    #         continue

    #     if price_list and rental_income:
        formatted_data = format_property_data(property)
        comparison_data.append(formatted_data)
        
    return {"properties": comparison_data}