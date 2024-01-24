# Python File Upload Service

## Overview

This Python web service allows users to upload files through a web interface or via an API. Each file is stored with a
unique identifier and can be accessed through a generated URL. The service uses Flask for the backend and provides a
simple, responsive web interface for file uploads.

## Features

- File upload through a web interface and API.
- Drag-and-drop functionality on the web interface.
- API Key based authentication for uploads.
- Unique URLs for each uploaded file.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone this repository or download the source code.
2. Install the required Python dependencies:

   ```sh
   poetry install
   ```

3. Run the application:

   ```sh
   poetry run flask run
   ```

## Usage

### Web Interface

- Navigate to `http://localhost:5000/` in your web browser.
- Enter your API Key.
- Drag and drop a file into the designated area or click to select a file.
- The file will be uploaded, and a unique URL will be provided.

### API Usage

- Send a POST request to `http://localhost:5000/upload` with the `file` and `api_key`.
- The response will include the unique URL for the uploaded file.

## API Key Generation

- Run the API key generation script:

  ```sh
  python generate_api_key.py
  ```

- Use the generated API key for file uploads.

## Security

- Ensure to keep the API keys secure.
- Only share API keys with trusted users.

## License

[LGPL 3.0](LICENSE)
