# Order of the Phoneix CSV

This repository contains a Python application to process orders from a CSV file. The application computes various metrics from the order data and includes a separate testing module. The application and tests are containerized using Docker.

## Table of Contents

1. [Introduction](#introduction)
2. [Generating the Orders CSV](#generating-the-orders-csv)
3. [Application Files](#application-files)
4. [Dockerization](#dockerization)
5. [Running the Application](#running-the-application)
6. [Running the Tests](#running-the-tests)
7. [License](#license)

## Introduction

This application reads orders data from a CSV file, processes the data, and computes various metrics such as total revenue by month, product, and customer. The application is built using Python and is containerized using Docker for ease of deployment and testing.

## Generating the Orders CSV

The `orders.csv` file can be generated using Mockaroo, a free online tool for generating mock data. The schema for the CSV file includes the following fields:

- `order_id`: Unique identifier for the order
- `customer_id`: Unique identifier for the customer
- `product_id`: Unique identifier for the product
- `order_date`: Date when the order was placed
- `product_name`: Name of the product
- `product_price`: Price of the product
- `quantity`: Quantity of the product ordered

Save the generated file as `orders.csv`.

## Application Files

The application consists of three main Python files:

1. `main.py`: Entry point of the application that reads the CSV file, processes the data, and computes the metrics.
2. `data_processing.py`: Contains the `process_data` function to clean and preprocess the data.
3. `test_data_processing.py`: Unit tests for the data processing functions.

## Dockerization

To containerize the application, we will create a Dockerfile and a `docker-compose.yml` file.

## Build the Docker images:

  docker-compose build

## Running the Application
  
  docker-compose run app
  
## Running the tests:

  docker-compose run test

## License

This project is licensed under the MIT License. See the LICENSE file for details.

