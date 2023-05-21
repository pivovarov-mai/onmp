CREATE TABLE IF NOT EXISTS "probability_scale" (
  "id" SERIAL PRIMARY KEY,
  "sign" VARCHAR(60) NOT NULL,
  "points" VARCHAR(3)
);

COMMENT ON TABLE public."probability_scale" IS 'Шкала оценки вероятности ТЭЛА (Revised Geneva Score)';
COMMENT ON COLUMN public."probability_scale".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."probability_scale".sign IS 'Признак';
COMMENT ON COLUMN public."probability_scale".points IS 'Баллы';

INSERT INTO "probability_scale" ("sign", "points") VALUES
  ('Возраст старше 65 лет', '+1'),
  ('Тромбоз глубоких вен или ТЭЛА в анамнезе', '+3'),
  ('Хирургическое вмешательство или травма в течение 1 месяца', '+2'),
  ('Активная злокачественная опухоль', '+2'),
  ('Боль в одной ноге', '+3'),
  ('Кровохарканье', '+2'),
  ('ЧСС - 75-94 в минуту', '+3'),
  ('ЧСС более 95 в минуту', '+5'),
  ('Боль при пальпаци или отек одной из нижних конечностей', '+4');