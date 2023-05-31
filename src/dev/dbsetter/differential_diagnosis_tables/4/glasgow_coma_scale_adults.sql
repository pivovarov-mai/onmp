CREATE TABLE IF NOT EXISTS "glasgow_coma_scale_adults" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "type" VARCHAR(20) NOT NULL,
  "action" VARCHAR(30) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."glasgow_coma_scale_adults" IS 'Шкала Глазго (Glasgow Coma Scale) - Взрослые и детей старше 4 лет';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".type IS 'Тип';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".action IS 'Действие';
COMMENT ON COLUMN public."glasgow_coma_scale_adults".point IS 'Балл';

INSERT INTO "glasgow_coma_scale_adults" ("id", "type", "action", "point") VALUES
  ('1', 'Открывание глаз', 'Произвольное', '4'),
  ('2', 'Открывание глаз', 'На речь', '3'),
  ('3', 'Открывание глаз', 'На боль', '2'),
  ('4', 'Открывание глаз', 'Отсутствует', '1'),
  ('5', 'Речевая реакция', 'Ориентированная', '5'),
  ('6', 'Речевая реакция', 'Спутанная', '4'),
  ('7', 'Речевая реакция', 'Неподходящие слова', '3'),
  ('8', 'Речевая реакция', 'Малопонятные звуки', '2'),
  ('9', 'Речевая реакция', 'Отсутствует', '1'),
  ('10', 'Двигательная реакция', 'Выполняет команды', '6'),
  ('11', 'Двигательная реакция', 'Локализует боль', '5'),
  ('12', 'Двигательная реакция', 'Отдергивает конечность на боль', '4'),
  ('13', 'Двигательная реакция', 'Тоническое сгибание', '3'),
  ('14', 'Двигательная реакция', 'Тоническое разгибание', '2'),
  ('15', 'Двигательная реакция', 'Отсутствует', '1');