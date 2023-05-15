CREATE TABLE IF NOT EXISTS "glasgow_coma_scale_interpretation" (
  "id" SERIAL PRIMARY KEY,
  "point" INTEGER NOT NULL,
  "sign" VARCHAR(15) NOT NULL
);

COMMENT ON TABLE public."glasgow_coma_scale_interpretation" IS 'Шкала Глазго (Glasgow Coma Scale) - Интерпретация';
COMMENT ON COLUMN public."glasgow_coma_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."glasgow_coma_scale_interpretation".point IS 'Балл';
COMMENT ON COLUMN public."glasgow_coma_scale_interpretation".sign IS 'Признак';

INSERT INTO "glasgow_coma_scale_interpretation" ("point", "sign") VALUES
  ('15', 'Сознание ясное'),
  ('14', 'Оглушение'),
  ('13', 'Оглушение'),
  ('12', 'Сопор'),
  ('11', 'Сопор'),
  ('10', 'Сопор'),
  ('9', 'Сопор'),
  ('8', 'Кома'),
  ('7', 'Кома'),
  ('6', 'Кома'),
  ('5', 'Кома'),
  ('4', 'Кома'),
  ('3', 'Кома');