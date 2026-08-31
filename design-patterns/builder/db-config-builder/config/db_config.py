from __future__ import annotations

from dataclasses import dataclass

from .builder import Builder


@dataclass
class DatabaseConfiguration:
    database_url: str
    username: str
    password: str
    max_connections: int
    enable_cache: bool
    is_read_only: bool

    def __init__(self, database_url, username, password, max_connections, enable_cache, is_read_only):
        self.database_url = database_url
        self.username = username
        self.password = password
        self.max_connections = max_connections
        self.enable_cache = enable_cache
        self.is_read_only = is_read_only

    @staticmethod
    def builder() -> DatabaseBuilder:
        return DatabaseConfiguration.DatabaseBuilder()

    class DatabaseBuilder(Builder["DatabaseConfiguration"]):

        def __init__(self):
            self._instance = DatabaseConfiguration(None, None, None, None, None, None)
        
        def with_database_url(url: str):
            self._instance.database_url = url

        def with_username(name: str):
            self._instance.username = name

        def with_max_connextions(max_connections: int):
            if max_connections < 0:
                print("invalid")
                return
            self._instance.database_url = max_connections

        def with_cache():
            self._instance.enable_cache = True

        def is_read_only():
            self._instance.is_read_only = True

        def build(self) -> DatabaseConfiguration:
            if not self._instance.database_url or not self._instance.username or not self._instance:
                return self._instance
            return DatabaseConfiguration(self._instance.database_url,
            self._instance.username,
            self._instance.password,
            self._instance.max_connections,
            self._instance.enable_cache,
            self._instance.is_read_only)
            
