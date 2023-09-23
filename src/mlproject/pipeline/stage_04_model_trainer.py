from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_trainer import ModelTrainer



class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
            try:
                config=ConfigurationManager()
                model_trainer_config=config.get_model_trainer_config()
                model_trainer = ModelTrainer(config=model_trainer_config)
                model_trainer.train()
                
                
            except Exception as e:
                raise e