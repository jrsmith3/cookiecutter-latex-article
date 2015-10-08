from subprocess import call
call(["git", "init"])
call(["git", "add", "."])
call(["git", "commit", "-m", "\"cookiecut and initialize project.\""])
