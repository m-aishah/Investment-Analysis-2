from typing import Optional, Dict, Type
from pydantic import BaseModel, Field
from typing import get_args, get_origin


class PropertySchema(BaseModel):
    propertyID: str = Field(..., title="Property ID", description="Unique identifier for the property")
    no_of_rooms: int = Field(..., title="Number of Rooms", description="Number of rooms in the property")
    type: str = Field(..., title="Property Type", description="Type of the property (e.g., Apartment, Villa)")
    total_area_sqmeter: float = Field(..., title="Total Area (sq meter)", description="Total area of the property in square meters")
    no_of_bathrooms: float = Field(..., title="Number of Bathrooms", description="Number of bathrooms in the property")
    price: float = Field(..., title="Price", description="Price of the property in the local currency")

class ProjectSchema(BaseModel):
    projectID: str = Field(..., title="Project ID", description="Unique identifier for the project")
    projectName: str = Field(..., title="Project Name", description="Name of the project")
    propertyDeveloper: str = Field(..., title="Property Developer", description="Name of the property developer")
    location: str = Field(..., title="Location", description="Location of the project")
    description: str = Field(..., title="Description", description="Brief description of the project")
    purpose: str = Field(..., title="Purpose", description="Purpose of the project (e.g., Residential, Commercial)")
    start_date: str = Field(..., title="Start Date", description="Start date of the project")
    completion_date: str = Field(..., title="Completion Date", description="Estimated completion date of the project")
    facilities: list[str] = Field(..., title="Facilities", description="List of facilities available in the project")
    no_of_installments: int = Field(..., title="Number of Installments", description="Number of payment installments available")
    no_of_properties: int = Field(..., title="Number of Properties", description="Total number of properties in the project")
    percentage_sold: float = Field(..., title="Percentage Sold", description="Percentage of properties sold")
    property_types: list[PropertySchema] = Field(..., title="Property Types", description="List of property types available in the project")
    image_url: list[list] = Field(..., title="Image URLs", description="URLs of images related to the project")
item = {
              "completion_date": {
                "title": "Completion Date",
                "type": "string"
              },
              "description": {
                "title": "Description",
                "type": "string"
              },
              "facilities": {
                "title": "Facilities",
                "type": "array"
              },
              "image_url": {
                "title": "Image URLs",
                "type": "array"
              },
              "location": {
                "title": "Location",
                "type": "string"
              },
              "no_of_installments": {
                "title": "Number of Installments",
                "type": "integer"
              },
              "no_of_properties": {
                "title": "Number of Properties",
                "type": "integer"
              },
              "percentage_sold": {
                "title": "Percentage Sold",
                "type": "number"
              },
              "projectID": {
                "title": "Project ID",
                "type": "string"
              },
              "projectName": {
                "title": "Project Name",
                "type": "string"
              },
              "propertyDeveloper": {
                "title": "Property Developer",
                "type": "string"
              },
              "property_types": {
                "description": "List of property types available in the project",
                "items": {
                  "no_of_bathrooms": {
                    "title": "Number of Bathrooms",
                    "type": "number"
                  },
                  "no_of_rooms": {
                    "title": "Number of Rooms",
                    "type": "integer"
                  },
                  "price": {
                    "title": "Price",
                    "type": "number"
                  },
                  "propertyID": {
                    "title": "Property ID",
                    "type": "string"
                  },
                  "total_area_sqmeter": {
                    "title": "Total Area (sq meter)",
                    "type": "number"
                  },
                  "type": {
                    "title": "Property Type",
                    "type": "string"
                  }
                },
                "title": "Property Types",
                "type": "array"
              },
              "purpose": {
                "title": "Purpose",
                "type": "string"
              },
              "start_date": {
                "title": "Start Date",
                "type": "string"
              }
            }
class InvestmentOptionsSchema(BaseModel):
    budget_min: int = Field(0, title="Minimum Budget", description="Minimum budget for property investment")
    budget_max: int = Field(..., title="Maximum Budget", description="Maximum budget for property investment")
    location: str = Field(None, title="Location", description="Location preference for property investment")
    size_min: int = Field(0, title="Minimum Size", description="Minimum property size in square meters", ge=0)
    size_max: int = Field(0, title="Maximum Size", description="Maximum property size in square meters")
    bedrooms_min: int = Field(0, title="Minimum Bedrooms", description="Minimum number of bedrooms", ge=0)
    bedrooms_max: int = Field(0, title="Maximum Bedrooms", description="Maximum number of bedrooms")
    bathrooms_min: float = Field(0, title="Minimum Bathrooms", description="Minimum number of bathrooms", ge=0)
    bathrooms_max: float = Field(None, title="Maximum Bathrooms", description="Maximum number of bathrooms")
    family_size: int = Field(None, title="Family Size", description="Number of family members")
    property_type: str = Field(None, title="Property Type", description="Type of property (e.g., house, apartment)")
    sort_by: str = Field(None, title="Sort By", description="Sort the results by a specific field (e.g., price, size)")
    projects_data: tuple[ProjectSchema] = Field(..., title="Projects Data", description="List of projects data")




def get_properties_formated(model, visited=None):
    if visited is None:
        visited = set()
    
    if model in visited:
        return {"type": "object", "description": f"Recursive reference to {model.__name__}"}
    
    visited.add(model)
    
    if isinstance(model, type) and issubclass(model, BaseModel):
        schema = model.model_json_schema()
        properties_formatted = {}
        
        for k, v in schema["properties"].items():
            if v.get("type") == "array" and v.get("title") in ("Projects Data", "Property Types"):
                field = model.model_fields[k]
                field_type = field.annotation
                if get_origin(field_type) is list:
                    item_type = get_args(field_type)[0]
                    properties_formatted[k] = {
                        "title": v.get("title"),
                        "type": "array",
                        "description": v.get("description"),
                        "items": get_properties_formated(item_type, visited.copy())
                    }
                else:
                    # print("here")
                    properties_formatted[k] = v
            else:
                properties_formatted[k] = {
                        "title": v.get("title"),
                        "type": v.get("type")
                    }
        
        return properties_formatted
    else:
        # Handle simple types
        return {"type": type(model).__name__.lower()}

def custom_json_schema(model):
    properties_formatted = get_properties_formated(model)
    if isinstance(model, type) and issubclass(model, BaseModel):
        schema = model.model_json_schema()
        return {
            "type": "object",
            "default": {},
            "properties": properties_formatted,
            "required": schema.get("required", [])
        }
    else:
        return properties_formatted