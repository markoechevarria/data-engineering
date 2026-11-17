# Configuring cloud storage access in unity catalog

The goal of this setup is to assign specific cloud storage containers to individual catalogs or schemas, keeping data cleanly separated, organized, and securely managed

## Core Architecture Concepts

* Storage Credential: An authentication and authorization mechanism (backed by a Managed Identity or Service Principal through an Access Connector) that allows Unity Catalog to interact with cloud storage
* External Location: An object that combines a Storage Credential with a specific Cloud Storage Container
* Catalogs & Schemas: External locations are assigned directly to catalogs or schemas so that data separation is enforced at the Unity Catalog level

## Step-by-Step Implementation Guide

1. Create Dedicated Cloud Storage: Create a new cloud storage account for which you have full administrative control, rather than using the default Databricks-managed storage account
2. Create or Identify the Access Connector: Set up a dedicated Access Connector (or use Databricks' default one). Keeping it separate is recommended for cleaner access management
3. Assign the Blob Data Contributor Role: Grant the Storage Blob Data Contributor role on the data lake storage account to your access connector so it has permission to read and write data
4. Create the Storage Credential: In Unity Catalog, create the storage credential using the access connector's information. This bridges Unity Catalog with your cloud permissions
5. Create the External location: Create an external location in Unity Catalog by pairing your storage credential with the target cloud storage container
6. Grant Team Access and Granular Permissions: Apply access control lists to the storage credentials and external locations to securely share resources with your team

## Security & Authentication Flow

* Fail-Fast Enforcement: When a user references an external location, Unity Catalog verifies their permissions. If the user lacks access to the storage credential or external location, the request fails immediately without attempting cloud authentication.
* Granular Control: Administrators can manage permissions independently at both the storage credential level and the external location level for precise security management.
