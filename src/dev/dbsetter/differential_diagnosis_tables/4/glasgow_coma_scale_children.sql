CREATE TABLE IF NOT EXISTS "glasgow_coma_scale_children" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "type" VARCHAR(20) NOT NULL,
  "action" VARCHAR(30) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."glasgow_coma_scale_children" IS 'Шкала Глазго (Glasgow Coma Scale) - Дети от 1 до 4 лет';
COMMENT ON COLUMN public."glasgow_coma_scale_children".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."glasgow_coma_scale_children".type IS 'Тип';
COMMENT ON COLUMN public."glasgow_coma_scale_children".action IS 'Действие';
COMMENT ON COLUMN public."glasgow_coma_scale_children".point IS 'Балл';

INSERT INTO "glasgow_coma_scale_children" ("id", "type", "action", "point") VALUES
  ('1', 'Открывание глаз', 'Произвольное', '4'),
  ('2', 'Открывание глаз', 'На звук', '3'),
  ('3', 'Открывание глаз', 'На боль', '2'),
  ('4', 'Открывание глаз', 'Отсутствует', '1'),
  ('5', 'Речевая реакция', 'Речевая реакция по возрасту', '5'),
  ('6', 'Речевая реакция', 'Бессвязная речевая продукция', '4'),
  ('7', 'Речевая реакция', 'Крик и/или плач', '3'),
  ('8', 'Речевая реакция', 'Стон', '2'),
  ('9', 'Речевая реакция', 'Отсутствует', '1'),
  ('10', 'Двигательная реакция', 'Выполняет команды', '6'),
  ('11', 'Двигательная реакция', 'Локализует боль', '5'),
  ('12', 'Двигательная реакция', 'Отдергивает конечность на боль', '4'),
  ('13', 'Двигательная реакция', 'Тоническое сгибание', '3'),
  ('14', 'Двигательная реакция', 'Тоническое разгибание', '2'),
  ('15', 'Двигательная реакция', 'Отсутствует', '1');