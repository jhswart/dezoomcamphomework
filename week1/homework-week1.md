# Week 1

## Question 1
--rm                             Automatically remove the container when it exits

## Question 2
0.42.0

```
$ docker run -it python:3.9 bash 
$ root@e248c68bb698:/# pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 58.1.0
wheel      0.42.0
```

## Question 3

```
SELECT 
	count(*)
FROM 
	green_taxi_data
WHERE 
	CAST(lpep_pickup_datetime AS DATE) = '2019-09-18' AND
	CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18'
```

## Question 4

```
SELECT MAX(trip_distance), CAST(lpep_pickup_datetime AS DATE) 
	FROM green_taxi_data 
	GROUP BY CAST(lpep_pickup_datetime AS DATE)
	ORDER BY MAX(trip_distance) DESC
```

## Question 5

```
SELECT SUM(total_amount) as total_location_amount, zones."Borough"
	FROM green_taxi_data, zones
WHERE
	CAST(lpep_pickup_datetime AS DATE) = '2019-09-18' AND
	CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18' AND
	zones."Borough" != 'Unknown' AND
	green_taxi_data."PULocationID" = zones."LocationID"
GROUP BY zones."Borough"
ORDER BY total_location_amount DESC
LIMIT 3;
```

## Question 6

```
SELECT MAX(tip_amount), green_taxi_data."DOLocationID", zones."Zone"
	FROM green_taxi_data, zones
WHERE
	green_taxi_data."PULocationID" = (
		SELECT zones."LocationID" FROM zones WHERE zones."Zone" = 'Astoria'
	) AND
	green_taxi_data."DOLocationID" = zones."LocationID"
GROUP BY green_taxi_data."DOLocationID", zones."Zone"
ORDER BY MAX(tip_amount) DESC
LIMIT 1;
```

## Question 7
