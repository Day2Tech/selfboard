import gitlab
from ..config import GITLAB_URL, GITLAB_GROUP_ID, GITLAB_DEFAULT_LEVEL
class GitLab:
    def __init__(self, token):
        self.token = token
        self.g = False

    def login(self):
        if not self.g:
            self.g = gitlab.Gitlab(GITLAB_URL, self.token)
            self.group = self.g.groups.get(GITLAB_GROUP_ID)

    def userid(self, user):
        return self.g.users.list(username=user)[0]

    def add(self, user):
        self.login()
        return self.group.members.create({
            'user_id': self.userid(user),
            'access_level': GITLAB_DEFAULT_LEVEL,
        })
