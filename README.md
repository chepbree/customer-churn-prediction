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


## 📊 Dataset

The dataset contains customer-related information including:

* Call usage (total minutes, day minutes)
* Customer service interactions
* Subscription details


## ⚙️ Methodology

### Data Processing

* Feature engineering applied to usage variables
* Categorical variables encoded using pipelines
* Data split into training and testing sets

### Models Implemented

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* Voting Ensemble


## 📈 Model Performance

| Model               | Accuracy   | Precision  | Recall     | F1         | ROC AUC |
| ------------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| Random Forest       | 0.9595     | 0.9743     | 0.7525     | 0.8492     | 0.9386  |
| Gradient Boosting   | **0.9625** | 0.9524     | **0.7921** | **0.8649** | 0.9311  |
| Voting Ensemble     | 0.9595     | **0.9868** | 0.7426     | 0.8475     | 0.9297  |
| Decision Tree       | 0.9265     | 0.7549     | 0.7624     | 0.7586     | 0.8591  |
| Logistic Regression | 0.8576     | 0.6000     | 0.1782     | 0.2748     | 0.8281  |


## 🏆 Final Model

**Gradient Boosting** was selected due to:

* Highest accuracy and F1-score
* Strong recall for detecting churn
* Stable performance across cross-validation

---

## 🔍 Key Insights

* High **total usage (minutes)** increases churn likelihood
* Frequent **customer service calls** indicate dissatisfaction
* Customer behavior patterns are strong predictors of churn

---

## 🚀 Business Recommendations

* Improve customer service response for frequent callers
* Offer personalized plans for high-usage customers
* Use model predictions to identify high-risk customers early
* Implement targeted retention strategies


## ⚠️ Limitations

* Dataset may not include all churn factors
* Feature importance does not imply causation
* Model performance may vary with new data


## 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* Matplotlib


## 📈 Conclusion

Machine learning models can effectively predict customer churn and provide valuable insights. Applying these insights can help businesses reduce churn and improve customer satisfaction.


