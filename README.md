# Team Charizard NUber Project

For Mr. Diaz's CS 3398 Software Engineering class, we have created a RESTful API which will serve as the backend for our new, ingenius, never-before-thought-of business proposal...NUber

<hr>

### We implemented our backend with the Python3 programming language. This was our technology stack:
- The Flask Microframework
- Flask_RESTful
- Flask_SQLAlchemy
- Flask_Marshmallow
- Flask_Migrate
- Marshmallow_SQLAlchemy
- Google Maps API

<hr>

### How to run
1. Be sure to have Python3 and Pip installed on your computer
2. Install *virtualenv* with Pip <br>
```pip install virtualenv```
3. *cd* into the project folder and create a virtual environment <br>
```virtualenv -p python3 venv```
4. Activate virtual environment <br>
```source venv/bin/activate```
5. Install all dependencies listed in *requirements.txt* <br>
```pip install -r requirements.txt```
6. Create a binary executable of *create_database.sh* <br>
```chmod 755 create_database.sh```
7. Run *create_database.sh* to make a new instance of your database <br>
```./create_database.sh```
8. RUN DAT BOI:sunglasses:
```python main.py```

### When you spin up the server, you should see output like the following:
```
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 295-600-791
```
<hr>

### How to Use Extra Features

- Groups :: Riders have an attribute field named 'groupHost', by setting 
            your 'groupHost' to another rider's 'name' you will be added to their group. When in 
            a group only the group host can select a driver.
- RideCost :: Riders have an attribute called 'outstandingBalance', this holds how much 
              money riders owe their driver, this cost is divided by the number of people in the group.
- Radius Search :: Drivers have attribute fields 'avaiable', 'lat', and 'long' which describe their availability and location. These                        fields allow for riders to search for potential drivers based on their availability and relative distance from the                      rider
- Charge Riders :: Drivers obviously wish to be paid. Once a Rider has reached their destination, calculations are performed based on                      how far the rider was transported from their original location, and a cost is assigned at a fixed rate per mile.
- Rating System :: Each Driver posseses a 'rating' attribute, which holds an aggregate average of their ratings, given to them by                          previous Riders. This Rating System is used to assess the overall perceived quality of the Driver.

<hr>

### Routes
Below are the available list of routes and their functionalities

#### Admin
- ```/admin```
  - GET:
  
  - POST:
  
  - PUT:
  
  - DELETE:

- ```/admin/driver```
  - GET: Returns a list of all drivers in the database
    - Arguments: None
  - POST: Creates a new driver
    - Arguments: 
      - id: integer
      - name: string
  - PUT:
  - DELETE: Deletes a driver from the database
    - Arguments:
      - id: integer


- ```/admin/rider```
  - GET:
  
  - POST:
  
  - PUT:
  
  - DELETE:


#### Driver
- ```/driver/update_position```
  - PUT:
  
- ```/driver/update_availability```
  - PUT:
  
- ```/driver/get_rider_destination```
  - GET:

- ```/driver/get_rider_location```
  - GET:

- ```/driver/get_rider_charge```
  - GET:

#### Rider
- ```/rider/set_destination```
  - PUT:
  
- ```/rider/update_position```
  - PUT:

- ```/rider/select_driver```
  - PUT:

- ```/rider/get_drivers```
  - GET:

- ```/rider/get_driver_location```
  - GET:
  
