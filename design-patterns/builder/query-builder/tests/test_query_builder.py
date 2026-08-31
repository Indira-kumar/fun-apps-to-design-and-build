import unittest
from config import Query


class TestQueryBuilder(unittest.TestCase):

    def test_build_without_setting_fields(self):
        builder = Query.builder()
        query = builder.build()
        self.assertIsNotNone(
            query, "If the build method is called, it should return a non-None value"
        )
        self.assertIsInstance(
            query,
            Query,
            "If the build method is called, it should return an instance of Query",
        )

    def test_build_no_fields_set(self):
        builder = Query.builder()
        query = builder.build()

        self.assertIsNotNone(
            query, "If the build method is called, it should return a non-None value"
        )
        self.assertIsInstance(
            query,
            Query,
            "If the build method is called, it should return an instance of Query",
        )

        # Assert that all fields are None
        self.assertIsNone(
            query.select, "If no value is set, select should be None"
        )
        self.assertIsNone(
            query.from_, "If no value is set, from_ should be None"
        )
        self.assertIsNone(
            query.where, "If no value is set, where should be None"
        )
        self.assertIsNone(
            query.join, "If no value is set, join should be None"
        )
        self.assertIsNone(
            query.order_by, "If no value is set, order_by should be None"
        )
        self.assertIsNone(
            query.group_by, "If no value is set, group_by should be None"
        )

    def test_build_with_updated_instance(self):
        builder = Query.builder()
        builder._instance.select = "SELECT *"
        builder._instance.from_ = "FROM table"
        builder._instance.where = "WHERE condition"
        builder._instance.join = "INNER JOIN another_table ON condition"
        builder._instance.order_by = "ORDER BY column ASC"
        builder._instance.group_by = "GROUP BY column"

        query = builder.build()

        self.assertEqual(
            query.select,
            "SELECT *",
            "If the select is set, it should be returned",
        )
        self.assertEqual(
            query.from_, "FROM table", "If the from_ is set, it should be returned"
        )
        self.assertEqual(
            query.where, "WHERE condition", "If the where is set, it should be returned"
        )
        self.assertEqual(
            query.join, "INNER JOIN another_table ON condition", "If the join is set, it should be returned"
        )
        self.assertEqual(
            query.order_by,
            "ORDER BY column ASC",
            "If the order_by is set, it should be returned",
        )
        self.assertEqual(
            query.group_by,
            "GROUP BY column",
            "If the group_by is set, it should be returned",
        )


if __name__ == "__main__":
    unittest.main()
