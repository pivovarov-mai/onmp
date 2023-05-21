CREATE TABLE IF NOT EXISTS "coma_scale_interpretation" (
  "id" SERIAL PRIMARY KEY,
  "point" INTEGER NOT NULL,
  "sign" VARCHAR(21) NOT NULL
);

COMMENT ON TABLE public."coma_scale_interpretation" IS 'Шкала комы FOUR - Интерпретация';
COMMENT ON COLUMN public."coma_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."coma_scale_interpretation".point IS 'Балл';
COMMENT ON COLUMN public."coma_scale_interpretation".sign IS 'Признак';

INSERT INTO "coma_scale_interpretation" ("point", "sign") VALUES
  ('16', 'Ясное сознание'),
  ('15', 'Умеренное оглушение'),
  ('14', 'Глубокое оглушение'),
  ('13', 'Глубокое оглушение'),
  ('12', 'Сопор'),
  ('11', 'Сопор'),
  ('10', 'Сопор'),
  ('9', 'Сопор'),
  ('8', 'Кома I'),
  ('7', 'Кома I'),
  ('6', 'Кома II'),
  ('5', 'Кома II'),
  ('4', 'Кома II'),
  ('3', 'Кома II'),
  ('2', 'Кома II'),
  ('1', 'Кома II'),
  ('0', 'Кома III, гибель коры');