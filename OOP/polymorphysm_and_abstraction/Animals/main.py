from project.dog import Dog
from project.kitten import Kitten
from project.tomcat import Tomcat

kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)

dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)