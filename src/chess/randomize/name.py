import random


class RandomName:

    @staticmethod
    def person_name() -> str:
        first_names = [
            "Amani", "Kwame", "Zahara", "Tumelo", "Nala","Wei", "Priya", "Haruto", "Mei", "Ravi",
            "Emma", "Luca", "Sophie", "Mateo", "Freya", "Santiago", "Olivia", "Ximena", "Elijah",
            "Camila", "Tane", "Hine", "Manaia", "Aroha", "Kauri", "Leila", "Amir", "Yara", "Omar",
            "Layla", "Arjun", "Aanya", "Kabir", "Diya", "Rohan", "Hao", "Yuki", "Min", "Jin", "Hana",
            "Aylen", "Dakota", "Kai", "Tala", "Mato", "Sofia", "Idris", "Zuri", "Kofi", "Anaya"
        ]
        return random.choice(first_names)


    @staticmethod
    def cybernaut_name() -> str:
        allowed_letters = [c for c in string.ascii_lowercase if c not in {'i', 'l', 'o'}]
        allowed_numbers = [str(n) for n in range(2, 10)]

        random_letters = random.choices(allowed_letters, k=3)
        random_numbers = random.choices(allowed_numbers, k=3)

        return f"{''.join(random_letters)}-{''.join(random_numbers)}".upper()
