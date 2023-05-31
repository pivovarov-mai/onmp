CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_heart_rate" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(20) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_heart_rate" IS 'Критерии оценки новорождённого по шкале Апгар - ЧСС';
COMMENT ON COLUMN public."newborn_apgar_criteria_heart_rate".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_heart_rate".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_heart_rate".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_heart_rate" ("id", "description", "point") VALUES
  ('1', '0', '0'),
  ('2', 'Меньше 100 в минуту', '1'),
  ('3', 'Больше 100 в минуту', '2');