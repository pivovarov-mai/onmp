CREATE TABLE IF NOT EXISTS "status_rating_scale_position" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(70) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_position" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - В каком положении находится в постели';
COMMENT ON COLUMN public."status_rating_scale_position".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_position".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_position".point IS 'Балл';

INSERT INTO "status_rating_scale_position" ("id", "description", "point") VALUES
  ('1', 'Горизонтальное', '0'),
  ('2', 'С приподнятым головным концом (2+ подушки)', '1'),
  ('3', 'С приподнятым головным концом (2+ подушки) плюс просыпается от удушья', '2'),
  ('4', 'Сидя', '3');