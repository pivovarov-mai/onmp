CREATE TABLE IF NOT EXISTS "status_rating_scale_dyspnea" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(15) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_dyspnea" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Одышка';
COMMENT ON COLUMN public."status_rating_scale_dyspnea".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_dyspnea".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_dyspnea".point IS 'Балл';

INSERT INTO "status_rating_scale_dyspnea" ("description", "point") VALUES
  ('Нет', '0'),
  ('При нагрузке', '1'),
  ('В покое', '2');