CREATE TABLE IF NOT EXISTS "coma_scale_stem_reflexes" (
  "id" SERIAL PRIMARY KEY,
  "sign" VARCHAR(45) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."coma_scale_stem_reflexes" IS 'Шкала комы FOUR - Стволовые рефлексы (B)';
COMMENT ON COLUMN public."coma_scale_stem_reflexes".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."coma_scale_stem_reflexes".sign IS 'Признак';
COMMENT ON COLUMN public."coma_scale_stem_reflexes".points IS 'Баллы';

INSERT INTO "coma_scale_stem_reflexes" ("sign", "points") VALUES
  ('Зрачковый и роговичный рефлексы сохранены', '4'),
  ('Один зрачок расширен и не реагирует на свет', '3'),
  ('Зрачковый ИЛИ роговичный рефлекс отсутствует', '2'),
  ('Зрачковый и роговичный рефлексы отсутствуют', '1');