MISSING VALUES

    1. What is the missing datatype used in pandas?
           np.nan

    2. How to replace all occurrences of the value 9999 to missing in pandas?
           df = df.replace(9999, np.nan)

    3. How to get the absolute number of missing for each variable in pandas?
           df.isna().sum()

    4. How to get the percentage of missings for each variable in pandas?
           df.isna.sum() / df.shape[0]

    5. How to drop rows with missing values?
           df = df.notna()
           df.dropna(axis=0, inplace=True)

    6. How to drop variables with missing values?
           df.dropna(axis=1, inplace=True)

    7. What is the univariate imputation method in sklearn?
           A specific value or a mean/median/mode

    8. What is the multivariate imputation method in sklearn?
           Based on other features

    9. What is the best univariate imputation method to categorical variables? (Explain why)
           constant – if value is missing it adds a missing category. With categorical variables it either is or it isn’t something. We don’t want an average as this would create many more categories
           most frequent

    10. What is the best univariate imputation method to numerical variables? (Explain why)
           depends on the variable but mean is probably the best.

OUTLIERS

    1. What is an outlier?
           A convenient definition of an outlier is  a point which falls more than 1.5 times the interquartile range above the third quartile or below the first quartile.. In laments terms something that doesn’t fit the overall pattern of the data.

    2. What is a simple method to detect and deal with outliers of a numerical variable
           EDA and drop data that doesn’t fall into an inlier range. Or use an estimator:
           estimator.fit(X_train) → estimator.predict(X_test) → then drop those with a -1 score.

    3. What is novelty detection?
           Detecting whether a new observation is an outlier

    4. Name 4 advanced methods of outlier detection in sklearn.
           robust covariance | one-class SVM | isolation forest | Local Outlier Factor

TYPOS

    1. What is a typo?
		Where data has been gathered but entered incorrectly

    2. What is a good method of automatically detect typos?
           Check unique value counts. Check structure using regex

SAN FRANSICO BUILDING PERMITS
Consider the following dataset: San Francisco Building Permits. Look at the columns "Street Number Suffix" and "Zipcode". Both of these contain missing values.

    Which, if either, are missing because they don't exist?
      street number suffix may only exist if it is assigned on
    Which, if either, are missing because they weren't recorded?
      zipcode...everywhere has a zipcode pretty much. Very likely considering there is a road name.
