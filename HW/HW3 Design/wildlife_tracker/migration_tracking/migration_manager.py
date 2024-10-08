from typing import Any, List

from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:

    def __init__(self) -> None:
        migrations: dict[int, Migration] = {}
        paths: dict[int, MigrationPath] = {}

    def cancel_migration(self, migration_id: int) -> None:
        pass

    def schedule_migration(self, migration_path: MigrationPath) -> None:
        pass

    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:
        pass

    def get_migration_by_id(self, migration_id: int) -> Migration:
        pass

    def get_migration_details(self, migration_id: int) -> dict[str, Any]:
        pass

    def get_migrations(self) -> list[Migration]:
        pass

    def get_migrations_by_current_location(self, current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(self, migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(self, start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(self, status: str) -> list[Migration]:
        pass

