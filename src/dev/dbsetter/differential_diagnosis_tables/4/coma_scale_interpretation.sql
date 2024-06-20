CREATE TABLE IF NOT EXISTS "coma_scale_interpretation" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "point" INTEGER NOT NULL,
  "sign" VARCHAR(21) NOT NULL
);

COMMENT ON TABLE public."coma_scale_interpretation" IS 'Шкала комы FOUR - Интерпретация';
COMMENT ON COLUMN public."coma_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."coma_scale_interpretation".point IS 'Балл';
COMMENT ON COLUMN public."coma_scale_interpretation".sign IS 'Признак';

INSERT INTO "coma_scale_interpretation" ("id", "point", "sign") VALUES
  ('1', '16', 'Ясное сознание'),
  ('2', '15', 'Умеренное оглушение'),
  ('3', '14', 'Глубокое оглушение'),
  ('4', '13', 'Глубокое оглушение'),
  ('5', '12', 'Сопор'),
  ('6', '11', 'Сопор'),
  ('7', '10', 'Сопор'),
  ('8', '9', 'Сопор'),
  ('9', '8', 'Кома I'),
  ('10', '7', 'Кома I'),
  ('11', '6', 'Кома II'),
  ('12', '5', 'Кома II'),
  ('13', '4', 'Кома II'),
  ('14', '3', 'Кома II'),
  ('15', '2', 'Кома II'),
  ('16', '1', 'Кома II'),
  ('17', '0', 'Кома III, гибель коры');