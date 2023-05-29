# eBay-like E-commerce Auction Site

This Django project is part of the CS50w, named "commerce," is an eBay-like e-commerce auction site that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a "watchlist." It has been developed as part of the CS50W "commerce" project.

## Features

- User registration and authentication: Users can create accounts, log in, and log out.
- Listing creation: Users can create new auction listings, providing information such as title, description, starting bid, and an optional image URL.
- Listing bidding: Users can place bids on active listings, with real-time validation of bid amounts.
- Listing commenting: Users can post comments on active listings, engaging in discussions with other users.
- Watchlist functionality: Users can add listings to their personal watchlist for easy access.
- Categories: Listings can be associated with specific categories, allowing users to filter and search for items in desired categories.
- Closed listings: Listings that have expired or have been closed by the creator are displayed separately.

## Installation

To run this project locally, please follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/commerce.git`
2. Navigate to the project directory: `cd commerce`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Install the project dependencies: `pip install -r requirements.txt`
6. Apply the database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

The project should now be running locally at `http://localhost:8000/`. Access it through your preferred web browser.

## Technologies Used

- Django: A high-level Python web framework for rapid development and clean design.
- HTML: Markup language for creating the structure and content of web pages.
- CSS: Stylesheet language for describing the presentation of web pages.
- JavaScript: Programming language for enhancing user interactions and adding dynamic functionality.
- SQLite: Embedded relational database management system.
