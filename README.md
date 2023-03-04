`source venv/bin/activate`


`flask run`


`flask db drop`
`flask db create`
`flask db seed`


db_dev

CREATE DATABASE notes;
CREATE USER db_dev WITH PASSWORD 'db_dev'; (password for quentin is 123456 instead of 'db_dev'. from trello clone example)
GRANT ALL PRIVILEGES ON DATABASE pet_rent_db TO db_dev;

I couldn't create tables with `flask db create` until I also run
GRANT ALL PRIVILEGES ON SCHEMA public TO db_dev;


Note model needed to be written and `flask db create` before adding relationships? maybe?


`select * from "user";`


## Auth

## Require Login
Add, Edit, or Delete 

## Don't require login
Listing planets and register new planet endpoint
