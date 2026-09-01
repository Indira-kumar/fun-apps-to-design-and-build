from typing import Dict

from .registry import ConfigurationPrototypeRegistry
from .app_config import Configuration, ConfigurationType

class ConfigurationPrototypeRegistryImpl(ConfigurationPrototypeRegistry):
    
    def __init__(self):
        self.prototypes: Dict[ConfigurationType, Configuration] = {}

    
    def add_prototype(self, configuration: Configuration) -> None:
        self.prototypes[configuration.type_] = configuration
    
    def get_prototype(self, type_: ConfigurationType) -> Configuration:
        if type_ not in self.prototypes:
            return None
        return self.prototypes[type_]
    
    def clone(self, type_: ConfigurationType) -> Configuration:
        if type_ not in self.prototypes:
            return None
        return self.prototypes[type_].clone_object()
