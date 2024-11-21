# Code Breakdown:

# Purpose:

# The code aligns farm polygons to match the boundaries of corresponding geometry polygons.
# It reads an Excel file containing geographic data, extracts and processes polygons, and creates a new column with aligned polygons.

# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
from shapely import wkt  # For converting WKT strings to Shapely geometries
from shapely.geometry import Point, Polygon  # For creating geometric shapes
from shapely.affinity import affine_transform  # For performing affine transformations on geometries
import json  # For handling JSON data

# Load the Excel file
file_path = r'C:\Users\Vmose\Desktop\Data.xlsx'  # Define the path to the Excel file
data = pd.read_excel(file_path, sheet_name='Sheet1')  # Read the data from the specified sheet

# Parse the 'geometry' column to extract polygon boundaries
data['geometry_polygon'] = data['geometry'].apply(wkt.loads)  # Convert WKT strings to Shapely polygons

# Convert 'Farm Polygon' from JSON-like string to actual list of dictionaries
data['farm_polygon'] = data['Farm Polygon'].apply(lambda x: json.loads(x.replace("'", '"')))  # Convert JSON-like strings to Python dictionaries

def convert_farm_polygon_to_shapely(farm_polygon):
    """Convert farm polygon points to a Shapely Polygon."""
    points = [Point(p['longitude'], p['latitude']) for p in farm_polygon]  # Create a list of Shapely Points from the farm polygon coordinates
    return Polygon(points)  # Return a Shapely Polygon created from the list of points

def align_polygons(geometry_polygon, farm_polygon):
    """Align the farm polygon to match the geometry polygon boundaries."""
    farm_poly_shapely = convert_farm_polygon_to_shapely(farm_polygon)  # Convert the farm polygon to a Shapely Polygon
    
    # Get bounds of both polygons
    geo_bounds = geometry_polygon.bounds  # Get the bounding box of the geometry polygon
    farm_bounds = farm_poly_shapely.bounds  # Get the bounding box of the farm polygon
    
    # Calculate the necessary scale and translation factors
    scale_x = (geo_bounds[2] - geo_bounds[0]) / (farm_bounds[2] - farm_bounds[0])  # Calculate the scaling factor for the x-axis
    scale_y = (geo_bounds[3] - geo_bounds[1]) / (farm_bounds[3] - farm_bounds[1])  # Calculate the scaling factor for the y-axis
    
    trans_x = geo_bounds[0] - farm_bounds[0] * scale_x  # Calculate the translation factor for the x-axis
    trans_y = geo_bounds[1] - farm_bounds[1] * scale_y  # Calculate the translation factor for the y-axis
    
    # Apply affine transformation
    aligned_polygon = affine_transform(farm_poly_shapely, [scale_x, 0, 0, scale_y, trans_x, trans_y])  # Apply the scaling and translation to align the farm polygon with the geometry polygon
    
    return aligned_polygon  # Return the aligned polygon

# Apply the alignment to each row
data['aligned_polygon'] = data.apply(lambda row: align_polygons(row['geometry_polygon'], row['farm_polygon']), axis=1)  # Apply the align_polygons function to each row

# Display the first few rows to verify
print(data[['geometry_polygon', 'farm_polygon', 'aligned_polygon']].head())  # Print the first few rows of the DataFrame to check the results
