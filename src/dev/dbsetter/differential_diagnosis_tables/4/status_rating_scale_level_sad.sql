CREATE TABLE IF NOT EXISTS "status_rating_scale_level_sad" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(10) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_level_sad" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Уровень САД';
COMMENT ON COLUMN public."status_rating_scale_level_sad".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_level_sad".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_level_sad".point IS 'Балл';

INSERT INTO "status_rating_scale_level_sad" ("id", "description", "point") VALUES
  ('1', '> 120', '0'),
  ('2', '100-120', '1'),
  ('3', '< 100', '2');