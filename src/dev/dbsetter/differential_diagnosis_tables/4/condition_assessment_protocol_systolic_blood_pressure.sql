CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_systolic_blood_pressure" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_systolic_blood_pressure" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Систолическое артериальное давление, мм.рт.ст.)';
COMMENT ON COLUMN public."condition_assessment_protocol_systolic_blood_pressure".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_systolic_blood_pressure".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_systolic_blood_pressure".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_systolic_blood_pressure" ("parameter", "points") VALUES
  ('<= 90', '3'),
  ('91-100', '2'),
  ('101-110', '1'),
  ('111-219', '0'),
  ('>= 220', '3');