# Layer 2: Data Link - Frame

* Frames: 
    * A format of sending information over a layer two network
    * Components:
        * Preamble: Start frame delimiter, allows devices to know that it's the start of the frame
        * Destination Mac Address: 
        * Source Mac Address: 
        * EtherType: To specify which layer three protocol is putting its data inside A frame
        * Payload: 
            * From 46 to 1500 bites in size
            * Is the data the frame carries from source to destination
        * Frame Check Sequence: Used to identify any errors in the frame
* MAC address:
    * A hexadecimal address and 48 bits long (eg. 3e:22:fb )
    * Each device on the network has one
    * It is not software assigned, its unique attached to the hardware

* Identifiable devices
* Media access control (sharing)
* Collision detected
* Unicast 1:1
* Broadcast 1:ALL
* Switches - Like Hubs with Super powers
