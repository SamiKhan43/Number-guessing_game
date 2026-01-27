import random
import time
import os
import json

class NumberGuessingGame:
    def __init__(self):
        self.highscore_file = "highscore.json"

    def clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def load_high_score(self):
        try:
            with open(self.highscore_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"name": "None", "score": float('inf')}

    def save_high_score(self, name, score):
        data = {"name": name, "score": score}
        with open(self.highscore_file, "w") as file:
            json.dump(data, file, indent=4)

    def display_main_menu(self, best_data):
        self.clear_terminal()
        print("====================================")
        print("      NUMBER GUESSING GAME          ")
        print("====================================")
        name = best_data["name"]
        score = best_data["score"]
        if score == float('inf'):
            print(" CURRENT RECORD: No scores yet")
        else:
            print(f" CURRENT RECORD: {name} with {score} attempts")
        print("------------------------------------")
        print(" 1. START GAME")
        print(" 2. VIEW RULES")
        print(" 3. EXIT")
        print("------------------------------------")

    def show_rules(self):
        self.clear_terminal()
        print("--- GAME RULES ---")
        print("1. Select a difficulty level.")
        print("2. Guess the number between 1 and 100.")
        print("3. Try to beat the record in the fewest attempts.")
        input("\nPress Enter to return to menu...")

    def get_difficulty(self):
        self.clear_terminal()
        print("--- SELECT DIFFICULTY ---")
        print("1. Easy   (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard   (3 chances)")
        choice = input("\nEnter choice (1-3): ").strip()
        if choice == '1':
            return 10
        if choice == '2':
            return 5
        if choice == '3':
            return 3

    def play_round(self, player_name):
        secret_number = random.randint(1, 100)
        chances = self.get_difficulty()
        attempts = 0
        start_time = time.time()
        print(f"\nTarget number generated. Good luck {player_name}!")

        while chances > 0:
            try:
                print(f"\nChances left: {chances}")
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            attempts += 1
            chances -= 1
            if guess > secret_number:
                print("Lower...")
            elif guess < secret_number:
                print("Higher...")
            else:
                end_time = time.time()
                elapsed = end_time - start_time
                print(f"\nCorrect! You found it in {attempts} attempts.")
                print(f"Time taken: {elapsed:.2f} seconds")
                return attempts

        end_time = time.time()
        elapsed = end_time - start_time
        print(f"\nGame Over. The number was {secret_number}.")
        print(f"Time taken: {elapsed:.2f} seconds")
        input("\nPress Enter to continue...")
        return None

    def run(self):
        self.clear_terminal()
        print("Welcome to the System")
        user_name = input("Enter your name: ").strip()
        if not user_name:
            user_name = "Player"
        while True:
            best_data = self.load_high_score()
            self.display_main_menu(best_data)
            choice = input("Select an option: ").strip()
            if choice == '1':
                score = self.play_round(user_name)
                if score is not None and score < best_data["score"]:
                    print("NEW ALL-TIME RECORD!")
                    self.save_high_score(user_name, score)
                    input("\nPress Enter to continue...")
            elif choice == '2':
                self.show_rules()
            elif choice == '3':
                print(f"Goodbye, {user_name}!")
                break
            else:
                print("Invalid selection.")
                time.sleep(1)

def main():
    game = NumberGuessingGame()
    game.run()

if __name__ == "__main__":
    main()
