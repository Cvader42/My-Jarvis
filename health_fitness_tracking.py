class ExerciseTracker:
    """
    A class to track exercise routines, suggest workouts, and provide health tips.
    """

    def __init__(self):
        """
        Initialize the exercise tracker.
        """
        self.routines = []

    def track_exercise_routine(self, exercise_type, duration):
        """
        Track an exercise routine.

        Args:
            exercise_type (str): The type of exercise.
            duration (int): The duration of the exercise in minutes.
        """
        self.routines.append({
            "exercise_type": exercise_type,
            "duration": duration
        })

    def suggest_workouts(self, workout_level):
        """
        Suggest workouts for a given workout level.

        Args:
            workout_level (str): The workout level.

        Returns:
            list: A list of suggested workouts.
        """
        if workout_level == "beginner":
            return ["30-minute brisk walk", "10-minute bodyweight exercises"]
        elif workout_level == "intermediate":
            return ["45-minute jog", "20-minute circuit training"]
        elif workout_level == "advanced":
            return ["60-minute HIIT session", "Weightlifting routine"]
        else:
            return []

    def provide_health_tips(self, health_topic):
        """
        Provide health tips for a given health topic.

        Args:
            health_topic (str): The health topic.

        Returns:
            str: A health tip.
        """
        if health_topic == "nutrition":
            return "Stay hydrated and include a variety of fruits and vegetables in your diet."
        elif health_topic == "sleep":
            return "Aim for 7-9 hours of quality sleep per night for optimal recovery."
        elif health_topic == "stress":
            return "Practice relaxation techniques such as deep breathing and meditation."
        else:
            return "I'm sorry, I don't have tips for that topic."
