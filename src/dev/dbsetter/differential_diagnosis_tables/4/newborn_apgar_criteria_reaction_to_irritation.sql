CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_reaction_to_irritation" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(55) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_reaction_to_irritation" IS 'Критерии оценки новорождённого по шкале Апгар - Реакция на фарингеальный катетер (на раздражение)';
COMMENT ON COLUMN public."newborn_apgar_criteria_reaction_to_irritation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_reaction_to_irritation".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_reaction_to_irritation".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_reaction_to_irritation" ("description", "point") VALUES
  ('Реакция отсутствует', '0'),
  ('Гримаса', '1'),
  ('Хорошо выражена (крик, кашель, чихание, громкий плач)', '2');