# Django REST framework

A small introductory project for [Django REST framework](https://www.django-rest-framework.org/), a powerful and flexible toolkit for building Web APIs.

# What is an API?

Accodring to [IBM](https://www.ibm.com/cloud/learn/api), an API (Application Programming Interface), is a set of defined rules that enable different applications to communicate with each other. It acts as an intermediary layer that processes data transfers between systems, letting companies open their application data and functionality to external third-party developers, business partners, and internal departments within their companies.

The definitions and protocols within an API help businesses connect the many different applications they use in day-to-day operations, for developers, API documentation provides the interface for communication between applications, simplifying application integration.

# What is a REST API?

According to [IBM](https://www.ibm.com/topics/rest-apis), a REST (REpresentational State Transfer) API is an API that provides a relatively high level of flexibility and freedom for developers. This flexibility is just one reason why REST APIs have emerged as a common method for connecting components and applications in a [microservices](https://www.ibm.com/topics/microservices) architecture.

Some APIs, such as [SOAP](https://www.soapui.org/) or [XML-RPC](https://en.wikipedia.org/wiki/XML-RPC), impose a strict framework on developers. But REST APIs can be developed using virtually any programming language and support a variety of data formats.

# REST design principles - aka architectural constraints

- The REST API should ensure that the same piece of data, such as the name or email address of a user, belongs to only one uniform resource identifier ([URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)), and should contain every piece of information that the client might need.

- Client and server applications must be completely independent of each other. The only information the client application should know is the ([URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)) of the requested resource; it can't interact with the server application in any other ways. Similarly, a server application shouldn't modify the client application other than passing it to the requested data via [HTTP](https://en.wikipedia.org/wiki/HTTP).

- REST APIs are stateless, meaning that each request needs to include all the information necessary for processing it, in other words they do not require any server-side sessions and server applications aren’t allowed to store any data related to a client request.

- Resources should be cacheable on the client or server side (when possible), while server responses need to contain information about whether caching is allowed for the delivered resource. The goal is to improve performance on the client side, while increasing scalability on the server side.

- The calls and responses of data go through different layers. The client and server applications don't necessarily connect directly to each other, there may be a number of different intermediaries in the communication loop, therefore REST APIs need to be designed so that neither the client nor the server can tell whether it communicates with the end application or an intermediary.

- REST APIs usually send static resources, but in certain cases, responses can also contain executable code (such as [Java applets](https://en.wikipedia.org/wiki/Java_applet)). In these cases, the code should only run on-demand.
