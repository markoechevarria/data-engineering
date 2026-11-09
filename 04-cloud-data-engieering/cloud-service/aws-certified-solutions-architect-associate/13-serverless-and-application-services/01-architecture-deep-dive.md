# Architecture Deep Dive

## Monolithic Architecture

* Tightly Coupled Components: Internal modules heavily depend on one another, and data moves sequentially or via direct in-process function calls
* Scaling and Maintenance Challenges: As the application grows, scaling individual features independently is difficult
* If one component fails, the others also do

## Tiered Architecture

* Components are separated and can be on the same or different servers
* Each component connect to a single endpoint of another component
* Each component can scale individually according to their needs
* Load balancers can be located between each of the components, which allows scalling horizontally by adding new instances
* The components are still dependent of the others

## Microservice Architecture

* Producer: The microservice that generates and pushes a message or event to the queue
* Message Broker / Queue: The intermediary system that buffers, routes, and stores messages until they are consumed
* Consumer: The downstream microservice that pulls or receives the message and executes the task
* Dead Letter Queue (DLQ): A secondary queue that captures messages failing multiple processing attempts for debugging or manual intervention

## Event Driven Architecture

* Event producers: might be components of the application which direct interact with the customers or their might parts of the infraestructure such as EC2 or they might be systems monitoring components
* Event Consumers: pieces of software which are ready and wanting for events to occur
* Neither the event or consumers are just sat around waiting for things to occur. They are not constantly consuming resources
* Event Router: a highly available central exchange point for events. It has an **event bus** which can be thought of like a constant flow of informationo
* No constant running or waiting for things
* Producers generate events when something happens
* Events are delivered to consumers
* Consumers can perform some actions and return to a dormant state which does not consume resources once complete
