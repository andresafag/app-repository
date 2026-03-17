CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(250)
);


INSERT INTO products (name, description) VALUES ('bread', 'spongy');
INSERT INTO products (name, description) VALUES ('lasagna', 'tasty');
