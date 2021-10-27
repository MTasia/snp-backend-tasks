import re


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
        if str(self.calories).isnumeric():
            return int(self.calories) < 200
        else:
            find = re.findall(r"\d*\.\d+", str(self.calories))
            if find:
                return float(self.calories) < 200
            else:
                return False

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        Dessert.__init__(self, name, calories)
        self.flavor = flavor is not None

    def is_delicious(self):
        return not self.flavor == "black licorice"


def main():
    dessert = Dessert()
    dessert.calories = "199.999"
    print(dessert.calories)
    print(dessert.is_healthy())


if __name__ == '__main__':
    main()
