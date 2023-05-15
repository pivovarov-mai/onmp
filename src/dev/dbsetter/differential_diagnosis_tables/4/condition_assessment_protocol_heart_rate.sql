CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_heart_rate" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_heart_rate" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Частота сердечных сокращений в 1 минуту)';
COMMENT ON COLUMN public."condition_assessment_protocol_heart_rate".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_heart_rate".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_heart_rate".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_heart_rate" ("parameter", "points") VALUES
  ('<= 40', '3'),
  ('41-50', '1'),
  ('51-90', '0'),
  ('91-110', '1'),
  ('111-130', '2'),
  ('>= 130', '3');