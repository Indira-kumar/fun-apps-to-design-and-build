import unittest

from config import Configuration, ConfigurationType, ConfigurationPrototypeRegistryImpl


class TestConfigurationPrototypeRegistryImpl(unittest.TestCase):

    def setUp(self):
        self.registry = ConfigurationPrototypeRegistryImpl()

        # Sample configurations
        self.basic_config = Configuration(
            "white", True, "English", False, 12, "Arial", ConfigurationType.BASIC
        )
        self.advanced_config = Configuration(
            "black", False, "Spanish", True, 14, "Helvetica", ConfigurationType.ADVANCED
        )
        self.custom_config = Configuration(
            "blue",
            True,
            "French",
            True,
            16,
            "Times New Roman",
            ConfigurationType.CUSTOM,
        )

        # Add sample configurations to the registry
        self.registry.prototypes = {
            ConfigurationType.BASIC: self.basic_config,
            ConfigurationType.ADVANCED: self.advanced_config,
        }

    def test_clone_object(self):
        # Test cloning the configuration
        cloned_config = self.basic_config.clone_object()
        self.assertIsNot(
            cloned_config,
            self.basic_config,
            "If an object is cloned, it should not be the same as the original.",
        )
        self.assertEqual(
            cloned_config.theme_color,
            self.basic_config.theme_color,
            "If an object is cloned, the theme colour should be the same as the original.",
        )
        self.assertEqual(
            cloned_config.auto_save,
            self.basic_config.auto_save,
            "If an object is cloned, the auto save flag should be the same as the original.",
        )

    def test_clone(self):
        # Test cloning an existing configuration
        cloned_config = self.registry.clone(ConfigurationType.BASIC)
        
        self.assertIsNotNone(cloned_config, "If the configuration exists, it should be cloned.")
        self.assertEqual(cloned_config.theme_color, self.basic_config.theme_color, "If the configuration exists, the theme colour should be the same as the original.")
        self.assertEqual(cloned_config.auto_save, self.basic_config.auto_save, "If the configuration exists, the auto save flag should be the same as the original.")
        # Add more assertions for other fields

        # Test cloning a non-existent configuration
        non_existent_clone = self.registry.clone(ConfigurationType.DEFAULT)
        self.assertIsNone(non_existent_clone, "If the configuration does not exist, it should return None.")

    def test_add_prototype(self):
        # Test adding a new prototype
        initial_size = len(self.registry.prototypes)
        self.registry.add_prototype(self.custom_config)
        
        self.assertEqual(len(self.registry.prototypes), initial_size + 1, "If a new prototype is added, the size of the registry should increase by 1.")
        
        custom_config = self.registry.prototypes[ConfigurationType.CUSTOM]
        self.assertEqual(custom_config, self.custom_config, "If a new prototype is added, it should be accessible from the registry.")

    def test_get_prototype(self):
        # Test getting an existing prototype
        basic_config = self.registry.get_prototype(ConfigurationType.BASIC)
        self.assertEqual(basic_config, self.basic_config, "If the configuration exists, it should be accessible from the registry.")

        # Test getting a non-existent prototype
        non_existent_config = self.registry.get_prototype(ConfigurationType.DEFAULT)
        self.assertIsNone(non_existent_config, "If the configuration does not exist, it should return None.")


if __name__ == "__main__":
    unittest.main()
