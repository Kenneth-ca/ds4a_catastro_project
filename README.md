# Cadastral Appraiser - DS4A Project
Project about cadastral valuation of properties in Bogotá

## Project structure
    .
    └───flask_app
        ├───static
        │   ├───dist
        │   │   ├───css
        │   │   ├───fonts
        │   │   ├───img
        │   │   └───js
        │   └───src
        │       ├───js
        │       └───less
        └───templates

## Usage

1. Make sure to have the necessary packages
    ```
    $ pip install -r requirements.txt
    ```
   or via [Poetry](https://python-poetry.org/)
   ```
    $ poetry shell
    $ poetry update
    $ poetry run
    ```

2. Set your own environment configurations in the .env file

    * `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
    * `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
    * `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
    * `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.
    * `LESS_BIN`: Path to your local LESS installation via `which lessc` (optional for static assets).
    * `ASSETS_DEBUG`: Debug asset creation and bundling in `development` (optional).
    * `LESS_RUN_IN_DEBUG`: Debug LESS while in `development` (optional).
    * `COMPRESSOR_DEBUG`: Debug asset compression while in `development` (optional).

    Initially it is only necessary to have the `SQLALCHEMY_DATABASE_URI` configured
    with a string to connect with your local database.
    
    Never commit secrets saved in .env files to Github.

3. The `start.sh` file is ready to be executed to start the application
(you can modify it to setup the application as you want)
