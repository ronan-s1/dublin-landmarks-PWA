# Dublin Landmarks Django PWA

**[DEMO VIDEO](https://youtu.be/k-tA-KK7D_s?si=NUtwOd7V0VbZkv74)**

VIEW: https://awm-ronan.site/ (username: "ronan", password: "password")

<hr>

- This Django PWA displays the user's location along with landmarks in Dublin on a map using leaflet and openstreetmap.
- The application was deployed on Azure using Docker containers, Nginx and TSL was achieved using Certbot.
- Boostrap was employed to make the UI applealing and responsive.
- The Beautiful Soup package was utilised to scrape the weather data and parse the HTML.
- The different layers on the map was built using CartoDB
- The application is confirmed as a Progressive Web App (PWA) through Google Lighthouse validation.

## Features
- Choose a landmark from the dropdown to set it as your favorite.
  - The map automatically zooms in to the selected landmark.
- Click on a landmark marker on the map to update the dropdown selection.
- Easily add a new landmark to the map.
- Distinguish landmarks on the map based on category colour.
- Search different locations on the map.
- Choose different map layers to your liking.
- Find the nearest landmark to your current location.
- See the current weather in Dublin.
- Enjoy an intuitive and visually appealing user interface for a seamless experience.

## Screenshot of app

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/8eaea295-8727-4da6-a5a2-f36e0c49a6c7)

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/71f62e05-f339-4769-b3b9-c36219d6d943)

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/4d9cb174-fa6a-43b1-94d5-a3ad07ed5677)

![image](https://github.com/ronan-s1/geojango_tutorial/assets/85257187/403bb1fb-d0fa-4517-b330-39244a782387)


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
