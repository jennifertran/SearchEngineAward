# Contains all the basic info about awards
class Award:
    count = 0

    def __init__(self, number, name, type, application, aboriginal, renewable, value, due, description, url):
        self.number = number
        self.name = name
        self.type = type
        self.application = application
        self.aboriginal = aboriginal
        self.renewable = renewable
        self.value = value
        self.due = due
        self.description = description
        self.url = url
        Award.count += 1

        def displayCount(self):
            print "There are totally %d awards" % Award.count

        def displayAward(self):
            print "Award Number: ",self.number,", Name: ",self.name,", Type: ",self.type,", Application: ",self.application,", Aboriginal: ",self.aboriginal,", Renewable: ",self.renewable,", Value: ",self.value,", Due Day: ",self.due,", description: ",self.description,", URL: ",self.url
