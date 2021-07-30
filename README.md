# market-API
Simple Market API

###Created using:
* Django 3.2
* Django Rest 3.12
* MongoDb 4.0
* Swagger/OpenAPI 2.0

##  0.   Execute
To execute the api just download the git repository and inside its folder 
run the docker-compose file:

```bash
sudo docker-compose up
```

The API should be running on: [LOCALHOST:7000](127.0.0.1:7000)

##  1. Clarifications

The Database is populated with some users and categories, new ones can be 
created, or you can just play with the data, creating new products and adding 
them to the user's cart.
Exemplary data to test the API can be found in:
* example_data.js

## 2. Technical debt
* Improve the test coverage.
* Improve the documentation.
* Create a custom User (Customer, Seller)
* Create the Frontend based on [ReactApp](https://github.com/lucassing/REACT-.Js-Course)


