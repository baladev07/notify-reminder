# Django Email Scheduler
The Django Email Scheduler is a web application built using Django and Django REST framework that allows users to schedule an email to be sent at a specific date and time. It uses MySQL as its database.

# Installation
- Clone the repository to your local machine.
- Create a virtual environment using virtualenv.
- Activate the virtual environment.
- Create the database using python manage.py migrate.
- Start the development server using python manage.py runserver.


# Usage

Schedule an Email
To schedule an email, send a POST request to the /reminder endpoint with the following parameters:

```json
{
    "remindTo": "recipient@example.com",
    "reminderSub": "Subject of the email",
    "reminderBody": "Body of the email",
    "scheduled_time": "2023-04-20T12:00:00Z"
}
```
to: The email address of the recipient.
subject: The subject of the email.
body: The body of the email.
scheduled_time: The time at which the email should be sent. The format of the time should be in ISO 8601 format.
The response will contain the ID of the scheduled email.

```json
{
    "id": 1,
    "remindTo": "recipient@example.com",
    "reminderSub": "Subject of the email",
    "reminderBody": "Body of the email",
    "scheduled_time": "2023-04-20T12:00:00Z"
}
```
# Cancel a Scheduled Email
To cancel a scheduled email, send a DELETE request to the /reminder/{id}/ endpoint, where id is the ID of the email you want to cancel.

Contributions are welcome! If you find any bugs or want to suggest new features, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
