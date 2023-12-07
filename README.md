# classification_project

Angel Quintana
1 Dec 2023

Project Description
- We at Telco would like to now what factors drive customer churn. In this project I am investigating just that with the hopes of developing models that can accurately predict customer churn using available data. Understanding the features which lead to churn would allow for Telco to develop more effective marketing strategies, understand possible shortcomings in customer experience, and develop more efficient business solutions.

Project Goals
- Discover factors relating to customers terminating service with Telco
- Use said factors to develop modeling resources to predict churn

Initial Hypotheses 
- I assume contract_types, monthly charges, and whether or not a customer has phone/internet service to impact churn the most. 

-project planning 

    Aquire data using import/ sql query
    Prepare data
        -Handle nulls and blanks in data
        -Handle outliers
        -Distinguish categoricals and continous
        -Encode columns when neccesary
        
    Explore data in search of drivers of upsets
        -Do longer contract types correlate to higher churn??
        -Does monthly charge correlate to churn?
        -Do customers with phone service churn less?
        -Does whether or not customers have internet service correlate with churn?

    Develop a Model to predict if a customer will churn

        -Use features identified in explore to build predictive models of different types
        -Evaluate models on train and validate data
        -Select the best model based on highest accuracy
        -Evaluate the best model on test data
    Draw conclusions

-Conclusions

- Exploration
        
        - Churn accounts for about 73% of customers
        
- Modeling
        
        - Random Forest is the best model.
        
- Recomendations

        - Continue investigating for features that correlate to churn to develop more accurate models
        - Implement said models for establishing better business solutions