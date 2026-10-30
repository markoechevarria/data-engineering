# Object Versioning and MFA delete

## Object Versioning

* Controlled at bucket level and is disabled by default
* When the versioning was enabled it cannot be disabled, but it can be suspended and viceversa
* Without versioning the ID of the objects in the bucket are set to null, when an object is modified the original version of that object is replaced
* Versioning let store multiple versions of an object within a bucket, using ID to identify objects
* When the object is requested the object marked as "Current version" is retrieved
* Objects also can be requested with a specific version using the ID 
* When an object is deleted, an delete marked (which can be deleted)is added at the top of the object versions, which maked it look deleted
* When providing the object name and the version, an versioned object can be fully deleted
* All version objects are billed

## MFA delete

* It's enabled within the versioning configuration on a bucket
* When activated MFA is required to change bucket versioning state
* When activated MFA is required to delete any versions of an object
* The Serial Number (MFA) and the code that it generates needs to be provided when performing API calls 
