CREATE TABLE IF NOT EXISTS "coma_scale_eye_reactions" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "sign" VARCHAR(60) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."coma_scale_eye_reactions" IS 'Шкала комы FOUR - Глазные реакции (E)';
COMMENT ON COLUMN public."coma_scale_eye_reactions".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."coma_scale_eye_reactions".sign IS 'Признак';
COMMENT ON COLUMN public."coma_scale_eye_reactions".points IS 'Баллы';

INSERT INTO "coma_scale_eye_reactions" ("id", "sign", "points") VALUES
  ('1', 'Глаза открыты слежение и мигание по команде', '4'),
  ('2', 'Глаза открыты, но нет слежения', '3'),
  ('3', 'Глаза закрыты, открываются на громкий звук, но слежения нет', '2'),
  ('4', 'Глаза закрыты, открываются на боль, но слежения нет', '1'),
  ('5', 'Глаза остаются закрытыми в ответ на боль', '0');