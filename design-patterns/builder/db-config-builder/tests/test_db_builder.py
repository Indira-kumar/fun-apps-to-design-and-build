import unittest
from config import DatabaseConfiguration


class TestDatabaseBuilder(unittest.TestCase):

    def test_build_without_setting_fields(self):
        builder = DatabaseConfiguration.builder()
        config = builder.build()
        self.assertIsNotNone(
            config, "If the build method is called, it should return a non-None value"
        )
        self.assertIsInstance(
            config,
            DatabaseConfiguration,
            "If the build method is called, it should return an instance of DatabaseConfiguration",
        )

    def test_build_no_fields_set(self):
        builder = DatabaseConfiguration.builder()
        config = builder.build()

        self.assertIsNotNone(
            config, "If the build method is called, it should return a non-None value"
        )
        self.assertIsInstance(
            config,
            DatabaseConfiguration,
            "If the build method is called, it should return an instance of DatabaseConfiguration",
        )

        # Assert that all fields are None
        self.assertIsNone(
            config.database_url, "If no value is set, database_url should be None"
        )
        self.assertIsNone(
            config.username, "If no value is set, username should be None"
        )
        self.assertIsNone(
            config.password, "If no value is set, password should be None"
        )
        self.assertIsNone(
            config.max_connections, "If no value is set, max_connections should be None"
        )
        self.assertIsNone(
            config.enable_cache, "If no value is set, enable_cache should be None"
        )
        self.assertIsNone(
            config.is_read_only, "If no value is set, is_read_only should be None"
        )

    def test_build_with_updated_instance(self):
        builder = DatabaseConfiguration.builder()
        builder._instance.database_url = "example.com"
        builder._instance.username = "user"
        builder._instance.password = "password"
        builder._instance.max_connections = 10
        builder._instance.enable_cache = True
        builder._instance.is_read_only = False

        config = builder.build()

        self.assertEqual(
            config.database_url,
            "example.com",
            "If the database_url is set, it should be returned",
        )
        self.assertEqual(
            config.username, "user", "If the username is set, it should be returned"
        )
        self.assertEqual(
            config.password, "password", "If the password is set, it should be returned"
        )
        self.assertEqual(
            config.max_connections,
            10,
            "If the max_connections is set, it should be returned",
        )
        self.assertTrue(
            config.enable_cache, "If the enable_cache is set, it should be returned"
        )
        self.assertFalse(
            config.is_read_only, "If the is_read_only is set, it should be returned"
        )


if __name__ == "__main__":
    unittest.main()
