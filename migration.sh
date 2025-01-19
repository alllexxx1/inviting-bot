#!/bin/bash

DB_DIR="crm"
DB_FILE="$DB_DIR/crm.db"
SQL_FILE="$DB_DIR/initial_migration.sql"


if [ ! -d "$DB_DIR" ]; then
  echo "Directory '$DB_DIR' does not exist. Please create it first."
  exit 1
fi

if [ -f "$DB_FILE" ]; then
  echo "Database file '$DB_FILE' already exists."
else
  sqlite3 "$DB_FILE" "VACUUM;"
  if [ $? -eq 0 ]; then
    echo "Database file '$DB_FILE' has been created successfully in the '$DB_DIR' directory."
  else
    echo "An error occurred while creating the database file."
  fi
fi

sqlite3 "$DB_FILE" < "$SQL_FILE"
if [ $? -eq 0 ]; then
  echo "SQL file '$SQL_FILE' executed successfully. Table 'users' has been created in '$DB_FILE'."
else
  echo "An error occurred while executing the SQL file."
  exit 1
fi
