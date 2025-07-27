import os
import pathlib
import sys

import nest_asyncio


def init(verbose=False):
    workspace = pathlib.Path(__file__).resolve().parents[1]
    project_root = workspace / "app"

    try:
        nest_asyncio.apply()
        if verbose:
            print("Applied nest_asyncio patch for Jupyter compatibility")
    except ImportError:
        if verbose:
            print("nest_asyncio not available, skipping patch")

    # Set DATABASE_URL if not already set
    if not os.getenv("DATABASE_URL"):
        db_vars = {
            "user": os.getenv("POSTGRES_USER"),
            "pw": os.getenv("POSTGRES_PASSWORD"),
            "host": os.getenv("POSTGRES_HOST"),
            "port": os.getenv("POSTGRES_PORT"),
            "db": os.getenv("POSTGRES_DB"),
        }
        os.environ["DATABASE_URL"] = (
            f"postgresql://{db_vars['user']}:{db_vars['pw']}@{db_vars['host']}:{db_vars['port']}/{db_vars['db']}"
        )

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
        if verbose:
            print(f"Added {project_root} to sys.path")

    import django

    django.setup()


if __name__ == "__main__":
    init()
