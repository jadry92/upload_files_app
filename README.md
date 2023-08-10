# Upload App Files

This is a simple app to upload files to a server. It is built with Django using the Model View Controller (MVC) design pattern. The app is containerized using Docker and can be deployed locally or to a production server.

This app doesn't have user management. It is assumed that the user is already authenticated and authorized to upload files to the server. And it not using the Admin interface.

## Example

The home page has a form where the images are supply and a table to display the files that have been uploaded. The only allow file types are (txt, pdf and docx) and the maximum file size is 5MB.

![img1][image_1]

## Requirements

To run this app you will need the following:

- Docker

## Installation

### Local

```bash
docker-compose -f local.yml build
docker-compose -f local.yml django python manage.py migrate
docker-compose -f local.yml up -d
```

### Production

```bash
docker-compose -f production.yml build
docker-compose -f production.yml django python manage.py migrate
docker-compose -f production.yml up -d
```

[image_1]: ./static/images/example_1.png "Home Page"
