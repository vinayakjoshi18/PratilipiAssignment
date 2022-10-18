# PratilipiAssignment
## Exploratory Analysis
The data given to me was in the form of two CSVs, the first one is named ‘user-interactions.csv’, containing columns of ‘user_id’, ‘pratilipi_id’, ‘read_percent’, and ‘updated_at’, and the second one is ‘metadata.csv’, containing columns of ‘author_id’, ‘pratilipi_id‘, ‘category_name’, ‘reading_time’, ‘updated_at’, and ‘published_at’. In ‘metadata.csv’ there were a lot of duplicate mentions of pratilipi_id, reading_time, and published_at but with a different category_name.

## Data Cleaning and Preperation 
The main part of data cleaning was joining the two CSVs together on the basis of pratilipi_id. 
After doing this, the Null values, were exchanged with zero. The next step was categorical encoding where in layman's terms, I converted categorical data into integer format so that the data with converted values could be provided to different models.

#### Note That, due to low availability of good resources with me, I was unable to complete the assignment with the complete data, as a result, I selected the first 20,000 rows of the joined data for doing all my computations(data modeling, training and evaluations).

## Models and Approaches
There are basically two popular approaches for such reccomendation problems, the first one is content-based filtering but this usually works when there is less number of users in the data, the other is collaborative filtering, which addresses quiet a few of the limitations presented to us by content-based filtering, collaborative filtering uses similarities between users and items simultaneously to provide recommendations. 
Firstly we have used Cosine Similarity - This is a probablistic approcach towards our problem, based on the ideas of collaborative filtering. 
Secondly we have used a custom built shallow neural network, with one layer, and LeakyReLU as the activation function. 

## Improvements
This firstly will be improved whenI use the complete data, instead of using the first 20,000 rows. After getting the data we can improve the models with hyperparameter tuning and we can also improve it by running operations on the metedata.csv, in such a way that there remain only unique pratilipi_id and the multiple categories of a single pratilipi are shown in the same row, instead of different rows of the data. A code for this approach has been shared by the name of 'row-merge.py'.

