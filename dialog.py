class DialogManager:
    def __init__(self):
        self.context = {}  # Store conversation context

    def start_dialog(self):
        self.context.clear()  # Clear context at the start of a new dialog
        self.context["user_name"] = None
        self.context["user_intent"] = None

    def update_context(self, user_input, intent):
        self.context["user_input"] = user_input
        self.context["user_intent"] = intent

    def generate_response(self):
        intent = self.context.get("user_intent")

        if intent == "greeting":
            return "Hello! How can I assist you today?"
        elif intent == "farewell":
            return "Goodbye! Have a great day!"
        elif intent == "thank_you":
            return "You're welcome! If you need anything else, feel free to ask."
        elif intent == "weather":
            return "Sure, let me check the weather for you..."
        # Add more intent-specific responses here
        else:
            return "I'm here to help. Please let me know how I can assist you."

if __name__ == "__main__":
    dialog_manager = DialogManager()

    print("Voice Assistant: Hello! Welcome to the conversation.")
    dialog_manager.start_dialog()

    while True:
        user_input = input("You: ")
        intent = input("Intent (optional): ")  # For demonstration purposes, you can manually input the intent
        dialog_manager.update_context(user_input, intent)
        
        response = dialog_manager.generate_response()
        print("Voice Assistant:", response)

