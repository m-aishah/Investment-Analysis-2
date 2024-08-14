import logging
from models import InvestmentOptionsSchema
from modules.cost_comparison import run_cost_comparison_module
from modules.rental_income_forecast import run_rental_income_forecast
from modules.risk_analysis import run_risk_analysis_module
from modules.property_details_and_insights import run_property_details_and_insights

def run_investment_recommendation_wrapper(**kwargs):
    """
    Run the investment recommendation wrapper. Returns a list of recommendations based on input parameters.
    
    This function initializes the InvestmentOptionsSchema with input parameters,
    runs each module's function, and compiles the results into a single dictionary.

    Args:
        **kwargs: Arbitrary keyword arguments containing input parameters.
    
    Returns:
        dict: A dictionary containing the recommendations.
    """
    logging.info("Starting investment recommendation wrapper")
    # Initialize the InvestmentOptionsSchema with input parameters
    #try:
    #    parameters = InvestmentOptionsSchema(**kwargs)
    #except Exception as e:
     #   logging.error(f"Error initializing InvestmentOptionsSchema: {e}")
      #  return {"error": str(e)}
    
    # Run each module's function and collect results
    cost_comparison_result = run_cost_comparison_module(**kwargs)
    rental_income_forecast_result = run_rental_income_forecast(**kwargs)
    risk_analysis_result = run_risk_analysis_module(**kwargs)
    property_details_result = run_property_details_and_insights(**kwargs)

    recommendations = []
    for property in cost_comparison_result['properties']:
        property_id = property['propertyID']
        RIF = None; RA = None; PDI = None
        for item in rental_income_forecast_result['rental_income_forecast']:
            if property_id == item['propertyID']:
                RIF = item
                break
        for item in risk_analysis_result['risk_analysis']:
            if property_id == item['Risk Report']['propertyID']:
                RA = item['Risk Report']
                break
        for item in property_details_result['property_details']:
            if property_id == item['propertyID']:
                PDI = item['Property Details']
                break
        if RIF and RA and PDI:
            recommended_property = {
                'Cost Comparison': property,
                'Rental Income Forecast': RIF,
                'Risk Analysis': RA,
                'Property Details and Insights': PDI
            }
            recommendations.append(recommended_property)
    # Compile all results into a single dictionary
    return {"recommendations": recommendations}


if __name__ == "__main__":
    params = {
            "budget_min": 100000,
            "budget_max": 3000000
        }
    print(run_investment_recommendation_wrapper(**params))
        