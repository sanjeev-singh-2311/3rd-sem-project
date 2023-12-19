# Project Documentation

- **User Authentication**
- **Startup Owner Side**
- **Investor Side**

---

## User Authentication

The user authentication application consists of one database model: _User Data_.

The _User Data_ model is stored in the form of a SQLite table with four main fields:
- Username
- User-Email
- User Type (TODO)
- Password

Username and Email are stored as normal text, while the User Password is stored as a simple string. The Password is hashed for privacy reasons. The Username serves as the table's _Primary Key_, allowing it to be used for data querying and as a _Foreign Key_ for the tables in the next apps.

The User Authentication app has two templates that translate into _Django Views_ to be shown over the web browser: the Login and Registration pages. When a user enters data in the form within these views, the info is sent to the backend via the POST method and then validated and saved within the User Data model. Users can configure their account as per their requirements with topic tags.

---

## Startup Owner and Investor Side (TODO)

Both these apps are mostly common, with the only difference being a different profile displayed whenever their profile is opened.

Both apps consist of two database models: _User Profile_ and _UserProjects_ / _UserInvestments_.

The _UserProfile_ model consists of these fields:
- Username (serving as a _Foreign key_ from the UserData table)
- ProjectID (StartUp Owner side) / InvestmentPortfolioID (Investor side)

The ProjectID / InvestmentPortfolioID themselves act as a _Primary Key_ to the UserProfile model and a _Foreign Key_ to UserProjects / UserInvestments model.

The UserProjects / UserInvestment tables at last consist of all the attachments and information that the user wishes to present on their profile.

---

## Ending Statement

Hence, the two foreign keys allow for easy access between the three tables on both the apps and the Authentication app. Just knowing the UserName, a query can be passed to fetch anything from the other tables.
