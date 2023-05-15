CREATE TABLE IF NOT EXISTS "acute_respiratory_failure" (
  "id" SERIAL PRIMARY KEY,
  "state" VARCHAR(7) NOT NULL,
  "consciousness" VARCHAR(40) NOT NULL,
  "skin" VARCHAR(30) NOT NULL,
  "arterial_pressure" VARCHAR(30) NOT NULL,
  "heart_rate" VARCHAR(35) NOT NULL,
  "respiratory_rate" VARCHAR(12) NOT NULL,
  "spo2" VARCHAR(7) NOT NULL
);

COMMENT ON TABLE public."acute_respiratory_failure" IS 'Острая дыхательная недостаточность (Кассиль В.Л. 2004 г.)';
COMMENT ON COLUMN public."acute_respiratory_failure".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."acute_respiratory_failure".state IS 'Состояние';
COMMENT ON COLUMN public."acute_respiratory_failure".consciousness IS 'Сознание';
COMMENT ON COLUMN public."acute_respiratory_failure".skin IS 'Кожные покровы';
COMMENT ON COLUMN public."acute_respiratory_failure".arterial_pressure IS 'АД - артериальное давление';
COMMENT ON COLUMN public."acute_respiratory_failure".heart_rate IS 'ЧСС - частота сердечных сокращений';
COMMENT ON COLUMN public."acute_respiratory_failure".respiratory_rate IS 'ЧД - частота дыхания';
COMMENT ON COLUMN public."acute_respiratory_failure".spo2 IS 'SpO2 при O2 терапии';

INSERT INTO "acute_respiratory_failure" ("state", "consciousness", "skin", "arterial_pressure", "heart_rate", "respiratory_rate", "spo2") VALUES
  ('Норма', 'Ясное', 'Обычной окраски', 'Норма', 'Норма', '12-16', '96-99'),
  ('ОДН I', 'Ясное', 'Бледность, умеренный цианоз', 'Норма, умеренная гипертензия', ' 100-110', '14-20', '92-95'),
  ('ОДН II', 'Возможно возбуждение, агрессивность', 'Цианоз', 'Умеренная гипертензия', '110-120', '20-30', '90-92'),
  ('ОДН III', 'Спутанность, оглушение', 'Выраженный цианоз', 'ГИПЕРтензия', '120-140', '30-40', '85-90'),
  ('ОДН IV', 'Гипоксическая кома, судороги, мидриаз', 'Мраморный цианоз', 'ГИПОтензия', '> 140 или < 60, возможна аритмия', '> 40 или < 8', '85');