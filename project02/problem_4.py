#!/usr/bin/env python3-


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.grand = []

    def add_group(self, group):

        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"Group: {self.name}"


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    elif not group.get_groups():
        return False
    else:
        for sub in group.get_groups():
            if is_user_in_group(user, sub):
                return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_c_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)


print("Testcases:")
print(is_user_in_group("p", parent))
# False
print(is_user_in_group("sub_c_user", parent))
# True
print(is_user_in_group("", parent))
# False
print(is_user_in_group("", child))
# False
