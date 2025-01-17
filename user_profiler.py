import json
import os

class UserProfile:
    def __init__(self, username, settings=None):
        self.username = username
        self.settings = settings if settings is not None else {}

    def update_setting(self, key, value):
        self.settings[key] = value
        print(f"Setting '{key}' updated to '{value}' for user '{self.username}'.")

    def get_setting(self, key):
        return self.settings.get(key, None)

    def __repr__(self):
        return f"UserProfile(username={self.username}, settings={self.settings})"

class UserProfiler:
    def __init__(self, profiles_file='user_profiles.json'):
        self.profiles_file = profiles_file
        self.profiles = self.load_profiles()

    def load_profiles(self):
        if os.path.exists(self.profiles_file):
            with open(self.profiles_file, 'r') as file:
                return json.load(file)
        return {}

    def save_profiles(self):
        with open(self.profiles_file, 'w') as file:
            json.dump(self.profiles, file, indent=4)
        print("Profiles saved successfully.")

    def create_profile(self, username):
        if username in self.profiles:
            print(f"Profile for '{username}' already exists.")
            return

        self.profiles[username] = UserProfile(username).__dict__
        self.save_profiles()
        print(f"Profile created for user '{username}'.")

    def delete_profile(self, username):
        if username not in self.profiles:
            print(f"No profile found for user '{username}'.")
            return

        del self.profiles[username]
        self.save_profiles()
        print(f"Profile for user '{username}' deleted.")

    def update_user_setting(self, username, key, value):
        if username not in self.profiles:
            print(f"No profile found for user '{username}'.")
            return

        user_profile = UserProfile(**self.profiles[username])
        user_profile.update_setting(key, value)
        self.profiles[username] = user_profile.__dict__
        self.save_profiles()

    def get_user_setting(self, username, key):
        if username not in self.profiles:
            print(f"No profile found for user '{username}'.")
            return None

        user_profile = UserProfile(**self.profiles[username])
        return user_profile.get_setting(key)


if __name__ == "__main__":
    profiler = UserProfiler()

    # Example usage
    profiler.create_profile("alice")
    profiler.update_user_setting("alice", "theme", "dark")
    print(profiler.get_user_setting("alice", "theme"))
    profiler.delete_profile("alice")