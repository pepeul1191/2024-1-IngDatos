-- migrate:up

ALTER TABLE users ADD COLUMN activation_key VARCHAR(20);
ALTER TABLE users ADD COLUMN reset_key VARCHAR(20);

-- migrate:down

ALTER TABLE users DROP COLUMN activation_key VARCHAR(20),
ALTER TABLE users DROP COLUMN reset_key VARCHAR(20);