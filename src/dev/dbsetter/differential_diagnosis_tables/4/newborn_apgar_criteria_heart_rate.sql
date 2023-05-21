CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_heart_rate" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(20) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_heart_rate" IS 'Критерии оценки новорождённого по шкале Апгар - ЧСС';
COMMENT ON COLUMN public."newborn_apgar_criteria_heart_rate".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_heart_rate".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_heart_rate".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_heart_rate" ("description", "point") VALUES
  ('0', '0'),
  ('Меньше 100 в минуту', '1'),
  ('Больше 100 в минуту', '2');