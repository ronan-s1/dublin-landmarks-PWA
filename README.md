# Dublin Landmarks Django PWA

VIEW: https://awm-ronan.site/ (username: "ronan", password: "password")

- This Django PWA displays the user's location along with landmarks in Dublin on a map using leaflet and openstreetmap.
- The application was deployed on Azure using Docker containers, Nginx and TSL wash achieved using Certbot.
- Boostrap was employed to make the UI applealing and responsive.
- The application is confirmed as a Progressive Web App (PWA) through Google Lighthouse validation.

## Features
- Choose a landmark from the dropdown to set it as your favorite.
  - The map automatically zooms in to the selected landmark.
- Click on a landmark marker on the map to update the dropdown selection.
- Easily add a new landmark to the map.
- Colour-coded markers distinguish landmarks based on different categories.
- Find the nearest landmark to your current location.
- Enjoy an intuitive and visually appealing user interface for a seamless experience.

## Screenshot of app

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/fa5fb0e3-78d9-4e06-bc8a-4b77b2acc1c2)

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/71f62e05-f339-4769-b3b9-c36219d6d943)


# Setup

## Create GIS container
```bash
docker create --name lab4_post_gis --network geojango_tutorial_network --network-alias lab4_post_gis -e POSTGRES_USER=docker -e POSTGRES_PASS=docker -t -p 25432:5432 -v name_of_volume:/var/lib/postgresql kartoza/postgis
```

## Create app container
```bash
docker build -t geojango_tutorial .
```

```bash
docker create --name geojango_tutorial --network geojango_tutorial_network --network-alias geojango_tutorial -t -p 8001:8001 geojango_tutorial
```

## Start containers
```bash
docker start geojango_tutorial
```

```bash
docker start lab4_post_gis
```

## Load landmarks and migrate model
```bash
docker exec geojango_tutorial bash -c "conda run -n geojango_tutorial python manage.py migrate"
```
```bash
docker exec geojango_tutorial bash -c "conda run -n geojango_tutorial python manage.py import_landmarks"
```

## Note the configuration script in `settings.py`

set `LOCAL_DOCKER_TEST = True` if running the docker containers locally

[script here](https://github.com/ronan-s1/geojango_tutorial/blob/main/geojango_tutorial/settings.py#L100C1-L129C1)
