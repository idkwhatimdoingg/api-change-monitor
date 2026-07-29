# API Change Monitor

A modular Python monitoring tool that tracks changes in external API data and detects newly added or removed items.

The application periodically fetches data from an API provider, compares it against previously stored state, and identifies changes. The project uses a provider-based architecture, making it easy to add new monitoring sources without changing the core logic.

## Features

- Fetches data from external APIs
- Detects added and removed entities
- Stores previous state locally using JSON
- Modular provider architecture
- Reusable comparison system
- Extensible notification system
- Designed to support multiple monitoring sources

## Current Provider

### GitHub Release Monitor

The current implementation monitors GitHub repository releases.

Example:

```
Repository:
pallets/flask

New release detected:
Flask 3.1.0

Release URL:
https://github.com/pallets/flask/releases
```

The monitor checks the repository's release data, compares it with previously saved information, and detects newly published releases.

## How It Works

The application follows this workflow:

```
External API
      |
      v
Provider
      |
      v
Current Data
      |
      v
Comparator
      |
      v
Change Detection
      |
      v
State Storage
      |
      v
Notifications
```

Each component has a separate responsibility:

- **Providers** handle fetching data from external services.
- **Comparator** detects changes between old and new data.
- **Storage** saves previous states so changes can be detected across restarts.
- **Notifications** handle sending alerts.

This design allows additional monitoring sources to be added without modifying the core application.

## Project Structure

```
api-change-monitor/
│
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── README.md
├── .gitignore
│
├── Providers/
│   ├── __init__.py
│   ├── base.py                 # Provider interface
│   └── github.py               # GitHub release provider
│
├── notifications/
│   ├── __init__.py
│   └── discord.py              # Discord notification handler
│
├── storage/
│   ├── __init__.py
│   └── json_storage.py         # Local JSON state storage
│
├── utils/
│   ├── __init__.py
│   └── comparator.py            # Change comparison logic
│
└── data/
    └── .gitkeep                # Runtime storage directory
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project folder:

```bash
cd api-change-monitor
```

Install required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

On the first run, the application creates a baseline of the current API state.

On future runs, it compares the latest data against the previously stored state and reports any changes.

## Example Output

```
Requesting:
https://api.github.com/repos/pallets/flask/releases

Status code:
200

Number of releases found:
30

Changes:

{
    'added': {
        123456789
    },
    'removed': set()
}
```

## Adding New Providers

The provider system is designed to be extended.

A new provider only needs to implement the provider interface:

```python
class ExampleProvider(Provider):

    def get_state(self):
        # Fetch external data
        # Return structured state
        pass
```

The existing comparison and storage systems can then be reused automatically.

Possible future providers:

- Website change monitor
- Product price tracker
- GitHub issue tracker
- Social media metrics monitor
- Software update tracker

## Technologies Used

- Python
- Requests
- REST APIs
- JSON data storage
- Object-oriented design


## License

This project is available for educational and portfolio purposes.