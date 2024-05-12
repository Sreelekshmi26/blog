# Blog

This repository contains a Dockerized blog application that allows users to register, log in, and log out, create, edit, and delete their own blog posts, view all blog posts, search for posts by title or content, and interact with the application through RESTful APIs.

## Features

1. **User Authentication**: Users can register, log in, and log out securely.
2. **Blog Post Management**: Registered users can create, edit, and delete their own blog posts.
3. **Blog Post Details**: Each blog post includes a title, content, publication date, and author.
4. **Blog Post Listing**: Visitors can view all blog posts sorted by publication date, with pagination.
5. **Search Functionality**: Users can search for posts by title or content.
6. **RESTful APIs**: Exposes CRUD operations on blog posts with proper authentication mechanisms.

## Technologies Used

- Docker
- Python
- Django
- Django restframework
- Javascript

## Setup Instructions

To set up this project locally using Docker, follow these steps:

1. **Clone the repository**:
    ```shell
    git clone [repository-url]
    cd blog
    ```

2. **Build the Docker images**:
    ```shell
    docker-compose build
    ```

3. **Run the project**:
    ```shell
    docker-compose up
    ```
    
4. **API Documentation**:
    - You can use tools like Postman or CURL to test the API endpoints.

