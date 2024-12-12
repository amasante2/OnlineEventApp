from app import app, db
from flask_migrate import Migrate
from flask.cli import with_appcontext
import click

# Initialize Migrate
migrate = Migrate(app, db)

# Initialize the Flask-Migrate commands
@app.cli.command("db_init")
@with_appcontext
def db_init():
    """Initialize the database migrations."""
    click.echo("Initializing migrations...")
    db.create_all()  # Create all tables if they don't exist (for initial setup)

@app.cli.command("db_migrate")
@with_appcontext
def db_migrate():
    """Run the database migration."""
    from flask_migrate import migrate, upgrade, init
    click.echo("Running migrations...")
    init()  # Initialize migrations (this creates the migration folder if not exists)
    migrate()  # Generates migration scripts
    upgrade()  # Apply the migrations

if __name__ == "__main__":
    app.run(debug=True)


