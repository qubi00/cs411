from typing import Any

class Migration:

    def __init__(self,
                migration_id: int,
                migration_path: MigrationPath,
                start_date: str,
                current_date: str,
                current_location: str,
                status: str = "Scheduled"
                )
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.start_date = start_date
        self.current_date = current_date
        self.status = status
        self.current_location = current_location

    def update_migration_details(self, **kwargs: Any) -> None:
        pass
    
    def get_migration_details(self) -> dict[str, Any]:
        pass