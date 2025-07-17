# FoCS project
This is the project for the Foundation of Computer Science exam of the Data Science master's degree.

## Description 
This project analyzes a real-world dataset of taxi trips in New York City, based on the NYC Yellow Taxi Fare dataset. The dataset includes information about trip duration, distance, fare amount, pickup/dropoff locations, payment types, and more.

The goal of this analysis is to extract key insights and patterns from the data by performing various operations such as:

* filtering trips based on distance or missing values;
* aggregating statistics by pickup/dropoff location and time intervals;
* creating custom time-based features (e.g., 30-minute pickup windows);
* identifying the most frequent routes and time-based fare trends;
* calculating ratios such as tip-to-fare for different payment methods;
* detecting chains of consecutive trips by the same vendor.

The notebook is structured step-by-step, following a set of well-defined tasks that demonstrate exploratory data analysis, data cleaning, grouping and aggregation, time series processing, and advanced filtering logic.

## Dataset

The dataset is avalaible on Kaggle, here the link [NYC Trip Fare](https://www.kaggle.com/api/v1/datasets/download/diishasiing/revenue-for-cab-drivers/
). It's possibile to skip the `store_and_fwd_flag` column, but it’s a bonus point if manage it correctly.

## Notes

1. It is mandatory to use GitHub for developing the project.
2. The project must be a jupyter notebook.
3. There is no restriction on the libraries that can be used, nor on the Python version.
4. All questions on the project must be asked in the Discussion forum on the course website.
5. At most 3 students can be in each group. You must create the groups by yourself. You can use the Discussion forum to create the groups.
6. You do not have to send me the project *before* the discussion.
7. You do not have to prepare any slides for the discussion.

## Project questions

1. Extract all trips with `trip_distance` larger than 50
2. Extract all trips where `payment_type` is missing
3. For each (`PULocationID, DOLocationID`) pair, determine the number of trips
4. Save all rows with missing `VendorID`, `passenger_count`, `store_and_fwd_flag`, `payment_type` in a new dataframe called `bad`, and remove those rows from the original dataframe.
5. Add a duration column storing how long each trip has taken (use `tpep_pickup_datetime`, `tpep_dropoff_datetime`)
6. For each pickup location, determine how many trips have started there.
7. Cluster the pickup time of the day into 30-minute intervals (e.g. from 02:00 to 02:30)
8. For each interval, determine the average number of passengers and the average fare amount.
9. For each payment type and each interval, determine the average fare amount
10. For each payment type, determine the interval when the average fare amount is maximum
11. For each payment type, determine the interval when the overall ratio between the tip and the fare amounts is maximum
12. Find the location with the highest average fare amount
13. Build a new dataframe (called `common`) where, for each pickup location we keep all trips to the 5 most common destinations (i.e. each pickup location can have different common destinations).
14. On the `common` dataframe, for each payment type and each interval, determine the average fare amount
15. Compute the difference of the average fare amount computed in the previous point with those computed at point 9.
16. Compute the ratio between the differences computed in the previous point and those computed in point 9. Note: you have to compute a ratio for each pair (payment type, interval).
17. Build *chains* of trips. Two trips are consecutive in a chain if (a) they have the same VendorID, (b) the pickup location of the second trip is also the dropoff location of the first trip, (c) the pickup time of the second trip is after the dropoff time of the first trip, and (d) the pickup time of the second trip is at most 2 minutes later than the dropoff time of the first trip.

*Hint*: Add a column `chain` to the dataset. A chain can have more than two trips.