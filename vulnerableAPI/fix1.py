from config import db, vuln_app
from models.user_model import User
from sqlalchemy import text

with vuln_app.app.app_context():
    # Establish a connection
    with db.engine.connect() as connection:
        # Drop the users table if it exists
        connection.execute(text("DROP TABLE IF EXISTS users"))
        print("Dropped 'users' table if it existed.")

    # Recreate all tables
    db.create_all()
    print("Tables recreated successfully!")
