CREATE TABLE IF NOT EXISTS "glasgow_coma_scale_newborns" (
  "id" SERIAL PRIMARY KEY,
  "type" VARCHAR(20) NOT NULL,
  "action" VARCHAR(35) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."glasgow_coma_scale_newborns" IS 'Шкала Глазго (Glasgow Coma Scale) - Грудные дети (до 1 года)';
COMMENT ON COLUMN public."glasgow_coma_scale_newborns".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."glasgow_coma_scale_newborns".type IS 'Тип';
COMMENT ON COLUMN public."glasgow_coma_scale_newborns".action IS 'Действие';
COMMENT ON COLUMN public."glasgow_coma_scale_newborns".point IS 'Балл';

INSERT INTO "glasgow_coma_scale_newborns" ("type", "action", "point") VALUES
  ('Открывание глаз', 'Произвольное', '4'),
  ('Открывание глаз', 'На звук', '3'),
  ('Открывание глаз', 'На боль', '2'),
  ('Открывание глаз', 'Отсутствует', '1'),
  ('Речевая реакция', 'Гулит, улыбвается или недоволен', '5'),
  ('Речевая реакция', 'Эпизодический крик, плач спонтанно', '4'),
  ('Речевая реакция', 'Крик и/или плач', '3'),
  ('Речевая реакция', 'Стон', '2'),
  ('Речевая реакция', 'Отсутствует', '1'),
  ('Двигательная реакция', 'Выполняет команды', '6'),
  ('Двигательная реакция', 'Локализует боль', '5'),
  ('Двигательная реакция', 'Отдергивает конечность на боль', '4'),
  ('Двигательная реакция', 'Тоническое сгибание', '3'),
  ('Двигательная реакция', 'Тоническое разгибание', '2'),
  ('Двигательная реакция', 'Отсутствует', '1');