<div align="center">

# Fampay-Assignment

![Size](https://github-size-badge.herokuapp.com/Saurav-Shrivastav/Fampay-Assignment.svg)
[![License](https://img.shields.io/github/license/Saurav-Shrivastav/Fampay-Assignment)](https://github.com/Saurav-Shrivastav/Fampay-Assignment/blob/main/LICENSE)
![GitHub contributors](https://img.shields.io/github/contributors/Saurav-Shrivastav/Fampay-Assignment?logo=github)

</div>

# Main Features
1. Server calls the YouTube API continuously in background (async) with 30 seconds interval for fetching the latest videos for a predefined search query (the query 
currently used is "fampay", it can be modified in `app/app/tasks.py`) and stores the data of videos in a database.
2. A API which returns the stored video data in a paginated response sorted in descending order of published datetime. Also allows searching by `title`, filtering and ordering.
3. Support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
4. The project is scalable and optimised. For deployment, just need to build and push the containers.

# Technology Stack
<table>
  <thead align="center">
    <tr>
      <td><strong>Technology</strong></td>
      <td><strong>Use</strong></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Django / Django REST Framework</td>
      <td>API</td>
    </tr>
    <tr>
      <td>Docker and docker-compose</td>
      <td>Containerization</td>
    </tr>
    <tr>
      <td>Celery</td>
      <td>Asynchronous Task Queue</td>
    </tr>
    <tr>
      <td>Celery Beat</td>
      <td>Scheduler</td>
    </tr>
    <tr>
      <td>Redis</td>
      <td>Messaging Broker</td>
    </tr>
    <tr>
      <td>PostgreSQL</td>
      <td>Database</td>
    </tr>
    <tr>
      <td>NGINX</td>
      <td>Reverse Proxy</td>
    </tr>
    <tr>
      <td>Git</td>
      <td>Version Control</td>
    </tr>
    <tr>
      <td>GitHub</td>
      <td>Remote Code Hosting</td>
    </tr>
  </tbody>

</table>

# Class Diagram
![Class Diagram](/assets/class-diagram.png)

# Set Up Project

## Requirements to run the project
- Docker and docker-compose

## Steps
- Clone the repository:
```
git clone git@github.com:Saurav-Shrivastav/Fampay-Assignment.git
```
- Create 2 files named `.env` and `.db.env` in the root of the project. 
- Copy the contents of the file from `.env.example` to `.db.example` and from `.db.env.example` to `.db.env`. 
Update `YOUTUBE_API_KEY` variable in your `.env` file with a newly generated API key. You can know more about generating an API key <a href="https://blog.hubspot.com/website/how-to-get-youtube-api-key">here</a>.
- You can also update `DEBUG` if you wish to run the application without the DEBUG settings.
- Start the containers:
```
docker-compose up -d --build
```
- Run migrations:
```
docker-compose exec web python manage.py migrate --noinput
```
- Collect static files:
```
docker-compose exec web python manage.py collectstatic --noinput --clear
```
- Create a superuser:
```
docker-compose exec web python manage.py createsuperuser
```
You can now access the docs at <a href="http://localhost:1337/docs">localhost:1337/docs</a>

# System Architecture
![System Architecture](/assets/sys-architecture.png)

# API Endpoints
The **Swagger Documentation** is available at <a href="https://localhost:1337/docs">`/docs/`</a> <br>
The **OpenAPI Specification** is available at <a href="https://localhost:1337/openapi">`/openapi/`</a>

- `/api/videos/`: Get and list videos. Sample Reponse:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "title": "string",
      "publishing_date": "2021-12-19T14:23:49.308Z",
      "thumbnail_url": "string",
      "url": "string",
      "live_broadcast": "upcoming"
    }
  ]
}
```
- `/api/videos/{id}/`: Get video details by id. Sample Response:
```json
{
  "title": "string",
  "description": "string",
  "publishing_date": "2021-12-19T14:25:59.568Z",
  "thumbnail_url": "string",
  "url": "string",
  "live_broadcast": "upcoming",
  "channel": {
    "id": 0,
    "channel_url": "string",
    "channel_id": "string",
    "channel_title": "string"
  }
}
```

# License

See [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
