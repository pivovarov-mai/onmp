CREATE TABLE IF NOT EXISTS "tactics" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_tactics" TEXT NOT NULL
);

COMMENT ON TABLE public."tactics" IS 'Тактика диагноза';
COMMENT ON COLUMN public."tactics".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."tactics".name_tactics IS 'Наименование тактики';

INSERT INTO "tactics" ("id", "name_tactics") VALUES
  ('1', '1. Рекомендовать обратиться в поликлинику.'),
  ('2', '1. Актив в поликлинику.'),
  ('3', '2. Вызов бригады СМП при отсутствии эффекта от проведённой терапии или при наличии в анамнезе аневризмы сосудов головного мозга в сочетании с головной болью.'),
  ('4', '3. В случае отказа от вызова бригады СМП актив в ОНМПВиДН.'),
  ('5', '1. Рекомендовать обратиться в поликлинику.'),
  ('6', '1. Рекомендовать обратиться в поликлинику.');