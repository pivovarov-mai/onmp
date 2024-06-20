CREATE TABLE IF NOT EXISTS "status_rating_scale_neck_veins" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(15) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_neck_veins" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Набухшие шейные вены';
COMMENT ON COLUMN public."status_rating_scale_neck_veins".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_neck_veins".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_neck_veins".point IS 'Балл';

INSERT INTO "status_rating_scale_neck_veins" ("id", "description", "point") VALUES
  ('1', 'Нет', '0'),
  ('2', 'Лежа', '1'),
  ('3', 'Стоя', '2');