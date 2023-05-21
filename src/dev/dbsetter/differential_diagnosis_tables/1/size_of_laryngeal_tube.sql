CREATE TABLE IF NOT EXISTS "size_of_laryngeal_tube" (
  "id" SERIAL PRIMARY KEY,
  "patient_parameters" VARCHAR(35) NOT NULL,
  "tube_size" REAL NOT NULL,
  "tube_connector_color" VARCHAR(10) NOT NULL
);

COMMENT ON TABLE public."size_of_laryngeal_tube" IS 'Соответствие размеров ларннгеальных трубок параметрам пациента';
COMMENT ON COLUMN public."size_of_laryngeal_tube".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."size_of_laryngeal_tube".patient_parameters IS 'Параметры пациента';
COMMENT ON COLUMN public."size_of_laryngeal_tube".tube_size IS 'Размер трубки';
COMMENT ON COLUMN public."size_of_laryngeal_tube".tube_connector_color IS 'Цвет коннектора трубки';

INSERT INTO "size_of_laryngeal_tube" ("patient_parameters", "tube_size", "tube_connector_color") VALUES
  ('Новорожденные, весом менее 5 кг', '0', 'Прозрачный'),
  ('Дети, весом от 5 до 12 кг', '1', 'Белый'),
  ('Дети, весом от 12 до 35 кг', '2', 'Зеленый'),
  ('Дети, ростом от 125 до 150 см', '2.5', 'Оранжевый'),
  ('Взрослые, ростом менее 150 см', '3', 'Желтый'),
  ('Взрослые, ростом от 155 до 180 см', '4', 'Красный'),
  ('Взрослые, ростом более 180 см', '5', 'Фиолетовый');