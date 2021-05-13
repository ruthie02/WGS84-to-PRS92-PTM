from pyproj import Transformer, CRS


def Geog_Proj(Latitude, Longitude, Elev, Zone):
    # initialize a variable using the EPSG code from spatial reference
    PRS92 = CRS.from_epsg(4995)
    WGS84 = CRS.from_epsg(4979)
    PRS92Z1 = CRS.from_epsg(3121)
    PRS92Z2 = CRS.from_epsg(3122)
    PRS92Z3 = CRS.from_epsg(3123)
    PRS92Z4 = CRS.from_epsg(3124)
    PRS92Z5 = CRS.from_epsg(3125)
    
    # this is to convert WGS84 to PRS92
    transform_WGS84_PRS92_geog = Transformer.from_crs(WGS84, PRS92)
    LatG, LongG, ElevG =  transform_WGS84_PRS92_geog.transform(Latitude, Longitude, Elev)

    # choosing the correct zone to transform to PTM
    if PTM_zone == 1:
        transform_geog_proj = Transformer.from_crs(PRS92, PRS92Z1)

    elif PTM_zone == 2:
        transform_geog_proj = Transformer.from_crs(PRS92, PRS92Z2)

    elif PTM_zone == 3:
        transform_geog_proj = Transformer.from_crs(PRS92, PRS92Z3)

    elif PTM_zone == 4:
        transform_geog_proj = Transformer.from_crs(PRS92, PRS92Z5)
    
    elif PTM_zone == 5:
        transform_geog_proj = Transformer.from_crs(PRS92, PRS92Z4)

    Northing, Easting, Height = transform_geog_proj.transform(LatG, LongG, ElevG)
    return Northing, Easting, Height


#this computes the N, E , and H 
Latitude = float(input("Lat: "))
Longitude = float(input("Long: "))
Elev = float(input("Elevation: "))
PTM_zone = int(input("Enter which zone: "))
Transformed = print(Geog_Proj(Latitude, Longitude, Elev, PTM_zone))

# try to add conversion for PTM to WGS84
# I will edit this code as soon as possible