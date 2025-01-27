from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Creating Factory Class to create object 
# return model dynamically
class Factory:

    @staticmethod
    def get_model(model_type, **kwargs):
        """Factory method returns ML models dynamically"""
        if model_type == "logistic_regression":
            return LogisticRegression(**kwargs)
        elif model_type == "random_forest":
            return RandomForestClassifier(**kwargs)
        elif model_type == "svm":
            return SVC(**kwargs)
        else:
            raise ValueError(f"Unknown model: {model_type}")

if __name__ == "__main__":
    # Step 1 - Loading dataset
    df = load_iris()
    X = df.data
    Y = df.target

    # Step 2 -  Split the dataset into train and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=10)

    # Step 3 -  Define model type and parameters
    model_type = "logistic_regression"  # Change this to "logistic_regression" or "svm" to test different models

    model_params = {"n_estimators": 100, "random_state": 20}
    # Step 4 -  Creating model using the factory dynamically
    model = Factory.get_model(model_type, **model_params)

    # Step 5 - Build a pipeline
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", model)
    ])

    # Step 6 - Train the model
    pipeline.fit(X_train, Y_train)

    # Step 7 - Evaluate the model
    accuracy = pipeline.score(X_test, Y_test)
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Model: {model_type}")

