## TLDR; how to run
- Clone/unzip repo.
- Run the command `docker-compose up -d`
- Open browser and open `http://localhost:8000/admin/djangoapp/companies/`
- Use default username and password of `admin` and `admin`


### Some additional Details
- Build using Python, Django, PostgreSQL and docker.
- Docker spins up 2 containers - 1 app server and 1 db server.
- Docker compose up takes care of running migrations to create the models, creating first superuser admin and starting the server.
- Used django admin with customised list and filters to achieve the task.
- Have used a management command that runs at start to load csv data to a DB and create the first superuser.
- Have diabled add, edit and delete from django admin interface to be inline with the requirement of only list and fitlers.
