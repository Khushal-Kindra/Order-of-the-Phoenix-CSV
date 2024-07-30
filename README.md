# Order of the Phoenix CSV

This repository contains a Python application to process orders from a CSV file. The application computes various metrics from the order data and includes a separate testing module. The application and tests are containerized using Docker.

## Table of Contents

1. [Introduction](#introduction)
2. [Generating the Orders CSV](#generating-the-orders-csv)
3. [Project Directory](#project-directory)
4. [Application Files](#application-files)
5. [Dockerization](#dockerization)
6. [Running the Application](#running-the-application)
7. [Running the Tests](#running-the-tests)
8. [License](#license)

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

## Project Directory

Your project directory should look like this:
~~~
my_project/  
│  
├── Dockerfile  
├── docker-compose.yml  
├── main.py  
├── requirements.txt  
├── data_processing.py  
└── tests/  
    └── testing.py  
~~~

## Application Files

The application consists of three main Python files:

`main.py`
`data_processing.py`
`testing.py`

### Files Description

`main.py`

This is the main script that orchestrates the data reading, processing, and analysis. It includes the following components:

### Functions:

- read_csv_file(file_path): Reads a CSV file into a Pandas DataFrame, handling errors if the file does not exist or cannot be read.
- compute_metrics(df): Computes and prints various metrics from the DataFrame, such as monthly revenue, product revenue, customer revenue, and top customers by revenue.

### Main Function:

main(): The main function that sets the file path for the CSV file, reads the data, processes it using the process_data function from data_processing.py, and computes metrics. It serves as the entry point for the script.

`data_processing.py`

This module handles the data cleaning and preprocessing tasks. It includes the process_data(df) function, which performs the following operations on the DataFrame:

- Drops rows with missing values in critical columns (order_id, customer_id, product_id).
- Converts order_date to a datetime format, filling any missing or erroneous dates with a default value.
- Fills missing product_name values with 'Unknown'.
- Converts product_price to float, fills missing values with the mean price, and ensures no negative prices.
- Converts quantity to float, fills missing values with the median quantity, ensures no negative quantities, and converts back to integer.
- Adds a year_month column for grouping by month.

`testing.py`

This module contains unit tests for the data processing functionality using the unittest framework. It includes the following:

### Test Class:

- TestDataProcessing: Contains test cases for the process_data function.
- setUp(): Sets up a sample DataFrame from a CSV string for testing.
- test_process_data(): Tests various aspects of the process_data function, including handling of missing values, data type conversions, and the addition of the year_month 
    column. It includes assertions to verify that the processed DataFrame meets the expected criteria.

## Dockerization

To containerize the application, we will create a `Dockerfile` and a `docker-compose.yml` file.

## Build the Docker images:

  docker-compose build
  
A Docker image is a lightweight, standalone, and executable package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and configuration files.

## Running the Application
  
  docker-compose run app
  
## Running the tests:

  docker-compose run test

## License

This project is licensed under the MIT License. See the LICENSE file for details.

