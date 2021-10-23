class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name is not None
        self.calories = calories is not None

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name

    def set_calories(self, calories):
        self.calories = calories

    def is_healthy(self):
        return self.calories < 200

    def is_delicious(self):
        return True


def main():
    pass


if __name__ == '__main__':
    main()
