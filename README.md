# react-flask-chat-room

## Flask

## Database
### Setup
1. Download and install [MAMP](https://www.mamp.info/en/)
2. Nevigate to [MAMP manage page](http://localhost:8888), > Tools > phpMyAdmin
3. Create a new data base named `rf_chat_room`
4. Find schema file in `/db/schema.sql`, and dump schema to `rf_chat_room`
5. Notice: you may need to change database connection in server.py based on your MAMP setup

## React

## Data Model
### User
User has a name and en email, a user also has multiple conversations and message
### Conversation
Conversation has many users and many messages
### Message
Message belongs to a single user and a single conversation
