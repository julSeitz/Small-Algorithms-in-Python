import subprocess

user_name = "foo"
user_password = "password1234!"

result = subprocess.run(["cat /etc/passwd | grep {0}".format(user_name)], shell=True, capture_output=True, text=True)
if len(result.stdout) != 0:
    print("User {0} already exists!".format(user_name))
    exit()

result = subprocess.run(["sudo useradd -m " + user_name], shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print("Created user " + user_name)
else:
    print("An error occured when trying to create user " + user_name)
    exit()

result = subprocess.run(["echo {0}:{1} | sudo chpasswd".format(user_name, user_password)], shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print("Set password for user " + user_name)
else:
    print("An error occured when trying to set password for user " + user_name)