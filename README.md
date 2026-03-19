# customer-churn-prediction


## 📌 Project Overview

This project aims to predict customer churn using machine learning techniques. The objective is to identify customers who are likely to leave a SyriaTel service and provide actionable insights to improve retention strategies.

## Business Understanding

#### Problem
SyriaTel is experiencing customer churn, which leads to revenue loss. Retaining existing customers is often more cost-effective than acquiring new ones. Therefore, identifying customers who are likely to stop using SyriaTel’s services allows the company to implement proactive retention strategies

#### Stakeholders
Executive leaders(CEO/CFO)

Marketing team

Customer success

### Goal
The goal of this project is to build a classification model that predicts whether a customer will churn. This prediction can help the company take preventive measures to retain customers.


## 📊 Data Understanding
The dataset contains 3,333 customer records with 21 features, including:

Key Feature Categories:

Usage behavior (minutes, calls)

Service plans (international plan, voicemail plan)

Customer interactions (customer service calls)

Target Variable
churn (0 = No, 1 = Yes)


## Data Processing

The following preprocessing steps were applied:

Converted target variable (churn) to numeric

Removed identifiers (phone number)

Removed redundant features (charge columns due to multicollinearity)

Performed feature engineering:

Total minutes
Total calls
Service call rate
Usage ratios
To prevent data leakage, splitting, preprocessing and feature engineering were applied using Scikit-learn pipelines.

## Modelling

### Models Implemented

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* Voting Ensemble

## Evaluation

Evaluation Metrics
The models were evaluated using:

Recall → prioritized to reduce missed churners
Precision → measures accuracy of churn predictions
F1-score → balance between precision and recall
Confusion Matrix → shows prediction errors
ROC Curve & AUC → evaluates model discrimination ability

## 📈 Model Performance

| Model               | Accuracy   | Precision  | Recall     | F1         | ROC AUC |
| ------------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| Random Forest       | 0.9595     | 0.9743     | 0.7525     | 0.8492     | 0.9386  |
| Gradient Boosting   | **0.9625** | 0.9524     | **0.7921** | **0.8649** | 0.9311  |
| Voting Ensemble     | 0.9595     | **0.9868** | 0.7426     | 0.8475     | 0.9297  |
| Decision Tree       | 0.9265     | 0.7549     | 0.7624     | 0.7586     | 0.8591  |
| Logistic Regression | 0.8576     | 0.6000     | 0.1782     | 0.2748     | 0.8281  |


Interpretation

Gradient Boosting achieved the highest F1-score (0.865)
- This means it provides the best balance between precision and recall, making it the most effective at identifying churners while limiting false predictions.

Random Forest achieved the highest ROC AUC (0.939)
- This indicates it has a slightly better ability to distinguish between churners and non-churners overall, but its lower F1-score suggests it is less balanced in actual predictions.

Voting Ensemble did not outperform individual models
- This suggests that combining models did not add value, because Gradient Boosting already captures the patterns effectively

-Logistc regression performed poorely  in overall perfomance compared to the models

## Visuals

 - Gradient boosting confusion matrix which shows that this model is our top choice for churn prevention. It correctly identified 80 churners and had the lowest "miss" rate (only 21 False Negatives). This ensures the business captures the most at-risk revenue.

![Confusion Matrix](images/gb%20confusion%20matrix.png)

![ROC-AUC curve of GB](images/ROC-AUc%20curve.png)


- feature inportance to see which features are high in leading to customer churn

![Feature importance ](images/feature%20importnace.png)


## Perfomance Analysis

Among the evaluated models, Gradient Boosting achieved the highest F1-score, indicating the best balance between precision and recall.

Although Random Forest had a slightly higher ROC AUC, the difference was marginal, and F1-score is more relevant for this problem.

The Voting Classifier did not outperform individual models, suggesting that combining models did not provide additional benefit.

Therefore, Gradient Boosting is selected as the final model.


## 🔍 Key Insights on feature importance

* High **total usage (minutes)** increases churn likelihood
* Frequent **customer service calls** indicate dissatisfaction
* Customer behavior patterns are strong predictors of churn



## 🚀 Business Recommendations
*  Use Gradient Boosting for Deployment.Deploy the Gradient Boosting model to predict churn in real time
* Improve customer service response for frequent callers
* Offer personalized plans for high-usage customers
* Use model predictions to identify high-risk customers early
* Implement targeted retention strategies


## ⚠️ Limitations

* Dataset may not include all churn factors like external data (e.g., competitor pricing)
* Feature importance does not imply causation
* Model performance may vary with new data


## 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* Matplotlib


## 📈 Conclusion


The analysis shows that Gradient Boosting is the best-performing model, achieving the highest F1-score and providing a strong balance between precision and recall.

This makes it well-suited for predicting customer churn, where correctly identifying at-risk customers is critical.

By deploying this model, SyriaTel can proactively target customers likely to churn and implement retention strategies, ultimately reducing revenue loss and improving customer loyalty.


