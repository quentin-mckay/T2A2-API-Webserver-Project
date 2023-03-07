from controllers.auth_controller import auth
from controllers.users_controller import users
from controllers.projects_controller import projects
from controllers.comments_controller import comments

registerable_controllers = [
    auth,
    users,
    projects,
    comments
]