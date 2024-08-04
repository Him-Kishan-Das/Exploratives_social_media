# Exploratives_social_media

# Exploratives A Social Media Website

A Django-based social media platform where users can create posts, like and comment on posts, view who has liked and commented, search for profiles, and navigate to user profiles. Users can also follow or unfollow others and see their followers and following lists.

## Features

- **Create Posts**: Users can create new posts.
- **Like Posts**: Users can like posts and see who has liked them.
- **Comment on Posts**: Users can comment on posts and see who has commented.
- **Profile Search**: Users can search for profiles using the search bar.
- **Profile Navigation**: Users can navigate to their own profile and other users' profiles.
- **Follow/Unfollow**: Users can follow or unfollow other users.
- **Followers/Following**: Users can see their followers and following lists by navigating to the user profile.

## Technologies Used

- **HTML5**
- **CSS**
- **JavaScript**
- **Django**
- **Django built-in libraries**
- **SQLite** (database)
- **FontAwesome** (icons)


## Cloning and Running the Project

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.x
- Git

### Steps

1. **Clone the repository**:
    Open your terminal or command prompt and run the following command:
    ```bash
    git clone https://github.com/yourusername/exploratives.git
    cd exploratives
    ```

2. **Create a virtual environment**:
    Create a virtual environment to manage dependencies:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**:
    Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**:
    Apply the database migrations to set up the database schema:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    Create a superuser account to access the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

1. **Create a Post**: Navigate to the home page and create a new post.
2. **Like a Post**: Click the like button on any post to like it.
3. **Comment on a Post**: Add a comment to any post.
4. **View Likes and Comments**: Click on the post to see who has liked and commented.
5. **Search Profiles**: Use the search bar to find other users' profiles.
6. **Navigate Profiles**: Click on a username to navigate to their profile.
7. **Follow/Unfollow Users**: Click the follow/unfollow button on a user's profile.
8. **View Followers/Following**: Navigate to a user's profile to see their followers and following lists.

## Contributors
We’d like to thank the following contributors for their valuable contributions:

1. Abinash Bordoloi - Helped in building the login system and solving initial issues

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
5. **Push to the branch**:
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Open a pull request**.

## License

This project is copyrighted by **Him Kishan Das**. All rights reserved.

## Acknowledgements

- Django Documentation
- FontAwesome for icons
- GPT-4 for generating dynamic content images
- Any other libraries or tools you used

---
