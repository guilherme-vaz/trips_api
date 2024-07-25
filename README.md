
# Travel API

## Description

This is a travel management API developed in Python using Flask. It allows the creation and management of trips, participants, events/attractions, activities, and sending invitations via email. Participants can confirm their presence on trips through the API.

## Features

- **Trip Management**:
  - Create, find, and confirm trips.
  
- **Trip Participants**:
  - Add and list participants from a trip.
  - Send email invitations to participants.
  - Confirm participants' presence on a trip.
  
- **Trip Events/Attractions**:
  - Add, list, and remove events/attractions for the trip.
  
- **Trip Activities**:
  - Add, list, and remove activities for the trip.

## Technologies Used

- **Python**: Main programming language.
- **Flask**: Web framework used to build the API.
- **SMTP**: Protocol used for sending emails.
- **Virtual Environment**: Used to isolate project dependencies.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/repository-name.git
    cd repository-name
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies


## Endpoints

### Trips

- **GET /trips/:tripId**: Find a trip.
- **POST /trips**: Create a new trip.

### Participants

- **GET /trips/:tripId/participants**: Find a participant of a trip.
- **POST /trips/:tripId/invites**: Invite a new participant to the trip.
- **PATCH /participants/:participantId/confirm**: Confirm a participant's presence on the trip.

### Events/Attractions

- **GET /trips/:tripId/links**: List all links for events/attractions of a trip.
- **POST /trips/:tripId/links**: Create a new link for an event/attraction to the trip.


### Activities

- **GET /trips/:tripId/activities**: List all activities of a trip.
- **POST /trips/:tripId/activities**: Add a new activity to the trip.

## Contribution

1. Fork the project.
2. Create a new branch with your feature: `git checkout -b my-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin my-feature`
5. Submit a pull request.

---
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,flask,sqlite,git" />
  </a>
</p>
<p align="center">Made with ❤️ by Guilherme Vaz 👋🏽 Get in touch!</p>
<div align="center">

  [![Linkedin Badge](https://img.shields.io/badge/-Guilherme-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/guiilherme-vaz/)](https://www.linkedin.com/in/guiilherme-vaz/) 
  [![Gmail Badge](https://img.shields.io/badge/-guilhermeolivaaz@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:guilhermeolivaaz@gmail.com)](mailto:guilhermeolivaaz@gmail.com)

</div>
