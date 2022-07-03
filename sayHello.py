from app import app, db
from app.models import User


# Add database into flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
