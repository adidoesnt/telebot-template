# Telebot Template

## Overview

A simple template for creating Telegram bots using FastAPI and PyTelegramBotAPI.

## Getting Started

### Prerequisites

-   [Poetry](https://python-poetry.org/)
    -   **What is this?** Poetry is a tool for dependency management and packaging in Python.
    -   **Which version?** Poetry v2.0.1 or higher.
-   [Python](https://www.python.org/downloads/)
    -   **What is this?** Python is a programming language with a vast ecosystem of libraries and frameworks.
    -   **Which version?** Python 3.12 or higher.
-   [Docker](https://www.docker.com/)
    -   **What is this?** Docker is a platform for developing, shipping, and running applications.
    -   **Which version?** There is no specific version requirement, but it's best to keep things up-to-date.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/adidoesnt/telebot-template.git
```

2. Install the dependencies:

```bash
poetry install
```

3. Create a `.env` file in the root directory of the project:

```bash
cp .env.template .env
```

4. Fill in the required environment variables in the `.env` file:

```bash
# .env

# Environment
ENV=dev

# Server
HOST=127.0.0.1
PORT=8000
WEBHOOK_URL=<YOUR_WEBHOOK_URL> # This is only required for 'prod' environment

# Telegram
BOT_TOKEN=<YOUR_BOT_TOKEN>

# PostgreSQL/MySQL - Default is PostgreSQL
DB_NAME=test_db
DB_USER=test_user
DB_PASSWORD=test_password
DB_HOST=localhost
DB_HORT=5432

# SQLite
DB_PATH=path/to/db # This is only required for SQLite
```

5. *(Optional)* Try to build the Docker image, and then run it:  
   **Note:** The container will not be able to connect to the database unless you use [docker-compose](https://docs.docker.com/compose/).

```bash
docker build -t telebot-template:latest .
docker run -d -p 8000:8000 --name telebot-template telebot-template:latest
```

6. Start the bot:

```bash
poetry run start
```

7. Interact with the bot! The bot menu will guide you with using the available commands.

## Cloning the Repository

Please feel free to fork this repository and modify it to suit your needs. If you have any questions or need help, please don't hesitate to reach out.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
