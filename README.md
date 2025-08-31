# Core Project

This repository is a monorepo that contains shared components for the Django microservices project. It is designed to be installed as a package in other Django projects.

## Components

The `core_project` consists of three main Python packages:

1.  **`shared_models`**: Contains shared Django models that are used across multiple services.
    *   `models.py`: Defines `TimeStampedModel`, `User`, and `Product`.
    *   `setup.py`: Package definition and dependencies (Django).

2.  **`shared_utils`**: Contains common utility functions that are not specific to Django.
    *   `health.py`: A simple `get_health` function for health checks.
    *   `logger.py`: Basic logging configuration.
    *   `aws.py`: Placeholder for AWS-related utilities.
    *   `setup.py`: Package definition and dependencies (boto3, requests).

3.  **`django_core`**: Contains core Django components, such as base settings and views.
    *   `settings.py`: Common Django settings.
    *   `views.py`: A `health_check` view that uses the utility from `shared_utils`.
    *   `urls.py`: URL patterns for the core views.
    *   `setup.py`: Package definition and dependencies.

## How to Extend

To maintain a clean and decoupled architecture, follow these guidelines when extending the core project.

### Adding a New Shared Model

1.  Open `shared_models/shared_models/models.py`.
2.  Define your new model class. It's recommended to inherit from `TimeStampedModel` to get `created_at` and `updated_at` fields automatically.
3.  **Crucially**, add `app_label = 'shared_models'` within the model's `Meta` class. This ensures that Django associates the model with the correct application.
4.  Database migrations for shared models are **not** generated or stored in this repository. They are handled by the consumer microservices (`app1`, `app2`, etc.) that use them.

### Adding a New Shared Utility

1.  Create a new Python file in the `shared_utils/shared_utils/` directory (e.g., `my_new_util.py`).
2.  Add your functions or classes to this new file.
3.  If your new utility requires additional third-party packages, add them to the `install_requires` list in `shared_utils/setup.py`.

### Using Core Components

These packages can be installed in two ways:

1.  **From a Git repository (Production):**
    You can install them directly from a Git repository in your `requirements.txt`.
    ```
    shared-models @ git+ssh://git@github.com/your_org/core_project.git@main#subdirectory=shared_models
    ```

2.  **From a local directory (Development):**
    For local development, you can install them using a relative path with the `-e` (editable) flag.
    ```
    -e ../core_project/shared_models
    ```