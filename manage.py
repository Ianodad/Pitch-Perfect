from app import create_app, db
from flask_script import Manager, Server

# user imports models
from app.models import User, Catergory, Post, Comment
# Creating app instance
app = create_app('development')


manager = Manager(app)

manager.add_command('server', Server)

# manager.add_command('db', MigrateCommand)

# access to the shell


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Catergory=Catergory, Post=Post, Comment=Comment)


if __name__ == '__main__':
    manager.run()
