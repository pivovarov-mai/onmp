CREATE TABLE IF NOT EXISTS "mkb" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_mkb" VARCHAR(50) NOT NULL,
  "tag_id" INTEGER REFERENCES mkb_tags(id) NOT NULL
);

COMMENT ON TABLE public."mkb" IS 'Таблица кодов МКБ';
COMMENT ON COLUMN public."mkb".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."mkb".name_mkb IS 'Название кода МКБ';
COMMENT ON COLUMN public."mkb".tag_id IS 'Внешний ключ к таблице Теги МКБ';

INSERT INTO "mkb" ("id", "name_mkb", "tag_id") VALUES
  ('1', 'I10-I15.2', '2'),
  ('2', 'М10-M19', '1'),
  ('3', 'G90', '3');