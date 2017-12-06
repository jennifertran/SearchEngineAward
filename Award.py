# Contains all the basic info about awards
class Award:
  count = 0

  def __init__(self, url, number, name, type, application, restrictions, renewable, value, due, description,
               sequence):
    self.url = url
    self.number = number
    self.name = name
    self.type = type
    self.application = application
    self.restrictions = restrictions
    self.renewable = renewable
    self.value = value
    self.due = due
    self.description = description
    self.sequence = sequence
    Award.count += 1

  def displayCount(self):
    return "There are a total of %d awards" % Award.count

  def displayAward(self):
    return "Award Number: ", self.number, ", Name: ", self.name, ", Type: ", self.type, ", Application: ", self.application, ", Restrictions: ", self.restrictions, ", Renewable: ", self.renewable, ", Value: ", self.value, ", Due Day: ", self.due, ", description: ", self.description, ", URL: ", self.url
