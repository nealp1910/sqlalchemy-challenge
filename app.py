# Part 2: Design Your Climate App

# Import libraries 
import numpy as np
import pandas as pd
import datetime as dt
from datetime import timedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
#Homepage.
#List all available routes
@app.route("/")
def welcome():
    """List of all available API routes."""
    return(
        f"List of all available API routes below:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

################# Precipitation Route #######################################
#Convert the query results to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")    
def precipitation():
    #Create our session (link) from Python to DB
    session = Session(engine)
    """Percipitation Data from Last Year"""
    #last date in database
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first().date
    # Calculate the date one year from the last date in data set.
    last_date = dt.datetime.strptime(last_date, "Y-%m-%d")
    first_date = last_date - timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    prcp_data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= first_date).all()
    return jsonify(prcp_data)

###################### Stations Route #######################################
#Return a JSON list of stations from the datase
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to DB
    session = Session(engine)
    """Weather Stations List"""
    # Design a query to calculate the total number stations in the dataset
    stations = session.query(station.station).all()
    # Return a JSON list of stations from the dataset.
    return jsonify(stations)

############################### Tobs #######################################
#Query the dates and temperature observations of the most active station for the previous year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobes():
    #Create our session (link) from Python to DB
    session = Session(engine)
    """Most Active Station Temperature Data from the Previous Year"""
    #last date in database
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first().date
    # Calculate the date one year from the last date in data set.
    last_date = dt.datetime.strptime(last_date, "Y-%m-%d")
    first_date = last_date - timedelta(days=365)
    # List the stations and the counts in descending order.
    active_station_count = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    top_station = (active_station_count[0])
    top_station = (top_station[0])
    # Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
    session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station == top_station).all()
    # Using the most active station id 
    # Query the last 12 months of temperature observation data for this station and plot the results as a histogram
    most_active_station_tobs = session.query(measurement.tobs).filter(measurement.date >= first_date).all()
    return jsonify(most_active_station_tobs)

############################### Start/End #######################################
#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date.
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive).
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    


if __name__ == '__main__':
    app.run()

