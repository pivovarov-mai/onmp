CREATE TABLE IF NOT EXISTS "status_rating_scale_gallop_rhythm" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(5) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_gallop_rhythm" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Наличие ритма галопа';
COMMENT ON COLUMN public."status_rating_scale_gallop_rhythm".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_gallop_rhythm".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_gallop_rhythm".point IS 'Балл';

INSERT INTO "status_rating_scale_gallop_rhythm" ("description", "point") VALUES
  ('Нет', '0'),
  ('Есть', '1');