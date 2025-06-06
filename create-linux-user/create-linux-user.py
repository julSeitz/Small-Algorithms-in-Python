import subprocess

def create_user(name, password):
    """Creates a user with the given name and password if it does not exist yet."""
    result = subprocess.run(["cat /etc/passwd | grep {0}".format(name)], shell=True, capture_output=True, text=True)
    if len(result.stdout) != 0:
        print("User {0} already exists!".format(name))
        return

    result = subprocess.run(["sudo useradd -m " + name], shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Created user " + name)
    else:
        print("An error occured when trying to create user " + name)
        return

    result = subprocess.run(["echo {0}:{1} | sudo chpasswd".format(name, password)], shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Set password for user " + name)
    else:
        print("An error occured when trying to set password for user " + name)

user_name = "foo"
user_password = "password1234!"

create_user(user_name, user_password)