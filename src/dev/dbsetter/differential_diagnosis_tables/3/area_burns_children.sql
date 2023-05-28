CREATE TABLE IF NOT EXISTS "area_burns_children" (
  "id" SERIAL PRIMARY KEY,
  "area_affected" VARCHAR(60) NOT NULL,
  "zero_years" REAL NOT NULL,
  "one_year" REAL NOT NULL,
  "five_years" REAL NOT NULL,
  "ten_years" REAL NOT NULL,
  "fifteen_years" REAL NOT NULL
);

COMMENT ON TABLE public."area_burns_children" IS 'Определение площади ожогов у детей (по Lund и Browder)';
COMMENT ON COLUMN public."area_burns_children".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."area_burns_children".area_affected IS 'Область поражения';
COMMENT ON COLUMN public."area_burns_children".zero_years IS '0 лет';
COMMENT ON COLUMN public."area_burns_children".one_year IS '1 год';
COMMENT ON COLUMN public."area_burns_children".five_years IS '5 лет';
COMMENT ON COLUMN public."area_burns_children".ten_years IS '10 лет';
COMMENT ON COLUMN public."area_burns_children".fifteen_years IS '15 лет';

INSERT INTO "area_burns_children" ("area_affected", "zero_years", "one_year", "five_years", "ten_years", "fifteen_years") VALUES
  ('Половина головы', '10', '8.5', '6.5', '5', '4'),
  ('Передняя поверхность шеи', '1', '1', '1', '1', '1'),
  ('Задняя поверхность шеи', '1', '1', '1', '1', '1'),
  ('Передняя поверхность грудной клетки, живот', '18', '18', '18', '18', '18'),
  ('Задняя поверхность грудной клетки, поясничная область', '11', '11', '11', '11', '11'),
  ('Передняя поверхность плеча', '2', '2', '2', '2', '2'),
  ('Задняя поверхность плеча', '2', '2', '2', '2', '2'),
  ('Передняя поверхность предплечья', '1.25', '1.25', '1.25', '1.25', '1.25'),
  ('Задняя поверхность предплечья', '1.25', '1.25', '1.25', '1.25', '1.25'),
  ('Передняя поверхность кисти', '1.25', '1.25', '1.25', '1.25', '1.25'),
  ('Задняя поверхность кисти', '1.25', '1.25', '1.25', '1.25', '1.25'),
  ('Ладонь', '1', '1', '1', '1', '1'),
  ('Промежность', '1', '1', '1', '1', '1'),
  ('Ягодицы', '2.5', '2.5', '2.5', '2.5', '2.5'),
  ('Половина бедра', '2.75', '3.25', '4', '4.5', '4.75'),
  ('Половина голени', '2.25', '2.5', '2.75', '3', '3.25'),
  ('Тыльная поверхность стопы', '1.25', '1.25', '1.25', '1.25', '1.25'),
  ('Подошвенная поверхность стопы', '1.25', '1.25', '1.25', '1.25', '1.25');