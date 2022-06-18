"""
IMPORTS
"""
import os
from bookworm import app


if __name__ == "main":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
