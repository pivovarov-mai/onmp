CREATE TABLE IF NOT EXISTS "size_of_laryngeal_tube" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "patient_parameters" VARCHAR(35) NOT NULL,
  "tube_size" REAL NOT NULL,
  "tube_connector_color" VARCHAR(10) NOT NULL
);

COMMENT ON TABLE public."size_of_laryngeal_tube" IS 'Соответствие размеров ларннгеальных трубок параметрам пациента';
COMMENT ON COLUMN public."size_of_laryngeal_tube".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."size_of_laryngeal_tube".patient_parameters IS 'Параметры пациента';
COMMENT ON COLUMN public."size_of_laryngeal_tube".tube_size IS 'Размер трубки';
COMMENT ON COLUMN public."size_of_laryngeal_tube".tube_connector_color IS 'Цвет коннектора трубки';

INSERT INTO "size_of_laryngeal_tube" ("id", "patient_parameters", "tube_size", "tube_connector_color") VALUES
  ('1', 'Новорожденные, весом менее 5 кг', '0', 'Прозрачный'),
  ('2', 'Дети, весом от 5 до 12 кг', '1', 'Белый'),
  ('3', 'Дети, весом от 12 до 35 кг', '2', 'Зеленый'),
  ('4', 'Дети, ростом от 125 до 150 см', '2.5', 'Оранжевый'),
  ('5', 'Взрослые, ростом менее 150 см', '3', 'Желтый'),
  ('6', 'Взрослые, ростом от 155 до 180 см', '4', 'Красный'),
  ('7', 'Взрослые, ростом более 180 см', '5', 'Фиолетовый');