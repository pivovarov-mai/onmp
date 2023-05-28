CREATE TABLE IF NOT EXISTS "status_rating_scale_liver" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(20) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_liver" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Печень';
COMMENT ON COLUMN public."status_rating_scale_liver".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_liver".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_liver".point IS 'Балл';

INSERT INTO "status_rating_scale_liver" ("description", "point") VALUES
  ('Не увеличена', '0'),
  ('Увеличена до 5 см', '1'),
  ('Увеличена более 5 см', '2');