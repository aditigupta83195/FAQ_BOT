FAQ CHATBOT

PROBLEM STATEMENT

Modern websites often receive repetitive customer queries related to orders, payments, returns, account issues, and general support. Handling these manually increases support workload and delays response time. Traditional keyword-based chatbots fail to understand variations in user phrasing, leading to inaccurate or irrelevant answers.

This project aims to develop an intelligent FAQ chatbot that uses semantic search to understand the meaning of user questions and deliver the most appropriate responses from a predefined FAQ dataset.

 SCOPE OF THE PROJECT

The scope of this project includes:

Developing a web-based chatbot interface for interaction.

Implementing a Flask-based backend capable of processing user queries.

Using sentence embeddings for meaning-based similarity detection.

Delivering accurate FAQ answers and fallback responses when no match is found.

Handling casual small-talk for better user engagement.

Ensuring the system works efficiently without external APIs.

Out of scope:

Live customer support integration

User login or authentication

Database storage

Voice input or real-time chat support

 TARGET USERS

The primary users of this system are:

E-commerce customers seeking quick answers to common questions

Website visitors needing instant support

Businesses wanting to automate FAQ handling

Students or developers studying chatbot and NLP concepts

 HIGH-LEVEL FEATURES

Semantic FAQ Matching: Identifies the closest FAQ using sentence embeddings.

Smalltalk Support: Replies to greetings, thanks, and common conversational inputs.

Intuitive Chat UI: Smooth frontend interface for easy interaction.

Lightweight Architecture: Uses local embeddings without external APIs.

Fallback Response System: Handles unmatched queries gracefully.

Modular Code Design: FAQ data, embeddings, NLP logic, and UI kept separate.
