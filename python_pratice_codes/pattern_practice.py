# abstract_factory
class Abstract_Weapon_Ireposity1:

    def automatic_shooting(self):
        pass

    def install_bullet(self):
        pass


class Abstract_Weapon_Ireposity2:

    def automatic_shooting(self):
        pass

    def install_bullet(self):
        pass


class GunWeapon_Reposity1(Abstract_Weapon_Ireposity1):

    def automatic_shooting(self):
        print("shooting by gun weapon from reposity1")

    def install_bullet(self):
        print("install bullet to the gun weapon from reposity1")


class CannonWeapon_Reposity1(Abstract_Weapon_Ireposity1):

    def automatic_shooting(self):
        print("shooting by cannonweapon from reposity1")

    def install_bullet(self):
        print("install bullet to the cannonweapon from reposity1")


class GunWeapon_Reposity2(Abstract_Weapon_Ireposity2):

    def automatic_shooting(self):
        print("shooting by gun weapon from reposity2")

    def install_bullet(self):
        print("install bullet to the gun weapon from reposity2")


class CannonWeapon_Reposity2(Abstract_Weapon_Ireposity2):

    def automatic_shooting(self):
        print("shooting by cannon weapon from reposity2")

    def install_bullet(self):
        print("install bullet to the cannon weapon from reposity2")


class Ifactory:

    def create_reposity1(self):
        pass

    def create_reposity2(self):
        pass


class Gun_factory(Ifactory):

    def create_reposity1(self):
        temp = GunWeapon_Reposity1()
        return temp

    def create_reposity2(self):
        temp = GunWeapon_Reposity2()
        return temp


class Cannon_factory(Ifactory):

    def create_reposity1(self):
        temp = CannonWeapon_Reposity1()
        return temp

    def create_reposity2(self):
        temp = CannonWeapon_Reposity2()
        return temp


# simple factory-------

class Ifeed:

    def getFeed(self):
        pass


class EatFeed(Ifeed):

    def __init__(self, eat_happeniness_rate):
        self.eat_happeniness_rate = eat_happeniness_rate

    def getFeed(self):
        if(self.eat_happeniness_rate > 0.5):
            print("very happeniness")
        else:
            print("very tradegy")


class DrinkFeed(Ifeed):

    def __init__(self, drink_happeniness_rate):
        self.drink_happeniness_rate = drink_happeniness_rate

    def getFeed(self):
        if(self.drink_happeniness_rate > 0.5):
            print("the drink tastes very well ")
        else:
            print("very disgusting")


class GameFeed(Ifeed):

    def __init__(self, game_happeniness_rate):
        self.game_happeniness_rate = game_happeniness_rate

    def getFeed(self):
        if(self.game_happeniness_rate > 0.5):
            print("the game is very intresting")
        else:
            print("so bad")


class TVFeed(Ifeed):

    def __init__(self, TV_happeniness_rate):
        self.TV_happeniness_rate = TV_happeniness_rate

    def getFeed(self):
        if(self.TV_happeniness_rate > 0.5):
            print("the TV show is very exicting")
        else:
            print("so boring")


class uniFeed(Ifeed):

    def getFeed(self):
        print("no feed of this type")


class FeedFactory:
    feeds = {}
    feeds['eat'] = EatFeed(0.4)
    feeds['drink'] = DrinkFeed(0.8)
    feeds['game'] = GameFeed(0.3)
    feeds['TVshow'] = TVFeed(0.4)

    def create_feed_type(self, ch):
        if(ch not in self.feeds.keys()):
            return uniFeed()
        else:
            return self.feeds[ch]
#-----------------strategy pattern-------------------------


class Istrategy:

    def operate(self):
        pass


class Prevent_Strategy(Istrategy):

    def operate(self):
        print("prevent ...")


class Attack_Strategy(Istrategy):

    def operate(self):
        print("attack ...")


class Negotiation_Strategy(Istrategy):

    def operate(self):
        print("negotiating ...")


class Context:

    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.operate()


context = Context(Prevent_Strategy())
context.execute()


feedfactory = FeedFactory()
eat_feed = feedfactory.create_feed_type('eat')
eat_feed.getFeed()


gun_factory = Gun_factory()
gun = gun_factory.create_reposity1()
gun.automatic_shooting()
gun.install_bullet()
