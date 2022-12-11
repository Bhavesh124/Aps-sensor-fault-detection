from dataclasses import dataclass

class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str
    
class DataValidationArtifact:
    report_file_path:str
    
class DataTransformationArtifact:...
class ModelEvalutionArtifact:...
class ModelTrainerArtifact:...
class ModelPusherArtifact:...