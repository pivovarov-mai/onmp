CREATE TABLE IF NOT EXISTS "glasgow_coma_scale_adults" (
  "id" SERIAL PRIMARY KEY,
  "type" VARCHAR(20) NOT NULL,
  "action" VARCHAR(30) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."glasgow_coma_scale_adults" IS 'Шкала Глазго (Glasgow Coma Scale) - Взрослые и детей старше 4 лет';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".type IS 'Тип';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".action IS 'Действие';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".point IS 'Балл';

INSERT INTO "glasgow_coma_scale_adults" ("type", "action", "point") VALUES
  ('Открывание глаз', 'Произвольное', '4'),
  ('Открывание глаз', 'На речь', '3'),
  ('Открывание глаз', 'На боль', '2'),
  ('Открывание глаз', 'Отсутствует', '1'),
  ('Речевая реакция', 'Ориентированная', '5'),
  ('Речевая реакция', 'Спутанная', '4'),
  ('Речевая реакция', 'Неподходящие слова', '3'),
  ('Речевая реакция', 'Малопонятные звуки', '2'),
  ('Речевая реакция', 'Отсутствует', '1'),
  ('Двигательная реакция', 'Выполняет команды', '6'),
  ('Двигательная реакция', 'Локализует боль', '5'),
  ('Двигательная реакция', 'Отдергивает конечность на боль', '4'),
  ('Двигательная реакция', 'Тоническое сгибание', '3'),
  ('Двигательная реакция', 'Тоническое разгибание', '2'),
  ('Двигательная реакция', 'Отсутствует', '1');