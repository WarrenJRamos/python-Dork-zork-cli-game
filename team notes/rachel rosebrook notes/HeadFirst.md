[Chapter 1 Welcome to Design Patterns](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-1-welcome-to-design-patterns)
[Chapter 2 Keeping your Objects in the Know](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-2-keeping-your-objects-in-the-know)
[Chapter 3 Decorating Objects](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-3-decorating-objects)
[Chapter 4 Baking with OO Goodness](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-4-baking-with-oo-goodness)
[Chapter 5 One of a Kind Objects](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-5-one-of-a-kind-objects)
[Chapter 6 Encapsulating Invocation](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-6-encapsulating-invocation)
[Chapter 7 Being Adaptive](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-7-being-adaptive)
[Chapter 8 Encapsulating Algorithms](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-8-encapsulating-algorithms)
[Chapter 9 Well-Managed Collections](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-9-well-managed-collections)
[Chapter 10 The State of Things](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-10-the-state-of-things)
[Chapter 11 Controlling Object Access](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-11-controlling-object-access)
[Chapter 12 Pattern of Patterns](https://github.com/WarrenJRamos/Dork/blob/feature/notes/team%20notes/rachel%20rosebrook%20notes/HeadFirst.md#chapter-12-pattern-of-patterns)

# Chapter 1 Welcome to Design Patterns
## Principals:
- Identify the aspects of your application that vary and separate them from what stays the same
- Program to an interface, not an implimentation
- Favor composition over inheritance

## Pattern:
  #### Strategy Pattern: 
    Defines a family of algorithms, encapsulates each one, and makes them interchangeable.  
    This lets the algorithm vary independently from the clients using it.

### Encapsulation
Encapsulation is the idea that one takes break code down until you are left with simply what is expected to be unchanging. Beyond that, encapsulate (separate from) anything that is expected to have changes.  Astract these ideas and commonly group them.

Anticipating what bits will be the most variable in the future can help save time down the road if encapsulation is implemented appropriately early on.

### Programming to an Interface
Abstract ideas and commonly group them.  Instead of a ‘bark’ class for dogs and a ‘meow’ class for cats, use a sound class for animals with unique implementation at the sound level, not the animal level.  However, we need not have needless middle classes - if we’re concerned with each breed and not just the species, we can have simply SiameseCats and ChihuahuaDogs instead of having Siamese as a subclass of Cats.

### Strategy Pattern
This pattern encapsulates interchangeable behaviors and uses delegation to decide which behavior to use at the call

```
 // DON'T program to an implementation
 Dog d = new Dog();
 d.bark();

 // DO program to an interface
 Animal animal = new Dog();
 animal.makeSound();

 //implement only at runtime
 //we don't know the animal's subtype, but it knows what it'll do to makeSound()
 a = GetAnimal(); 
 a.makeSound();
 ```
 
 ### Composition
 Composition permits behavior changes at run time by implimenting a new behavior interface.  
 
 # Chapter 2 Keeping your Objects in the Know
 ## Principals:
 - Strive for loosely coupled designs between objects that interact
 
 ## Patterm:
  #### Observer Pattern:
    Defines a one-to-many dependency between objects so that when one object changes state, 
    all its dependents are notified and updated automatically.
    
In the obverser pattern there are two specific roles, the SUBJECT and the OBERSERVERS
##### Subject: 
The subject holds the current data state.  
The subject manages the set of observers.
##### Observers:
The observers are registered with the subject to receive updates from the subject.

### Loosely coupling interactions
When two objects are loosely coupled, they can interact without knowing much about each other.
#### Loose coupling has many benefits
- The subject only needs to know that an observer implements the observer interface
- We can add/remove new observers at any time
  - This can also be done without modifying the subject
- We can reuse subjects and observers independently
- Changes to either the subject or an observer does not affect the other

### Observer Pattern and Java
Java has its own built-in Observer Pattern: 
Impliment the Observer interface to make an object an observer:
  java.util.Observer
To send notifications, expect the java.util.Observer superclass and
  1. You must call the setChanged() method to signify that the state has changed
  2. Then you must call either:
    - notifyObservers()
    - notifyObservers(Object arg) 
To receive notifcations:
  - update(Observable o) or
  - update(Observable o, Object arg)
  
### Problems with the Java Observer Pattern
- Observable is a class, which means you have to subclass it
- Observable protects crucial methods, which requires subclasses again
You can either extend java.util.Obersvable, or use your own implementation

### Example implementation
```
public interface Subject {
  public void registerObserver(Observer o);
  public void removeObservers(Observer o);
  public voic notifyObservers();
}

#vars are the values the Observer gets from the Subject
public interface Observer {
  public void update(float temperature, float humidity, float pressure);
}

#this single method is called when we need to display
public interface DisplayElement {
  public void display();
}

#impliment Subject interface
public class WeatherData implements Subject {
  private ArrayList observers;
  private float temperature;
  private float humidity;
  private float pressure;
  
  public WeatherData() {
    observers = new ArrayList90;
  }
  
  #when an observer registers, add to end of list
  public void registerObserver(Observer o) {
    observers.add(o);
  }
  
  #when unregister, remove from list
  public void removeObserver(Observer o) {
    int i = observers.indexOf(o);
    if (i >= 0) {
      observers.remove(i);
    }
  }
  
  #tell observers about the current state
  public void notifyObservers() {
    for (int i = 0; i < observers.size(); i++) {
      Observer observer = (Observer)observers.get(i);
      observer.update(temperature, humidity, pressure);
    }
  }
  
  #notify that there's an update
  public voic measurementsChanged() {
    notifyObservers();
  }
  
  #display elements
  public void setMeasurements(float temperature, float humidity, float pressure) {
    this.temperature = temperature;
    this.humidity = humidity;
    this.pressure = pressure;
    measurementsChanged();
  }
  
  //etc
}
```

# Chapter 3 Decorating Objects
## Principal:
- Classes should be open for extension but closed for modification

## Pattern:
  #### Decorator Pattern: 
    Attach additional responsibilities to an object dynamically.  
    Decorators provide a flexible alternative to subclassing for extending functionality.

### Decorator
Decorator allows one to not alter the interface while adding responsibility.
    
# Chapter 4 Baking with OO Goodness
## Principal: 
- Depend on abstractions, do not depend on concrete classes.

## Patterns:
  #### Factory Method:
    Define an interface fro creating an object, but let subclasses decide which class to instantiate.
    Factory Method lts a class defer instantiation to the subclasses.
  #### Abstract Factory:
    Provide an interface for creating familes of related or dependent objects 
    without specifying their concrete classes.

### Factory Method
In this pattern, subclasses decide which concrete classes to create.
    
# Chapter 5 One of a Kind Objects
## Pattern: 
  #### Singleton
    Ensure a class only has one instance 
    and provide a global point of access to it.
    
# Chapter 6 Encapsulating Invocation
## Pattern:
  #### Command:
    Encapsulates a request as an object, 
    thereby letting you parameterize clients with different requests, 
    queue or log requetss, and support undoable operations.

# Chapter 7 Being Adaptive
## Principal:
- Only talk to your friends

## Patterns:
  #### Adapter:
    Converts the interface of a class into another interface clients expect.
    Lets classes work together that couldn't otherwise bc of incompatibile interfaces.
  #### Facade:
    Provides a unified interface to a set of interfaces in a subsystem.  
    Facade defines a higher-level interface that makes the subsystem easier to see.
    
### Adapter
Adapter converts one interface into another

### Facade
Facade makes the interface simpler.

# Chapter 8 Encapsulating Algorithms
## Principal:
- Don't call us, we'll call you

## Pattern:
  #### Template Method
    Define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
    Template Method lets subclasses redefine certain steps of an algorithm 
    without changing the algorithm's structure.
    
### Template Method
Subclasses decide how to implement the steps in an algorithm

# Chapter 9 Well-Managed Collections
## Principal:
- A class should have only one reason to change

## Patterns:
  #### Iterator:
    Provide a way to access the elements of an aggregate object sequentially 
    without exposing its underlying representation
    
  #### Composite:
    Compose objects into tree structures to represent part-whole heirarchies.  
    Composite lets clients treat individual objects and compositions of objects uniformly.
    
# Chapter 10 The State of Things
## Pattern:
  #### State
    Allows an object to alter its behavior when its internal state changes.
    The object will appear to change its class.
   
# Chapter 11 Controlling Object Access
## Pattern: 
  #### Proxy
    Provide a surrogate or placeholder for another object to control access to it

# Chapter 12 Pattern of Patterns
## Pattern:
  #### Compound Patterns
    A Compound Pattern combines two or more patterns into a solution that solves a recurring or general problem.


