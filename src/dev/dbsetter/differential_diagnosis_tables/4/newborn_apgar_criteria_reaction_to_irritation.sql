CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_reaction_to_irritation" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(55) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_reaction_to_irritation" IS 'Критерии оценки новорождённого по шкале Апгар - Реакция на фарингеальный катетер (на раздражение)';
COMMENT ON COLUMN public."newborn_apgar_criteria_reaction_to_irritation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_reaction_to_irritation".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_reaction_to_irritation".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_reaction_to_irritation" ("id", "description", "point") VALUES
  ('1', 'Реакция отсутствует', '0'),
  ('2', 'Гримаса', '1'),
  ('3', 'Хорошо выражена (крик, кашель, чихание, громкий плач)', '2');