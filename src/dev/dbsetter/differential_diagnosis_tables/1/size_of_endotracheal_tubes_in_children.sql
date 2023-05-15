CREATE TABLE IF NOT EXISTS "size_of_endotracheal_tubes_in_children" (
  "id" SERIAL PRIMARY KEY,
  "age" VARCHAR(15) NOT NULL,
  "weight" VARCHAR(5) NOT NULL,
  "inner_diameter" REAL NOT NULL,
  "insertion_depth" REAL NOT NULL,
  "suction_catheter" INTEGER NOT NULL
);

COMMENT ON TABLE public."size_of_endotracheal_tubes_in_children" IS 'Размеры эндотрахеальных трубок у детей';
COMMENT ON COLUMN public."size_of_endotracheal_tubes_in_children".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."size_of_endotracheal_tubes_in_children".age IS 'Возраст';
COMMENT ON COLUMN public."size_of_endotracheal_tubes_in_children".weight IS 'Вес в кг';
COMMENT ON COLUMN public."size_of_endotracheal_tubes_in_children".inner_diameter IS 'Внутренний диаметр, в мм';
COMMENT ON COLUMN public."size_of_endotracheal_tubes_in_children".insertion_depth IS 'Глубина введения, в см';
COMMENT ON COLUMN public."size_of_endotracheal_tubes_in_children".suction_catheter IS 'Катетер для аспирации FG';

INSERT INTO "size_of_endotracheal_tubes_in_children" ("age", "weight", "inner_diameter", "insertion_depth", "suction_catheter") VALUES
  ('Новорожденные', '< 0,7', '2', '5', '5'),
  ('Новорожденные', '< 1', '2.5', '5.5', '5'),
  ('Новорожденные', '2', '3', '6', '6'),
  ('Новорожденные', '3', '3.5', '8.5', '7'),
  ('Новорожденные', '3.5', '3.5', '9', '8'),
  ('6 месяцев', '6', '3.5', '10', '8'),
  ('1 год', '10', '4', '11', '8'),
  ('2 года', '12', '4.5', '12', '8'),
  ('3 года', '14', '4.5', '13', '8'),
  ('4 года', '16', '5', '14', '10'),
  ('6 лет', '20', '5.5', '15', '10'),
  ('8 лет', '24', '6', '16', '10'),
  ('10 лет', '30', '6.5', '17', '12'),
  ('12 лет', '38', '7', '18', '12'),
  ('13-14 лет', '50', '7.5', '19', '12');