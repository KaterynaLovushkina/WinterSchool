from multipledispatch import dispatch


class FishInfo:
    def __init__(self, name, price_in_uah_per_kilo, origin, catch_date, due_date, isAlive):
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.catch_date = catch_date
        self.due_date = due_date
        self.isAlive = isAlive

    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Origin:{self.origin}\n'
                f'Price per kilo:{self.price_in_uah_per_kilo} UAH\n'
                f'Catch date:{self.catch_date}\n'
                f'Due date:{self.due_date}\n'
                f'Alive:{self.isAlive}\n')


class Fish(FishInfo):
    def __init__(self, name, price_in_uah_per_kilo, origin, catch_date, due_date, isAlive, age_in_months,
                 weight) -> None:
        super().__init__(name, price_in_uah_per_kilo, origin, catch_date, due_date, isAlive)
        self.age_in_months = age_in_months
        self.weight = weight

    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Origin:{self.origin}\n'
                f'Price per kilo:{self.price_in_uah_per_kilo} UAH\n'
                f'Catch date:{self.catch_date}\n'
                f'Due date:{self.due_date}\n'
                f'Alive:{self.isAlive}\n'
                f'Age ih months: {self.age_in_months} months\n'
                f'Weight:{self.weight} kg\n'
                f'\n')


class FishBox:
    def __init__(self, other, weightBox, package_date, height, weight, length):
        self.weightBox = weightBox
        self.package_date = package_date
        self.height = height
        self.weight = weight
        self.length = length
        self.fish_information = other

    def __repr__(self):
        return (f'{self.fish_information}'
                f'Weight of Box with fish: {self.weightBox} kg\n'
                f'Package date:{self.package_date}\n'
                f'Height of box:{self.height} m\n'
                f'Weight of box:{self.weight} m\n'
                f'Lenght of box:{self.length} m\n'
                f'\n')


class FishShop():

    def __init__(self):
        self.my_dict_for_fish = {}
        self.my_dict_for_fish_box = {}
        self.list_of_buy = []
        pass

    @dispatch(Fish)
    def add_fish(self, fish) -> None:
        if fish.isAlive == True:
            if fish.name in self.my_dict_for_fish:
                self.my_dict_for_fish[fish.name].append(fish)
            else:
                self.my_dict_for_fish[fish.name] = [fish]
        else:
            print("The fish is not alive, something went wrong)")
            self.my_dict_for_fish_box[FishBox.fish_information.name] = FishBox

    @dispatch(FishBox)
    def add_fish(self, fishBox: FishBox) -> None:
        if fishBox.fish_information.isAlive == False:
            if fishBox.fish_information.name in self.my_dict_for_fish_box:
                self.my_dict_for_fish_box[fishBox.fish_information.name].append(fishBox)
            else:
                self.my_dict_for_fish_box[fishBox.fish_information.name] = [fishBox]
        else:
            print("The fish is  alive, something went wrong)")
            self.my_dict_for_fish[Fish.name] = Fish

    def sell_fish(self, fish_name: str, weight: float, isAlive: bool) -> Union[str, float]:

        if isAlive == True:
            for key in self.my_dict_for_fish:
                if key == fish_name:
                    for fish in self.my_dict_for_fish[key]:
                        if fish.weight >= weight:
                            fish.weight -= weight
                            price = weight * fish.price_in_uah_per_kilo
                            self.list_of_buy.append([fish_name, weight, isAlive, price])
                        elif fish.weight < weight:
                            print('Sorry we dont have {} of {}, we have only {}'.format(weight, fish_name, fish.weight))
                        elif fish.weight == 0:
                            print("\nSorry we ran out of {}".format(fish_name))
                            self.my_dict_for_fish[key].delete(fish)
        elif isAlive == False:
            for key in self.my_dict_for_fish_box:
                if key == fish_name:
                    for fish_box in self.my_dict_for_fish_box[key]:
                        if fish_box.weightBox >= weight:
                            fish_box.weightBox -= weight
                            price = weight * fish_box.fish_information.price_in_uah_per_kilo
                            self.list_of_buy.append([fish_name, weight, isAlive, price])
                        elif fish_box.weightBox < weight:
                            print('Sorry we dont have', weight, ' kg of ', fish_name, ' we have only ',
                                  fish_box.weightBox, 'kg')
                        elif fish_box.weight == 0:
                            self.my_dict_for_fish_box[key].delete(fish_box)
        else:
            print("We don`t have that {} in the shop.".format(fish_name))

    def get_fresh_fish_names_sorted_by_price(self):
        sorted_fresh_fish_by_price = []
        print('----------------------------------Sorted list of fish------------------------------')
        for key in self.my_dict_for_fish:
            for i in range(len(self.my_dict_for_fish[key])):
                sorted_fresh_fish_by_price.append(
                    [self.my_dict_for_fish[key][i].name, self.my_dict_for_fish[key][i].price_in_uah_per_kilo])
        sorted_fresh_fish_by_price.sort(key=lambda price: price[1])
        for i in sorted_fresh_fish_by_price:
            print('Name: ', i[0], '   Price:', i[1], 'UAH')

    def get_frozen_fish_names_sorted_by_price(self):
        print('----------------------------------Sorted list of fish box------------------------------')
        list = []
        for fish in self.my_dict_for_fish_box:
            for box in self.my_dict_for_fish_box[fish]:
                price = box.fish_information.price_in_uah_per_kilo
                break
            list.append((fish, price))
        sorted_frozen_fish_by_price = sorted(list, key=lambda x: x[1])
        for i in sorted_frozen_fish_by_price:
            print('Name: ', i[0], '   Price:', i[1], 'UAH')

    def show_dict(self):
        print('------------------------- dictionary of fish-------------------------')
        for key, value in self.my_dict_for_fish.items():
            print(key, ' : ', value)
        print()
        print('------------------------- dictionary of boxes-------------------------')
        for key, value in self.my_dict_for_fish_box.items():
            print(key, ' : ', value)
        print('------------------------- Purchase-------------------------')
        for i in self.list_of_buy:
            print('Name:', i[0], '   Weight:', i[1], 'kg', '  Alive:', i[2], '  Price:', i[3], 'UAH')


class Seller:
    def discover_which_fish_the_freshest(self):
        pass

    def successful_transition(self, money_received, fish_cost):
        pass


class Buyer:
    def find_out_info_about_fish(self):
        pass

    def buy_fish(self):
        pass


# -------------------------------------------
fish_shop = FishShop()
fish_shop.add_fish(Fish('sea Bream', 106, 'Norwey', "11/12/21", "3/4/22", True, 2, 5.5))
fish_shop.add_fish(Fish('corop', 136, 'Italy', "11/11/21", "3/5/22", True, 2, 7.65))
fish_shop.add_fish(Fish('tilapia', 99, 'Japan', "1/1/22", "3/6/22", True, 1, 4.4))
fish_shop.add_fish(Fish('cod', 168, 'German', "30/11/21", "9/4/22", True, 3, 8.16))
fish_shop.add_fish(Fish('cod', 168, 'German', "30/11/21", "9/4/22", True, 3, 86.16))

fish_1 = FishInfo('salmon', 55, 'Norwey', "1/12/21", "3/4/22", False)
fish_2 = FishInfo('trout', 67, 'Swedish', "1/12/21", "3/4/22", False)
fish_3 = FishInfo('pollock', 73, 'Chine', "1/12/21", "3/4/22", False)
fish_4 = FishInfo('sardine', 45, 'Indonesia', "1/12/21", "3/4/22", False)
fish_5 = FishInfo('tilapia', 48, 'United States', "1/12/21", "3/4/22", False)
fish_6 = FishInfo('swordfish', 69, 'India', "1/12/21", "3/4/22", False)
fish_7 = FishInfo('rohu', 50, 'Japan', "1/12/21", "3/4/22", False)
fish_8 = FishInfo('prawn', 66, 'Peru', "1/12/21", "3/4/22", False)
fish_9 = FishInfo('anchovies', 51, 'India', "1/12/21", "3/4/22", False)
fish_10 = FishInfo('sardine', 87, 'Chile', "1/12/21", "3/4/22", False)

fish_shop.add_fish(FishBox(fish_1, 44, "12/1/22", 4.4, 7, 6.3))
fish_shop.add_fish(FishBox(fish_2, 50, "12/1/22", 4.4, 7, 6.3))
fish_shop.add_fish(FishBox(fish_3, 80, "12/1/22", 3.4, 7, 6.3))
fish_shop.add_fish(FishBox(fish_4, 28, '12/1/22', 8.48, 7, 6.3))
fish_shop.add_fish(FishBox(fish_5, 18, '12/1/22', 8, 7, 6.3))
fish_shop.add_fish(FishBox(fish_6, 40, '12/1/22', 9.4, 4, 3))
fish_shop.add_fish(FishBox(fish_7, 61, '12/1/22', 5.4, 6, 3))
fish_shop.add_fish(FishBox(fish_8, 33, '12/1/22', 4.4, 7, 6.3))
fish_shop.add_fish(FishBox(fish_9, 26, '12/1/22', 7.94, 6, 6.3))
fish_shop.add_fish(FishBox(fish_10, 50, '12/1/22', 3.4, 7, 6.3))

fish_shop.show_dict()
fish_shop.sell_fish('prawn', 20, False)
fish_shop.sell_fish('salmon', 2, False)
fish_shop.sell_fish('tilapia', 1.2, True)
fish_shop.show_dict()
fish_shop.get_fresh_fish_names_sorted_by_price()
print()
fish_shop.get_frozen_fish_names_sorted_by_price()


