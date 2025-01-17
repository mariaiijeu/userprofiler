# UserProfiler

UserProfiler is a Python program designed to create and manage user profiles with customizable settings for shared Windows computers. The tool allows you to easily handle user-specific settings and maintain them across sessions.

## Features

- **Create Profiles**: Create user profiles to store personalized settings.
- **Manage Settings**: Update and retrieve settings for each user.
- **Delete Profiles**: Remove user profiles when they are no longer needed.
- **Persistent Storage**: Profiles are saved in a JSON file for persistence.

## Installation

To run UserProfiler, you'll need to have Python installed. You can download Python from [python.org](https://www.python.org/).

Clone this repository or download the `user_profiler.py` file directly.

```bash
git clone https://github.com/yourusername/UserProfiler.git
cd UserProfiler
```

## Usage

Run the `user_profiler.py` script using Python:

```bash
python user_profiler.py
```

You can use the following methods to interact with user profiles:

- **Create a Profile**: `create_profile(username)`
- **Update User Setting**: `update_user_setting(username, key, value)`
- **Get User Setting**: `get_user_setting(username, key)`
- **Delete a Profile**: `delete_profile(username)`

### Example

```python
profiler = UserProfiler()

# Create a new user profile
profiler.create_profile("alice")

# Update a setting for the user
profiler.update_user_setting("alice", "theme", "dark")

# Retrieve a setting for the user
theme = profiler.get_user_setting("alice", "theme")
print(f"Alice's theme is set to: {theme}")

# Delete the user profile
profiler.delete_profile("alice")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.