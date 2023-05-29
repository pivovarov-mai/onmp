CREATE TABLE IF NOT EXISTS "status_rating_scale_gallop_rhythm" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(5) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_gallop_rhythm" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Наличие ритма галопа';
COMMENT ON COLUMN public."status_rating_scale_gallop_rhythm".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_gallop_rhythm".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_gallop_rhythm".point IS 'Балл';

INSERT INTO "status_rating_scale_gallop_rhythm" ("id", "description", "point") VALUES
  ('1', 'Нет', '0'),
  ('2', 'Есть', '1');