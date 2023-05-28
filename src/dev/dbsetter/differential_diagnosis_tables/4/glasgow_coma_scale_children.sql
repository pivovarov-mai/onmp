CREATE TABLE IF NOT EXISTS "glasgow_coma_scale_children" (
  "id" SERIAL PRIMARY KEY,
  "type" VARCHAR(20) NOT NULL,
  "action" VARCHAR(30) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."glasgow_coma_scale_children" IS 'Шкала Глазго (Glasgow Coma Scale) - Дети от 1 до 4 лет';
COMMENT ON COLUMN public."glasgow_coma_scale_children".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."glasgow_coma_scale_children".type IS 'Тип';
COMMENT ON COLUMN public."glasgow_coma_scale_children".action IS 'Действие';
COMMENT ON COLUMN public."glasgow_coma_scale_children".point IS 'Балл';

INSERT INTO "glasgow_coma_scale_children" ("type", "action", "point") VALUES
  ('Открывание глаз', 'Произвольное', '4'),
  ('Открывание глаз', 'На звук', '3'),
  ('Открывание глаз', 'На боль', '2'),
  ('Открывание глаз', 'Отсутствует', '1'),
  ('Речевая реакция', 'Речевая реакция по возрасту', '5'),
  ('Речевая реакция', 'Бессвязная речевая продукция', '4'),
  ('Речевая реакция', 'Крик и/или плач', '3'),
  ('Речевая реакция', 'Стон', '2'),
  ('Речевая реакция', 'Отсутствует', '1'),
  ('Двигательная реакция', 'Выполняет команды', '6'),
  ('Двигательная реакция', 'Локализует боль', '5'),
  ('Двигательная реакция', 'Отдергивает конечность на боль', '4'),
  ('Двигательная реакция', 'Тоническое сгибание', '3'),
  ('Двигательная реакция', 'Тоническое разгибание', '2'),
  ('Двигательная реакция', 'Отсутствует', '1');