# Simulated data (replace with actual data retrieval)
projects_data = [
    {
        "projectID": 1,
        "projectName": "Project A",
        "propertyDeveloper": "Developer X",
        "location": "Nicosia",
        "purpose": "Residential",
        "description": "Lorem ipsum dolor sit amet.",
        "start_date": "2023-01-01",
        "completion_date": "2024-12-31",
        "facilities": ["Swimming Pool", "Gym"],
        "image_url": ["image1.jpg", "image2.jpg"],
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
        "description": "Lorem ipsum dolor sit amet.",
        "start_date": "2023-06-01",
        "completion_date": "2025-05-31",
        "facilities": ["Parking Area", "Conference Rooms"],
        "image_url": ["image3.jpg", "image4.jpg"],
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