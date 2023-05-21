CREATE TABLE IF NOT EXISTS "status_rating_scale_wheezing" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(30) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_wheezing" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Хрипы в легких';
COMMENT ON COLUMN public."status_rating_scale_wheezing".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_wheezing".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_wheezing".point IS 'Балл';

INSERT INTO "status_rating_scale_wheezing" ("description", "point") VALUES
  ('Нет', '0'),
  ('Нижние отделы (до 1/3)', '1'),
  ('До лопаток (до 2/3)', '2'),
  ('Над всей поверхностью легких', '3');