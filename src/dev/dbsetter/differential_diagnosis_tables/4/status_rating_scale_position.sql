CREATE TABLE IF NOT EXISTS "status_rating_scale_position" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(70) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_position" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - В каком положении находится в постели';
COMMENT ON COLUMN public."status_rating_scale_position".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_position".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_position".point IS 'Балл';

INSERT INTO "status_rating_scale_position" ("description", "point") VALUES
  ('Горизонтальное', '0'),
  ('С приподнятым головным концом (2+ подушки)', '1'),
  ('С приподнятым головным концом (2+ подушки) плюс просыпается от удушья', '2'),
  ('Сидя', '3');