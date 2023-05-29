CREATE TABLE IF NOT EXISTS "status_rating_scale_edema" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(10) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_edema" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Отеки';
COMMENT ON COLUMN public."status_rating_scale_edema".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_edema".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_edema".point IS 'Балл';

INSERT INTO "status_rating_scale_edema" ("id", "description", "point") VALUES
  ('1', 'Нет', '0'),
  ('2', 'Плотность', '1'),
  ('3', 'Отеки', '2'),
  ('4', 'Анасарка', '3');