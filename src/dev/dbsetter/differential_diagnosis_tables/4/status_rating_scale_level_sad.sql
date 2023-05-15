CREATE TABLE IF NOT EXISTS "status_rating_scale_level_sad" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(10) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_level_sad" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Уровень САД';
COMMENT ON COLUMN public."status_rating_scale_level_sad".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_level_sad".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_level_sad".point IS 'Балл';

INSERT INTO "status_rating_scale_level_sad" ("description", "point") VALUES
  ('> 120', '0'),
  ('100-120', '1'),
  ('< 100', '2');