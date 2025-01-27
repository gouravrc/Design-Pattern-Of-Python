class ModelPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def __str__(self):
        return f"Pipeline Step: {' -> '.join(self.steps)}"


class PipelineBuilder:
    def __init__(self):
        self.pipeline = ModelPipeline()

    def add_scaler(self, scaler):
        """Adds scaler."""
        self.pipeline.add_step(f"Scaler: {scaler}")
        return self

    def add_feature_engineering(self, method):
        """Adds feature engineering"""
        self.pipeline.add_step(f"Feature Engineering: {method}")
        return self

    def add_model(self, model):
        """Adds model"""
        self.pipeline.add_step(f"Model: {model}")
        return self

    def add_evaluation(self, metric):
        """Adds evaluation"""
        self.pipeline.add_step(f"Evaluation Metric: {metric}")
        return self

    def build(self):
        """Returns the constructed pipeline."""
        return self.pipeline


if __name__ == "__main__":
    # Step-by-step pipeline construction
    builder = PipelineBuilder()
    pipeline = (
        builder
        .add_scaler("StandardScaler")
        .add_feature_engineering("PCA")
        .add_model("RandomForestClassifier")
        .add_evaluation("Accuracy")
        .build()
    )

    # Print the constructed pipeline
    print(pipeline)
