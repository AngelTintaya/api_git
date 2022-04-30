# api_git
This is a project to create a basic API REST

Preparing Environment:

1. Create a repo in GitHub.
2. Go to repo and copo the link to clone: [link_to_clone] (Click in code and copy the https link)
3. Open Terminal
4. Create file for Project: mkdir [project_name]
5. Enter to the Project file
6. Create a virtual env for project: python -m venv venv
7. Open Pycharm in current file: charm .
8. Set environment for Pycharm: Pycharm>Preferences>Project:[project_name]>PythonInterpreter>Add>Select venv (We just created)
9. Reopen project in Pycharm
10. In terminal, in file [project_name], clone the project from GitHub: git clone '[link_to_clone]' (This will copy the repo_name as a file)
11. Go to repo and name main branch to master: git branch -M master
12. Create the first temp file: Init.txt and make the first push git add . | git commit -m "message_to_commit" | git push origin master
13. In GitHub, create the Readme.md file
14. In Terminal, pull the changes: git pull origin master
15. Now we can go to Pycharm and enter inside [project_name] and start coding
16. Create development branch (git branch -b development) and working branch (git branch -b [working_branch] from development)
17. Create a version.txt and README.md

Running Flask
1. Go inside [project_name]
2. Be sure to be located in [working_branch]: git checkout [working_branch]
3. Install Flask: pip install Flask==2.1.2
4. Install Flask SQLAlchemy: Flask-SQLAlchemy==2.5.1
5. Create application.py: touch application.py
6. Work your code in application.py
7. Run our application:
   1. To do this, create environment variables: (WARNING!: WE NEED TO DO THIS ANYTIME WE OPEN THE TERMINAL)
      1. export FLASK_APP=application.py
      2. export FLASK_ENV=development
   2. Write: flask run
8. We can see where our flask is running in the link where says: "Running on [flask_link]"
9. Open the [flask_link] and see the response you wrote in application.py
10. We can create a get request by creating another function and routing it, then save it and it automatically will be updated in the link (We need to add the route to the link)

This information was created following the class:
https://www.youtube.com/watch?v=qbLc5a9jdXo
