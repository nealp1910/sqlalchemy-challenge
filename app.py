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
@app.route("/api/v1.0/precipitation")    
def precipitation():
    # Create our session (link) from Python to DB
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

################# Stations Route #######################################
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to DB
    session = Session(engine)
    """Weather Stations List"""
    # Design a query to calculate the total number stations in the dataset
    stations = session.query(station.station).all()
    # Return a JSON list of stations from the dataset.
    return jsonify(stations)











if __name__ == '__main__':
    app.run(debug=True)

