# Week 3

## Question 1

### Create and external table
```SQL
CREATE OR REPLACE EXTERNAL TABLE `jan-swart.ny_taxi.external_green_tripdata`
    OPTIONS (
    format = 'parquet',
    uris = ['gs://trips-batch-bucket/green/green_tripdata_2022-*.parquet']
);
```

### Create table in BQ (non partitioned / non clustered):
```SQL
CREATE OR REPLACE TABLE jan-swart.ny_taxi.green_tripdata_non_partitoned AS
SELECT * FROM jan-swart.ny_taxi.external_green_tripdata;
```


## Question 2

### Estimate bytes

```SQL
SELECT COUNT(DISTINCT PULocationID)
FROM jan-swart.ny_taxi.external_green_tripdata;
```

```SQL
SELECT COUNT(DISTINCT PULocationID)
FROM jan-swart.ny_taxi.green_tripdata_non_partitoned;

```

## Question 3

### Count records with 0 fare amount

```SQL
SELECT count(*) as zero_amount_trips
FROM jan-swart.ny_taxi.green_tripdata_non_partitoned
WHERE fare_amount = 0;
```

## Question 4

```SQL
CREATE OR REPLACE TABLE jan-swart.ny_taxi.green_tripdata_partitoned
PARTITION BY
DATE(lpep_pickup_datetime) AS
    SELECT * FROM jan-swart.ny_taxi.external_green_tripdata;
```

## Question 5

```SQL
SELECT DISTINCT(PULocationID)
FROM jan-swart.ny_taxi.green_tripdata_non_partitoned
WHERE lpep_pickup_datetime BETWEEN "2022-06-01" AND "2022-06-30"
```

```SQL
SELECT DISTINCT(PULocationID)
FROM jan-swart.ny_taxi.green_tripdata_partitoned
WHERE lpep_pickup_datetime BETWEEN "2022-06-01" AND "2022-06-30";
```

## Question 8

```SQL
SELECT count(*)
FROM jan-swart.ny_taxi.green_tripdata_partitoned
```