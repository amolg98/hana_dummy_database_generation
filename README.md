# hana_dummy_database_generation
This is a simple attempt at generating a dummy database. There are mulitple options to quickly populate database:
  - Populate with Images(to quickly populate database with TBs of data)
  - Populate with millions of records (won't make database in terms of TBs of data but will give load of dummy customer data along with order data)

This is work in progress. Anyone and everyone is free to use this project howsoever they deem fit. This could be customized further to one's requirement.

# install pip module pyhdb
  pip install pyhdb

# login to HANA db using either HANA Studio or command line
  Using command line:
  $ su - <SID_in_lowercase>adm
  $ hdbsql -i 00 -u <HANA_DB_Username> -p <HANA_DB_password>

  once in create few tables by executing commands given in HANA_CMDS.sql file
  line 11, 14, 17 and 20 

# Start populating the database
  Execute following command:
    python DummyDatabaseGeneration.py