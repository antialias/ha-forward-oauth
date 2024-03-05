# ForwardAuth Service for Home Assistant

This ForwardAuth service is designed to work with Traefik as a middleware to authenticate requests against Home Assistant's OAuth2 API before allowing access to specific services, such as Music Assistant. It leverages Home Assistant's OAuth2 and IndieAuth to securely manage authentication.

## Features

- ForwardAuth authentication with Home Assistant
- OAuth2 flow for securing internal services
- Easy integration with Traefik

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a Home Assistant instance running and accessible.
- You have Traefik set up as your reverse proxy.
- You have Python 3.6+ installed on your system.

## Installation

To install the ForwardAuth service, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/yourgithub/forward_auth_service.git
   ```

2. Navigate to the project directory:

   ```sh
   cd forward_auth_service
   ```

3. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Copy the `.env.example` to `.env` and update it with your configuration details:

   ```sh
   cp .env.example .env
   ```

5. Run the service:

   ```sh
   python -m flask run --port=5000
   ```

## Configuration

After cloning the project and before running the service, you need to configure it by setting the following environment variables in the `.env` file:

- `HOME_ASSISTANT_URL`: The URL of your Home Assistant instance.
- `CLIENT_ID`: The client ID registered with Home Assistant for OAuth2 flow.
- `REDIRECT_URI`: The redirect URI set for the OAuth2 flow.

## Usage

Once the ForwardAuth service is running, configure Traefik to use this service as a ForwardAuth middleware for your protected services. Here is an example Traefik dynamic configuration:

```toml
[http.middlewares]
  [http.middlewares.auth-forward.forwardAuth]
    address = "http://localhost:5000/auth"
    trustForwardHeader = true
```

## Contributing to ForwardAuth Service

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contact

If you want to contact me, you can reach me at `your_email@example.com`.

## License

This project uses the following license: [MIT](<link-to-license>).
