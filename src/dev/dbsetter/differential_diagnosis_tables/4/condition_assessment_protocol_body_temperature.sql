CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_body_temperature" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_body_temperature" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Температура тела)';
COMMENT ON COLUMN public."condition_assessment_protocol_body_temperature".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_body_temperature".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_body_temperature".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_body_temperature" ("parameter", "points") VALUES
  ('<= 35.0', '3'),
  ('35.1-36.0', '1'),
  ('36.1-38.0', '0'),
  ('38.1-39.0', '1'),
  ('>= 39.1', '2');