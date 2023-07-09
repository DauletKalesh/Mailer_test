# Mailer Test Problem

### Разработан через **DjangoRestFramework, PostgreSQL, RabbitMQ, Redis** 
![DjangoRestFramework Version](https://img.shields.io/badge/djangorestframework-3.0.0-orange)
![PostgreSQL Version](https://img.shields.io/badge/postgre-3.0.0-blue.svg)
![RabbitMQ Version](https://img.shields.io/badge/rabbitmq-3.0.0-green.svg)
![Redis Version](https://img.shields.io/badge/redis-3.0.0-red.svg)

## Project architecture
```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── email
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── repositories.py
│   │   └── email_sender.py
│   └── utils
│       ├── __init__.py
│       └── validation.py
├── test
│   ├── __init__.py
│   └── test_main.py
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── requirements.txt
```

## Запуск проекта
#### Clone the repository to your local machine:
>`git clone https://github.com/DauletKalesh/Mailer_test.git`

#### To run the project:

>`docker-compose up --build`

#### For questions and support, feel free to contact me: dauka_0202@mail.ru