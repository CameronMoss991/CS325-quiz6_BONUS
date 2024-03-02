from abc import ABC, abstractmethod

# Single Responsibility Principle (SRP):
# Each class has a single responsibility:
# - User: Shows a user of the fitness tracker.
# - Activity and its subclasses: Responsible for collecting data specific to each activity.
# - ActivityMonitor: Updates the display based on stored data and user activities.
# - DataStorage: Stores activity data.
# - Display: Updates the display with activity data.

# Open-Closed Principle (OCP):
# The ActivityMonitor class is open for extension but closed for modification.
# New activity types can be added by creating new subclasses of Activity without modifying existing classes.
# The ActivityMonitor class can handle new activity types by simply accepting instances of the new subclasses.

# Liskov Substitution Principle (LSP):
# The Activity class and its subclasses adhere to the observer pattern's contracts, making them compatible with the notification mechanism used in ActivityMonitor.
# Subclasses such as Walking and Running can be used interchangeably with the Activity class in the ActivityMonitor class without affecting the program's functionality.

# Interface Segregation Principle (ISP):
# The use of abstract base classes (ABC) helps to segregate interfaces. Each class defines its own interface through its methods, ensuring that users only need to know 
# about the methods relevant to them.

# Dependency Inversion Principle (DIP):
# Dependencies are injected into the ActivityMonitor class through its constructor, allowing for loose coupling.
# The ActivityMonitor class depends on abstractions (User, Display, DataStorage) rather than concrete implementations, making it easier to test and modify.
# This also allows for easy substitution of different implementations of User, Display, and DataStorage without changing the ActivityMonitor class.


class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

# Activity Class and Walking/Running are Subclasses
class Activity(ABC):
    @abstractmethod
    def collect_data(self):
        print("Activity Data Collected:")

class Walking(Activity):
    def collect_data(self):
        return {"type": "Walking", "steps": 5000, "distance_km": 4.0, "calories_burned": 200}

class Running(Activity):
    def collect_data(self):
        return {"type": "Running", "steps": 10000, "distance_km": 8.0, "calories_burned": 400}



class ActivityMonitor:
    def __init__(self, user, display, data_storage):
        self.user = user
        self.display = display
        self.data_storage = data_storage

    def monitor_activity(self, activity):
        data = activity.collect_data()
        self.data_storage.store_data(data)
        self.display.update(data)


class DataStorage:
    def store_data(self, data):
        print("Data stored:", data)

class Display:
    def update(self, data):
        print("Display updated with data:", data)

def main():
    user = User("Man Dummy", 30, 70)
    display = Display()
    data_storage = DataStorage()
    activity_monitor = ActivityMonitor(user, display, data_storage)

    walking_activity = Walking()
    activity_monitor.monitor_activity(walking_activity)

    running_activity = Running()
    activity_monitor.monitor_activity(running_activity)

if __name__ == "__main__":
    main()
