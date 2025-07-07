# Flask Task Manager API

## Overview
This project is a modular Flask-based API for managing tasks, users, organizations, and organization members. It supports both personal and organization-based task management, with JWT authentication and role-based access control.

## Project Structure

- `app.py` — Main Flask application entry point.
- `config.py` — Configuration settings for the Flask app.
- `extensions/` — App extensions (e.g., database, JWT setup).
- `models/` — Data models for Users, Tasks, Organizations, and Organization Members.
- `repositories/` — Data access layer for CRUD operations on models.
- `service/` — Business logic and use case implementations.
- `controllers/` — HTTP request handlers (Flask views/controllers).
- `routes/` — Route definitions for the API endpoints.
- `serializers/` — Serialization/deserialization logic for models.
- `enums/` — Enumerations for statuses and roles.
- `utils/` — Utility functions (e.g., date/time helpers).

## Main Features & Use Cases

### User
- Register, login, logout (JWT-based)
- [TODO] Update profile, change password, reset password, view profile

### Task
- Create, view, update, delete personal tasks
- Change task status, filter by status
- [TODO] Assign tasks, add comments/attachments, set due dates/priorities, search tasks

### Organization
- Create, edit, view, delete organizations
- [TODO] List/search organizations, update organization settings, audit/history

### Organization Member
- Add member, join organization, view members
- [TODO] Remove member, update member role, deactivate/reactivate member, view member details, list user organizations

### Organization Task
- Create, view, update, delete organization tasks
- Assign tasks to members, update status, view member tasks

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment variables as needed (see `config.py`).
3. Run the app: `python app.py`

## Extending the API
- Add new use cases in the `service/` layer.
- Expose new endpoints in the `controllers/` and `routes/` layers.
- Update `serializers/` for new data formats.

## Notes
- Ensure to implement missing use cases (marked as [TODO]) for a complete system.
- The codebase is modular and follows separation of concerns for maintainability.

---

For further details, review the code in each module and follow the structure for adding new features or endpoints.