CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_body_temperature" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_body_temperature" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Температура тела)';
COMMENT ON COLUMN public."condition_assessment_protocol_body_temperature".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_body_temperature".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_body_temperature".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_body_temperature" ("id", "parameter", "points") VALUES
  ('1', '<= 35.0', '3'),
  ('2', '35.1-36.0', '1'),
  ('3', '36.1-38.0', '0'),
  ('4', '38.1-39.0', '1'),
  ('5', '>= 39.1', '2');