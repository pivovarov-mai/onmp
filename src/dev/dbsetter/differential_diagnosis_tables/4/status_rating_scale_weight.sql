CREATE TABLE IF NOT EXISTS "status_rating_scale_weight" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(10) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_weight" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Изменился ли за последнюю неделю вес';
COMMENT ON COLUMN public."status_rating_scale_weight".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_weight".description IS 'Описание';
COMMENT ON COLUMN public."status_rating_scale_weight".point IS 'Балл';

INSERT INTO "status_rating_scale_weight" ("id", "description", "point") VALUES
  ('1', 'Нет', '0'),
  ('2', 'Увеличился', '1');