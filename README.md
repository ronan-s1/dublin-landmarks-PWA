# geodjango-landmark-app
advanced web mapping first assignment

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
