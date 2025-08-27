# Custom Admin App

A custom admin interface for the Peach Clone application that provides a more user-friendly and feature-rich alternative to the default Django admin.

## Features

- Custom dashboard with key metrics, visualizations, and recent activity
- CRUD operations for all major models (Companies, Items, Invoices, etc.)
- User management with custom permissions
- Activity logging for audit trails
- Customizable UI preferences (theme, sidebar, pagination)
- Responsive design with Bootstrap and Font Awesome
- Light/dark theme toggle
- Collapsible sidebar
- Interactive charts and statistics
- Filterable transaction views
- Date range selection for dashboard data

## Installation

The app is automatically installed as part of the main application. Make sure it's included in your `INSTALLED_APPS` setting:

```python
LOCAL_APPS = [
    # other apps...
    'src.custom_admin',
]
```

## URL Configuration

The custom admin is available at `/custom-admin/` by default. This can be changed in the settings.

## Initial Setup

To create an initial admin user, run:

```bash
python manage.py setup_admin --email=admin@example.com --password=securepassword --name="Admin User"
```

Or simply run:

```bash
python manage.py setup_admin
```

And follow the prompts to enter the admin details.

## Settings

The following settings can be configured in `settings/components/custom_admin.py`:

- `CUSTOM_ADMIN_SITE_HEADER`: The site header displayed in the admin interface
- `CUSTOM_ADMIN_SITE_TITLE`: The site title displayed in the browser tab

## Testing

### Automated Testing

Run the Django test suite:

```bash
python manage.py test src.custom_admin.tests
```

### UI Testing

To run the UI tests with Selenium:

1. Install the required packages:
   ```bash
   pip install -r src/custom_admin/test_requirements.txt
   ```

2. Make sure the Django server is running:
   ```bash
   python manage.py runserver
   ```

3. Run the UI test script:
   ```bash
   python src/custom_admin/test_ui.py
   ```

### Manual Testing

Refer to the `TESTING.md` file for a comprehensive manual testing guide.

## Additional Settings

- `CUSTOM_ADMIN_INDEX_TITLE`: The title displayed on the admin index page
- `CUSTOM_ADMIN_PERMISSION_REQUIRED`: Whether admin permissions are required to access the admin interface
- `CUSTOM_ADMIN_ITEMS_PER_PAGE`: Default number of items to display per page in list views

## Templates

The custom admin uses the following template structure:

- `base.html`: Base template with common layout elements
- `login.html`: Login page template
- `dashboard.html`: Dashboard template with metrics and activity
- Model-specific templates:
  - `list.html`: List view for model instances
  - `form.html`: Form for creating/editing model instances
  - `confirm_delete.html`: Confirmation page for deleting instances

## Activity Logging

All admin actions are automatically logged using the `AdminActivityMiddleware`. This includes:

- Page views
- Create operations
- Update operations
- Delete operations

The activity log can be viewed at `/custom-admin/activity-log/`.

## User Preferences

Users can customize their admin experience with the following preferences:

- Theme (light/dark)
- Sidebar collapsed state
- Items per page

These preferences are stored in the `AdminPreference` model and are automatically created for each admin user.