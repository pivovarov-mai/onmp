CREATE TABLE IF NOT EXISTS "status_rating_scale_neck_veins" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(15) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_neck_veins" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Набухшие шейные вены';
COMMENT ON COLUMN public."status_rating_scale_neck_veins".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_neck_veins".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_neck_veins".point IS 'Балл';

INSERT INTO "status_rating_scale_neck_veins" ("description", "point") VALUES
  ('Нет', '0'),
  ('Лежа', '1'),
  ('Стоя', '2');