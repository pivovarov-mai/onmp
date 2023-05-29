CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_breath" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(35) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_breath" IS 'Критерии оценки новорождённого по шкале Апгар - Дыхание';
COMMENT ON COLUMN public."newborn_apgar_criteria_breath".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_breath".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_breath".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_breath" ("id", "description", "point") VALUES
  ('1', 'Отсутствует', '0'),
  ('2', 'Брадипноэ, дыхание нерегулярное', '1'),
  ('3', 'Громкий крик или регулярное дыхание', '2');