CREATE TABLE IF NOT EXISTS "user_profile" (
  "id" SERIAL PRIMARY KEY NOT NULL ,
  "last_name" VARCHAR(50) NOT NULL,
  "first_name" VARCHAR(50) NOT NULL,
  "middle_name" VARCHAR(50) NOT NULL,
  "date_of_birth" DATE,
  "phone_number" VARCHAR(20),
  "passport" VARCHAR(50),
  "account_user_id" INTEGER REFERENCES account_user(id) NOT NULL
);

COMMENT ON TABLE public."user_profile" IS 'Пользователи (врачи)';
COMMENT ON COLUMN public."user_profile".id IS 'ID врача';
COMMENT ON COLUMN public."user_profile".last_name IS 'Фамилия';
COMMENT ON COLUMN public."user_profile".first_name IS 'Имя';
COMMENT ON COLUMN public."user_profile".middle_name IS 'Отчество';
COMMENT ON COLUMN public."user_profile".date_of_birth IS 'Дата рождения';
COMMENT ON COLUMN public."user_profile".phone_number IS 'Номер телефона';
COMMENT ON COLUMN public."user_profile".passport IS 'Паспортные данные';
COMMENT ON COLUMN public."user_profile".user_id IS 'Внешний ключ к таблице account_user на бэке';

INSERT INTO "user_profile" ("last_name", "first_name", "middle_name", "date_of_birth", "phone_number", "passport", "user_id") VALUES
  ('Иванов', 'Иван', 'Иванович', '1978-04-04', '88005553535', '5353 535353', '1');