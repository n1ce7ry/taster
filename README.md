# Taster
![Static Badge](https://img.shields.io/badge/python-3.10.8-green)
![Static Badge](https://img.shields.io/badge/django-5.0-blue)
<img alt="GitHub" src="https://img.shields.io/github/license/n1ce7ry/SyncPro">

## Table of Contents

- [Taster](#Taster)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## About

Taster is an innovative food delivery service focused on fast and convenient delivery of culinary masterpieces right to your door. Our platform combines cutting-edge technology and a personalized approach to each order, providing unmatched quality of service and satisfying the taste preferences of the most demanding customer. Join Taster to discover a world of exquisite flavors and fast delivery!

## Features

- Create profile and login.
- Manage news.
- Add food to cart, remove food from cart.
- Beautiful modal and pop-up windows.

## Getting Started

Follow these steps to get started with Travelers' Hub Forum:

1. Install poetry: 
```bash 
curl -sSL https://install.python-poetry.org | python3 -
```
2. Clone the project: 
```bash
git clone https://github.com/n1ce7ry/SyncPro`
```
3. Install the dependencies 
```bash
poetry shell
poetry install
```
4. Edit env.example, rename it to env.sh, and run it: 
```bash
vim env.example
mv env.example env.sh
. ./env.sh
```
5. Apply database migrations
```bash
python manage.py migrate
```
6. Create a superuser account: 
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

Once you start your local server, you can log in to it through your web browser. You don't have to create an account before you start shopping

## Contributing

We welcome contributions from the community! If you'd like to contribute to Travelers' Hub Forum, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and test them.
4. Commit your changes: `git commit -m "Add your brief commit message"`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Create a pull request to the `main` branch of this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
