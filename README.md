```
# File Management App

This is a simple web application built using Flask that allows you to upload files and list uploaded files along with their information.

## How to Launch the App

1. Install Docker on your system.
2. Clone this repository to your local machine.
3. Run the following command in the terminal. 

   ```
   $ ./launch_app.sh
   ```

5. Once the container is running, you can access the app in your browser at: http://127.0.0.1:5001

## Examples of Using curl

1. **Upload a File:**
   ```
   $ curl -X POST -F "file=@path/to/your/file" http://127.0.0.1:5001/v1/upload
   ```

2. **List Uploaded Files:**
   ```
   $ curl http://127.0.0.1:5001/v1/list_files
   ```

## Functionality

- **Upload Endpoint:** You can use the `/v1/upload` endpoint to upload files. The uploaded files are stored on the server and their information is recorded.

- **List Files Endpoint:** The `/v1/list_files` endpoint provides a list of all uploaded files along with their information.

## Technology Used

- **Flask:** Flask is a lightweight web framework used to build the web-server.
- **Docker:** The app is containerized using Docker for deployment.
- **HTML:** For simple Web UI

---

```
## Issues
Please open an issue on github.
