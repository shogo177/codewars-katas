import os
import requests
from bs4 import BeautifulSoup

# Your Codewars username
USERNAME = "Neonsage177"

# Your session ID (from browser DevTools)
SESSION_ID = "627f25f897f0a969fcfd3790b02d85ef"

# Base URLs
COMPLETED_SOLUTIONS_URL = f"https://www.codewars.com/users/Neonsage177/completed_solutions"

# Headers with session cookie to stay logged in
HEADERS = {
    'Cookie': f"_session_id={SESSION_ID}"
}

# Directory to save katas
base_dir = os.getcwd()

# Loop through multiple pages if needed (adjust range for more pages)
for page in range(1, 3):
    url = COMPLETED_SOLUTIONS_URL + str(page)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    kata_blocks = soup.find_all('div', class_='item-title')

    for block in kata_blocks:
        title_tag = block.find('a')
        if title_tag:
            title = title_tag.text.strip()
            kata_link = "https://www.codewars.com" + title_tag['href']

            # Visit Kata Solution Page
            solution_page = requests.get(kata_link, headers=HEADERS)
            solution_soup = BeautifulSoup(solution_page.text, 'html.parser')

            # Find your solution code block
            code_block = solution_soup.find('code', class_='language-python')
            if code_block:
                solution_code = code_block.text.strip()
            else:
                solution_code = "# Solution code not found."

            # Find the rank on the kata page
            rank_tag = solution_soup.find('span', class_='is-extra-wide')
            if rank_tag:
                 rank = rank_tag.text.strip().replace(" ", "").lower()  # e.g., "6kyu"
            else:
                 rank = "unknown_rank"

            # Folder structure
            folder = os.path.join(base_dir, rank)
            os.makedirs(folder, exist_ok=True)

            # Clean filename
            filename = title.replace(" ", "_").lower() + ".py"
            file_path = os.path.join(folder, filename)

            # Save the solution code
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(f"# {title}\n# Link: {kata_link}\n\n{solution_code}")

print("All solutions saved successfully!")
