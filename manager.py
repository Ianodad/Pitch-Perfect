from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


# user imports models
from app.models import User, Category, Pitch, Comment
# Creating app instance
app = create_app('development')


manager = Manager(app)

manager.add_command('server', Server)

# intiate migrate class
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# access to the shell


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Category=Category, Pitch=Pitch, Comment=Comment)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command('server', Server)


if __name__ == '__main__':
    manager.run()
