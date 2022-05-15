# sqlalchemy-challenge

### Instructions for this Homework assignment are under the Instructions Folder.

#### Part 1: Climate Analysis and Exploration
In this section, you’ll use Python and SQLAlchemy to perform basic climate analysis and data exploration of your climate database. Complete the following tasks by using SQLAlchemy ORM queries, Pandas, and Matplotlib.

- Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.

- Use SQLAlchemy’s create_engine to connect to your SQLite database.

- Use SQLAlchemy’s automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

- Link Python to the database by creating a SQLAlchemy session.

- Important: Don't forget to close out your session at the end of your notebook.

## Precipitation Analysis 
[![Percipitation-Within-Last-Year.png](https://i.postimg.cc/nhFmXG2Y/Percipitation-Within-Last-Year.png)](https://postimg.cc/RNYh8fjN)

## Station Analysis 
[![Most-Active-Station-Tobe.png](https://i.postimg.cc/3RmNSk9x/Most-Active-Station-Tobe.png)](https://postimg.cc/wyx93TSC)

#### Part 2: Design Your Climate App
Now that you have completed your initial analysis, you’ll design a Flask API based on the queries that you have just developed.
Use Flask to create your routes, as follows:
- /
  - Homepage.
  - List all available routes.

- /api/v1.0/precipitation
    - Convert the query results to a dictionary using date as the key and prcp as the value.
    - Return the JSON representation of your dictionary.

- /api/v1.0/stations
    - Return a JSON list of stations from the dataset.

- /api/v1.0/tobs
    - Query the dates and temperature observations of the most active station for the previous year of data.
    - Return a JSON list of temperature observations (TOBS) for the previous year.
    
- /api/v1.0/<start> and /api/v1.0/<start>/<end>
    - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
    - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date.
    - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive).
