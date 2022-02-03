# Accessing Databases With Python

## SQL API

 - Works between application and DBMS (database)
 - API can send errors back
 - Application must ask API to disconnect from base

## DB_API

 - Python standard API
 - Works with several databases

### Connection objects

 - Database connections
 - Manage transactions

### Cursor Objects
 - Database queries
 - Scans through results

1. Create connection object
2. Create cursor object
3. Run queries with cursor
4. Close out
