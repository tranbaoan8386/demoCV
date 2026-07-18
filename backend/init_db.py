"""Database initialization helpers.

This project now relies on Alembic migrations for schema management.
This module is intentionally lightweight so it can be used later for seed data
without bypassing the migration workflow.
"""

from __future__ import annotations


def init_database() -> None:
    """Placeholder entrypoint for future seed-data initialization.

    The schema is created and versioned by Alembic. If seed data is ever needed,
    it should be inserted here after the migration command has completed.
    """
    print("No seed data initialization is required at the moment.")


if __name__ == "__main__":
    init_database()