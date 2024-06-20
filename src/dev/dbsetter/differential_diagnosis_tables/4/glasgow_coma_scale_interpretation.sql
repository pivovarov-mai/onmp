CREATE TABLE IF NOT EXISTS "glasgow_coma_scale_interpretation" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "point" INTEGER NOT NULL,
  "sign" VARCHAR(15) NOT NULL
);

COMMENT ON TABLE public."glasgow_coma_scale_interpretation" IS 'Шкала Глазго (Glasgow Coma Scale) - Интерпретация';
COMMENT ON COLUMN public."glasgow_coma_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."glasgow_coma_scale_interpretation".point IS 'Балл';
COMMENT ON COLUMN public."glasgow_coma_scale_interpretation".sign IS 'Признак';

INSERT INTO "glasgow_coma_scale_interpretation" ("id", "point", "sign") VALUES
  ('1', '15', 'Сознание ясное'),
  ('2', '14', 'Оглушение'),
  ('3', '13', 'Оглушение'),
  ('4', '12', 'Сопор'),
  ('5', '11', 'Сопор'),
  ('6', '10', 'Сопор'),
  ('7', '9', 'Сопор'),
  ('8', '8', 'Кома'),
  ('9', '7', 'Кома'),
  ('10', '6', 'Кома'),
  ('11', '5', 'Кома'),
  ('12', '4', 'Кома'),
  ('13', '3', 'Кома');