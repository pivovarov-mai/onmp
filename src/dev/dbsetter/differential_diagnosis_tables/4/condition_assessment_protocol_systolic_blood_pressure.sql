CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_systolic_blood_pressure" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_systolic_blood_pressure" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Систолическое артериальное давление, мм.рт.ст.)';
COMMENT ON COLUMN public."condition_assessment_protocol_systolic_blood_pressure".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_systolic_blood_pressure".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_systolic_blood_pressure".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_systolic_blood_pressure" ("id", "parameter", "points") VALUES
  ('1', '<= 90', '3'),
  ('2', '91-100', '2'),
  ('3', '101-110', '1'),
  ('4', '111-219', '0'),
  ('5', '>= 220', '3');