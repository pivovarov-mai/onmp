CREATE TABLE IF NOT EXISTS "norms_in_children" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "age" VARCHAR(15) NOT NULL,
  "weight" VARCHAR(7) NOT NULL,
  "respiratory_rate" VARCHAR(7) NOT NULL,
  "heart_rate" VARCHAR(9) NOT NULL,
  "arterial_pressure" VARCHAR(9) NOT NULL
);

COMMENT ON TABLE public."norms_in_children" IS 'Нормы ЧД, ЧСС, АД у детей (в покое)';
COMMENT ON COLUMN public."norms_in_children".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."norms_in_children".age IS 'Возраст';
COMMENT ON COLUMN public."norms_in_children".weight IS 'Вес в кг';
COMMENT ON COLUMN public."norms_in_children".respiratory_rate IS 'ЧД - частота дыхания';
COMMENT ON COLUMN public."norms_in_children".heart_rate IS 'ЧСС - частота сердечных сокращений';
COMMENT ON COLUMN public."norms_in_children".arterial_pressure IS 'АД - артериальное давление';

INSERT INTO "norms_in_children" ("id", "age", "weight", "respiratory_rate", "heart_rate", "arterial_pressure") VALUES
  ('1', 'Новорожденные', '3,5', '40-60', '130-140', '70/40'),
  ('2', '3 месяца', '5', '35-40', '120-130', '85/40'),
  ('3', '6 месяцев', '7', '33-35', '120-125', '90/55'),
  ('4', '1 год', '10', '30-32', '120', '92/56'),
  ('5', '2 года', '12', '26-30', '110-115', '94/56'),
  ('6', '4 года', '16', '25-26', '100-105', '98/56'),
  ('7', '5 лет', '19', '25-26', '100', '100/58'),
  ('8', '6 лет', '20', '25', '90-95', '100/60'),
  ('9', '8 лет', '25', '22-24', '80-85', '100/65'),
  ('10', '10 лет', '30', '20-22', '78-80', '105/70'),
  ('11', '12 лет', '33-35', '18-20', '75-82', '110/70'),
  ('12', '14 лет', 'до 45', '16-18', '72-78', '120/70');