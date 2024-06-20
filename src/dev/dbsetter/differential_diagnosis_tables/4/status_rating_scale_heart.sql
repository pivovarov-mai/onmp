CREATE TABLE IF NOT EXISTS "status_rating_scale_heart" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(15) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_heart" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Жалобы на перебои в работе сердца';
COMMENT ON COLUMN public."status_rating_scale_heart".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_heart".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_heart".point IS 'Балл';

INSERT INTO "status_rating_scale_heart" ("id", "description", "point") VALUES
  ('1', 'Нет', '0'),
  ('2', 'Есть', '1');