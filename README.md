# Spy Cat Agency API

Welcome to the Spy Cat Agency API! This application allows for managing missions and spy cats, including creating, updating, and deleting records. 

## Table of Contents

- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Postman Collection](#postman-collection)
- [Contributing](#contributing)

## Technologies Used

- Django 4.2.16
- Django REST Framework
- SQLite (or your preferred database)
- Postman for API testing

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Taldariner/spy_cat_agency.git
cd spy-cat-agency
```

### Step 2: Set Up a Virtual Environment

```bash
python -m venv __venv__
source __venv__/bin/activate  # On Windows use '__venv__\Scripts\activate'
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Migration

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)

To create an admin user for accessing the admin panel:

```bash
python manage.py createsuperuser
```

### Step 6: Start the Development Server

Run the following command to start the server:

```bash
python manage.py runserver
```

## API Endpoints

### Spy Cats Endpoints

* List Spy Cats

	* GET `/cats/`

* Create Spy Cat

	* POST `/cats/create`

* Retrieve Spy Cat

	* GET `/cats/{id}/`

* Update Spy Cat Salary

	* PATCH `/cats/{id}/update_salary`

* Delete Spy Cat

	* DELETE `/cats/{id}/delete`


### Missions Endpoints

* List Missions

	* GET `/missions/`

* Create Mission

	* POST `/missions/create`

* Retrieve Mission

	* GET `/missions/{id}/`

* Update Mission Targets

	* PATCH `/missions/{id}/update_targets`

* Delete Mission

	* DELETE `/missions/{id}/delete`

* Assign Cat to Mission

	* POST `/missions/{mission_id}/assign_cat/{cat_id}/`

## Postman Collection

To help you test the API, you can import the Postman collection available at the following link:

[Download Postman Collection](https://api.postman.com/collections/39310750-975f08bb-4c1d-434e-9b6d-2fa17f239001?access_key=PMAT-01JB6S8CZKZQNBGK9VZRYWEPJ4)

## Contributing

Feel free to submit issues, suggestions, or pull requests to help improve this project!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Thank you for checking out the Spy Cat Agency API! Happy coding!
