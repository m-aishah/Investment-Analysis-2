from faker import Faker
import random

fake = Faker()

# Define options
purposes = ["All", "For Relocation", "For Max Rental ROI", "For Buy-Sell Investment"]
prices = [80000, 100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 260000, 
          280000, 300000, 350000, 400000, 450000, 500000, 1000000]
locations = ["All", "Kyrenia", "Iskele", "Guzelyurt", "Nicosia", "Famagusta", "Lefke", "Karpaz Peninsula"]

# Function to generate property types
def generate_property_types():
    property_types = []
    for _ in range(random.randint(1, 3)):
        property_id = random.randint(100, 999)
        no_of_rooms = random.randint(1, 5)
        property_type = random.choice(["apartment", "house", "villa"])
        total_area_sqmeter = random.randint(100, 300)
        no_of_bathrooms = random.randint(1, 3)
        price = random.choice(prices)
        
        property_types.append({
            "propertyID": property_id,
            "no_of_rooms": no_of_rooms,
            "type": property_type,
            "total_area_sqmeter": total_area_sqmeter,
            "no_of_bathrooms": no_of_bathrooms,
            "price": price
        })
    
    return property_types

# Function to generate projects
def generate_project():
    project_id = random.randint(1, 100)
    project_name = fake.company()
    property_developer = fake.company()
    location = random.choice(locations)
    purpose = random.choice(purposes)
    description = fake.text()
    start_date = fake.date_between(start_date='-2y', end_date='-1y')
    completion_date = fake.date_between(start_date='now', end_date='+2y')
    facilities = [fake.word() for _ in range(random.randint(1, 5))]
    image_urls = [fake.image_url() for _ in range(random.randint(1, 3))]
    no_of_installments = random.randint(6, 24)
    no_of_properties = random.randint(10, 100)
    property_types = generate_property_types()
    percentage_sold = random.randint(0, 100)
    
    return {
        "projectID": project_id,
        "projectName": project_name,
        "propertyDeveloper": property_developer,
        "location": location,
        "purpose": purpose,
        "description": description,
        "start_date": start_date,
        "completion_date": completion_date,
        "facilities": facilities,
        "image_url": image_urls,
        "no_of_installments": no_of_installments,
        "no_of_properties": no_of_properties,
        "property_types": property_types,
        "percentage_sold": percentage_sold
    }

# Generate dummy data for projects
projects_data = [generate_project() for _ in range(20)]

# Function to generate price list
def generate_price_list(property_id):
    return [
        {
            "No": i,
            "apratment_type": fake.word(),
            "block": fake.random_letter().upper(),
            "floor": random.randint(1, 20),
            "interior_sqmeter": random.randint(50, 150),
            "balcony_terrace_sqmeter": random.randint(10, 50),
            "rooftop_sqmeter": random.randint(0, 100),
            "total_living_space_sqmeter": random.randint(60, 250),
            "payment_plan": {
                "start_date": fake.date_between(start_date='now', end_date='+1y'),
                "delivery_date": fake.date_between(start_date='+1y', end_date='+2y'),
                "price": random.choice(prices),
                "percentage_payment_amount": random.randint(10, 50),
                "payment_amount": random.randint(10000, 50000),
                "installment_payment_plan": [
                    {
                        "percentage": random.randint(1, 20),
                        "plan": [(str(i), fake.date_between(start_date='now', end_date='+1y'), random.randint(1000, 5000)) for i in range(1, random.randint(2, 6))]
                    } for _ in range(random.randint(1, 3))
                ],
                "additional_fees": {
                    "property_price": random.randint(10000, 50000),
                    "VAT": random.randint(1000, 5000),
                    "stamp_duty": random.randint(500, 2000),
                    "title_deed_transfer": random.randint(1000, 5000),
                    "lawyer_fees": random.randint(1000, 5000)
                },
                "total_amount": random.randint(100000, 500000)
            }
        } for i in range(random.randint(1, 5))
    ]

# Generate dummy data for price lists
price_list_data = {property['propertyID']: generate_price_list(property['propertyID']) for project in projects_data for property in project['property_types']}

# Function to generate rental income
def generate_rental_income(property_id):
    scenarios = ["pessimistic", "realistic", "optimistic"]
    return {
        "propertyID": property_id,
        "property": fake.address(),
        "pessimistic": {
            "scenario": "pessimistic",
            "no_of_rental_days": random.randint(50, 365),
            "average_daily_rate": random.randint(50, 200),
            "gross_rental_income": random.randint(10000, 50000),
            "net_income": random.randint(5000, 25000),
            "unit_price": random.randint(100000, 500000),
            "annual_net_rental_yield": round(random.uniform(1, 10), 2),
            "ROI": round(random.uniform(1, 15), 2)
        },
        "realistic": {
            "scenario": "realistic",
            "no_of_rental_days": random.randint(50, 365),
            "average_daily_rate": random.randint(50, 200),
            "gross_rental_income": random.randint(10000, 50000),
            "net_income": random.randint(5000, 25000),
            "unit_price": random.randint(100000, 500000),
            "annual_net_rental_yield": round(random.uniform(1, 10), 2),
            "ROI": round(random.uniform(1, 15), 2)
        },
        "optimistic": {
            "scenario": "optimistic",
            "no_of_rental_days": random.randint(50, 365),
            "average_daily_rate": random.randint(50, 200),
            "gross_rental_income": random.randint(10000, 50000),
            "net_income": random.randint(5000, 25000),
            "unit_price": random.randint(100000, 500000),
            "annual_net_rental_yield": round(random.uniform(1, 10), 2),
            "ROI": round(random.uniform(1, 15), 2)
        }
    }

# Generate dummy data for rental incomes
rental_incomes = {property['propertyID']: generate_rental_income(property['propertyID']) for project in projects_data for property in project['property_types']}

# Example usage
if __name__ == "__main__":
    print("Projects Data:")
    print(projects_data)
    
    print("\nPrice List Data:")
    for property_id, price_list in price_list_data.items():
        print(f"Property ID {property_id}:")
        print(price_list)
        
    print("\nRental Income Data:")
    for property_id, rental_income in rental_incomes.items():
        print(f"Property ID {property_id}:")
        print(rental_income)


# Simulated data (replace with actual data retrieval)
projects_data = [
    {
        "projectID": 1,
        "projectName": "Project A",
        "propertyDeveloper": "Developer X",
        "location": "Nicosia",
        "purpose": "Residential",
        "description": fake.text(),
        "start_date": "2023-01-01",
        "completion_date": "2024-12-31",
        "facilities": ["Swimming Pool", "Gym"],
        "image_url": [fake.image_url(), fake.image_url()],
        "no_of_installments": 12,
        "no_of_properties": 50,
        "property_types": [
            {
                "propertyID": "A001",
                "no_of_rooms": 3,
                "type": "Apartment",
                "total_area_sqmeter": 120,
                "no_of_bathrooms": 2,
                "price": 250000
            },
            {
                "propertyID": "A002",
                "no_of_rooms": 4,
                "type": "Villa",
                "total_area_sqmeter": 300,
                "no_of_bathrooms": 3,
                "price": 500000
            }
        ],
        "percentage_sold": 70
    },
    {
        "projectID": 2,
        "projectName": "Project B",
        "propertyDeveloper": "Developer Y",
        "location": "Kyrenia",
        "purpose": "Commercial",
        "description": fake.text(),
        "start_date": "2023-06-01",
        "completion_date": "2025-05-31",
        "facilities": ["Parking Area", "Conference Rooms"],
        "image_url": [fake.image_url(), fake.image_url()],
        "no_of_installments": 24,
        "no_of_properties": 30,
        "property_types": [
            {
                "propertyID": "B001",
                "no_of_rooms": 10,
                "type": "Office Space",
                "total_area_sqmeter": 500,
                "no_of_bathrooms": 4,
                "price": 800000
            }
        ],
        "percentage_sold": 50
    },
    {
        "projectID": 3,
        "projectName": "Project C",
        "propertyDeveloper": "Developer Y",
        "location": "Girne",
        "purpose": "Residential",
        "description": fake.text(),
        "start_date": "2023-06-01",
        "completion_date": "2025-05-31",
        "facilities": ["Swimming Pool", "Parking Area", "Sauna"],
        "image_url": [fake.image_url(), fake.image_url()],
        "no_of_installments":13,
        "no_of_properties": 2,
        "property_types": [
            {
                "propertyID": "C001",
                "no_of_rooms": 4,
                "type": "Apartment 3+!",
                "total_area_sqmeter": 500,
                "no_of_bathrooms": 1,
                "price": 250000
            },
            {
                "propertyID": "C002",
                "no_of_rooms": 4,
                "type": "Penthouse",
                "total_area_sqmeter": 500,
                "no_of_bathrooms": 1,
                "price": 250000
            }, 
        ],
        "percentage_sold": 70
    }
]

price_list_data = {
    "A001": [
        {
            "No": 1,
            "apratment_type": "Apartment",
            "block": "A",
            "floor": 1,
            "interior_sqmeter": 100,
            "balcony_terrace_sqmeter": 20,
            "rooftop_sqmeter": 0,
            "total_living_space_sqmeter": 120,
            "payment_plan": {
                "start_date": "2023-08-01",
                "delivery_date": "2024-08-01",
                "price": 250000,
                "percentage_payment_amount": 30,
                "payment_amount": 75000,
                "installment_payment_plan": [
                    {
                        "percentage": "30%",
                        "plan": [
                            ("1", "August 2024", 1510)
                        ]
                    }
                ],
                "additional_fees": {
                    "property_price": 250000,
                    "VAT": 10000,
                    "stamp_duty": 5000,
                    "title_deed_transfer": 2000,
                    "lawyer_fees": 3000
                },
                "total_amount": 300000
            }
        }
    ],
    "A002": [
        {
            "No": 1,
            "apratment_type": "Villa",
            "block": "B",
            "floor": 2,
            "interior_sqmeter": 250,
            "balcony_terrace_sqmeter": 50,
            "rooftop_sqmeter": 20,
            "total_living_space_sqmeter": 320,
            "payment_plan": {
                "start_date": "2023-09-01",
                "delivery_date": "2024-09-01",
                "price": 500000,
                "percentage_payment_amount": 30,
                "payment_amount": 150000,
                "installment_payment_plan": [
                    {
                        "percentage": "30%",
                        "plan": [
                            ("1", "September 2024", 2510)
                        ]
                    }
                ],
                "additional_fees": {
                    "property_price": 500000,
                    "VAT": 20000,
                    "stamp_duty": 10000,
                    "title_deed_transfer": 4000,
                    "lawyer_fees": 6000
                },
                "total_amount": 600000
            }
        }
    ]
}

rental_income_data = {
    "A001": {
        "propertyID": "A001",
        "property": "Apartment A001",
        "pessimistic": {
            "scenario": "Pessimistic",
            "no_of_rental_days": 300,
            "average_daily_rate": 100,
            "gross_rental_income": 30000,
            "net_income": 25000,
            "unit_price": 250000,
            "annual_net_rental_yield": 10,
            "ROI": 5
        },
        "realistic": {
            "scenario": "Realistic",
            "no_of_rental_days": 330,
            "average_daily_rate": 120,
            "gross_rental_income": 39600,
            "net_income": 33600,
            "unit_price": 250000,
            "annual_net_rental_yield": 13.44,
            "ROI": 6.72
        },
        "optimistic": {
            "scenario": "Optimistic",
            "no_of_rental_days": 360,
            "average_daily_rate": 150,
            "gross_rental_income": 54000,
            "net_income": 46800,
            "unit_price": 250000,
            "annual_net_rental_yield": 18.72,
            "ROI": 9.36
        }
    },
    "A002": {
        "propertyID": "A002",
        "property": "Villa A002",
        "pessimistic": {
            "scenario": "Pessimistic",
            "no_of_rental_days": 280,
            "average_daily_rate": 200,
            "gross_rental_income": 56000,
            "net_income": 48000,
            "unit_price": 500000,
            "annual_net_rental_yield": 9.6,
            "ROI": 4.8
        },
        "realistic": {
            "scenario": "Realistic",
            "no_of_rental_days": 300,
            "average_daily_rate": 250,
            "gross_rental_income": 75000,
            "net_income": 65000,
            "unit_price": 500000,
            "annual_net_rental_yield": 13,
            "ROI": 6.5
        },
        "optimistic": {
            "scenario": "Optimistic",
            "no_of_rental_days": 330,
            "average_daily_rate": 300,
            "gross_rental_income": 99000,
            "net_income": 88000,
            "unit_price": 500000,
            "annual_net_rental_yield": 17.6,
            "ROI": 8.8
        }
    }
}