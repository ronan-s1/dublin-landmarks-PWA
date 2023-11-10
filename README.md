# geodjango-landmark-app

VIEW: https://awm-ronan.site/ (username: "ronan", password: "password")

- This django application displays the users location and landmarks in dublin on a map using leaflet and openstreetmap. Users can choose their favourite landmark!
- It creates, store and manipulate spatial data in PostgreSQL/PostGIS database.
- It uses Boostrap for it's grid layout and visually appealing components. This makes the application responsive to make usuable it on different screen sizes.
- The app was deployed on an ubuntu VM on Azure using docker, nginx and has HTTPS with the help of certbot.

## View for grading
[VIDEO DEMO SHARED POINT](https://tudublin-my.sharepoint.com/:v:/g/personal/c20391216_mytudublin_ie/EcZOnU5-60xPvpsHTTyirbYBZI1sV_lJeLe2PeN4hOe3NQ)

that is for some reason quite bad quality so I uploaded it to youtube:
https://youtu.be/5YyVTnQEQRE

**Screenshot of app**

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/3540fe56-4e31-4e3a-b926-fcd92c61796a)


**Proof of a responsive app:**

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/2853f71d-97c5-416a-9b2e-6af7029d6020)

# setup

## create docker container for gis
```bash
docker create --name lab4_post_gis --network geojango_tutorial_network --network-alias lab4_post_gis -e POSTGRES_USER=docker -e POSTGRES_PASS=docker -t -p 25432:5432 -v name_of_volume:/var/lib/postgresql kartoza/postgis
```

## create docker container for django app
```bash
docker build -t geojango_tutorial .
```

```bash
docker create --name geojango_tutorial --network geojango_tutorial_network --network-alias geojango_tutorial -t -p 8001:8001 geojango_tutorial
```

## start containers
```bash
docker start geojango_tutorial
```

```bash
docker start lab4_post_gis
```

## Load landmark and migrations
```bash
docker exec geojango_tutorial bash -c "conda run -n geojango_tutorial python manage.py makemigrations"
```
```bash
docker exec geojango_tutorial bash -c "conda run -n geojango_tutorial python manage.py migrate"
```
```bash
docker exec geojango_tutorial bash -c "conda run -n geojango_tutorial python manage.py import_landmarks"
```

## Note the configuration script in `settings.py`

set `LOCAL_DOCKER_TEST = True` if running the docker containers locally

[script here](https://github.com/ronan-s1/geojango_tutorial/blob/main/geojango_tutorial/settings.py#L100C1-L129C1)
