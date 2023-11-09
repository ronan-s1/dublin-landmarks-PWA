# geodjango-landmark-app
[VIDEO DEMO](https://tudublin-my.sharepoint.com/:v:/g/personal/c20391216_mytudublin_ie/Ef1k1o9EXYpMu0z3iQOhJlUBXnkwfNnOBAUU1ZZglN5azQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZyIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19&e=2pSMQx)

VIEW: https://awm-ronan.site/ (username: "ronan", password: "password")

NOTE: for some reason the markers don't show up on the map of the deployed cloud app, but they are there if you run locally. Regardless the app functions fine anyways.

Markers showing locally:
![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/7c625d6e-4776-4aa5-bd8d-feae5ba7be40)


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
