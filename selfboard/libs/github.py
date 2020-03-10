# https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html#github.Organization.Organization.invite_user
from github import Github

class GitHub:
    def __init__(self, token):
        self.token = token
        self.g = False

    def login(self):
        if not self.g:
            self.g = Github(self.token)

    def add(self, user):
        self.login()
        return [self.g.Organization.Organization.invite_user(user)]

    def remove(self, user):
        self.login()
        ret = []
        ret.append(self.g.Organization.Organization.remove_from_membership(user))
        ret.append(self.g.Organization.Organization.remove_from_members(user))
        return ret
