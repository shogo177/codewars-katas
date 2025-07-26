import os

# Example Kata Data (we’ll make this auto-fetch later)
solved_katas = [
    {"title": "Sum of Numbers", "rank": "6kyu", "solution": "def sum_numbers(a, b):\n    return sum(range(min(a, b), max(a, b) + 1))"},
    {"title": "String Repeat", "rank": "8kyu", "solution": "def repeat_str(repeat, string):\n    return string * repeat"},
]

# Base folder where your codewars repo is
base_dir = os.getcwd()

# Save each kata into folders by rank
for kata in solved_katas:
    folder = os.path.join(base_dir, kata["rank"])
    os.makedirs(folder, exist_ok=True)
    
    # Clean filename (no spaces, lowercase)
    filename = kata["title"].replace(" ", "_").lower() + ".py"
    file_path = os.path.join(folder, filename)
    
    # Write solution into file
    with open(file_path, "w") as f:
        f.write(kata["solution"])

print("Katas saved successfully!")
