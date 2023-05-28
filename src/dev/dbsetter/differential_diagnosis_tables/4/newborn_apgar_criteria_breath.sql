CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_breath" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(35) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_breath" IS 'Критерии оценки новорождённого по шкале Апгар - Дыхание';
COMMENT ON COLUMN public."newborn_apgar_criteria_breath".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_breath".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_breath".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_breath" ("description", "point") VALUES
  ('Отсутствует', '0'),
  ('Брадипноэ, дыхание нерегулярное', '1'),
  ('Громкий крик или регулярное дыхание', '2');