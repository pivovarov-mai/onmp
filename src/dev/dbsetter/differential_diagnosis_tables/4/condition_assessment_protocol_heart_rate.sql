CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_heart_rate" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_heart_rate" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Частота сердечных сокращений в 1 минуту)';
COMMENT ON COLUMN public."condition_assessment_protocol_heart_rate".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_heart_rate".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_heart_rate".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_heart_rate" ("id", "parameter", "points") VALUES
  ('1', '<= 40', '3'),
  ('2', '41-50', '1'),
  ('3', '51-90', '0'),
  ('4', '91-110', '1'),
  ('5', '111-130', '2'),
  ('6', '>= 130', '3');