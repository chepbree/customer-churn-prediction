import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix, 
    roc_curve, auc, precision_recall_curve, ConfusionMatrixDisplay
)

def evaluate_model(model_name, model, X_test, y_test, plot_roc=True, plot_visuals=True):
    """
    Evaluates a classification model and plots the ROC curve.
    """
    # 1. Predictions
    y_pred = model.predict(X_test)
    
    # 2. Print Metrics
    print(f"\n{'='*20} {model_name} {'='*20}")
    print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # 3. Plot Confusion Matrix
    if plot_visuals:
     cm = confusion_matrix(y_test, y_pred)
     disp = ConfusionMatrixDisplay(confusion_matrix=cm)
     disp.plot(cmap='Blues', values_format='d')
     plt.title(f'Confusion Matrix - {model_name}')
     plt.ylabel('True Label')
     plt.xlabel('Predicted Label')
     plt.show()

    # 4. Plot ROC Curve
    if plot_roc:
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_prob)
            roc_auc = auc(fpr, tpr)

            plt.figure(figsize=(8, 6))
            plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
            plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title(f'ROC Curve - {model_name}')
            plt.legend(loc="lower right")
            plt.grid(alpha=0.3)
            plt.show()
        else:
            print(f"ROC Curve not available for {model_name}: model has no predict_proba.")

    return accuracy_score(y_test, y_pred)
