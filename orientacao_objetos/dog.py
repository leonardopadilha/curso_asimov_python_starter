class Dog:
  def __init__(self, raca):
    self.raca = raca
    self.idade = 10

  def envelhecer(self):
    self.idade += 1

dog = Dog('Vira lata')
print(dog.raca)

print(dog.idade)
dog.envelhecer()
print(dog.idade)

print()

class Circle:
  def __init__(self, raio=1):
    self.raio = raio

  def calcula_area(self):
    return self.raio * self.raio * 3.14
  
  def retorna_raio(self):
    return self.raio

c1 = Circle()
c2 = Circle(2)

print(c1.calcula_area())
print(c2.calcula_area())
print(c2.retorna_raio())