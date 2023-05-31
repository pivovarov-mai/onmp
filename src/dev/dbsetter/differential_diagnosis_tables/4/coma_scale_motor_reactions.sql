CREATE TABLE IF NOT EXISTS "coma_scale_motor_reactions" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "sign" VARCHAR(65) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."coma_scale_motor_reactions" IS 'Шкала комы FOUR - Двигательные реакции (M)';
COMMENT ON COLUMN public."coma_scale_motor_reactions".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."coma_scale_motor_reactions".sign IS 'Признак';
COMMENT ON COLUMN public."coma_scale_motor_reactions".points IS 'Баллы';

INSERT INTO "coma_scale_motor_reactions" ("id", "sign", "points") VALUES
  ('1', 'Выполняет команды (знак отлично, кулак, знак мира)', '3'),
  ('2', 'Локализует боль', '2'),
  ('3', 'Сгибательный ответ на боль', '1'),
  ('4', 'Нет ответа на боль или генерализованный миоклонический эпистатус', '0');