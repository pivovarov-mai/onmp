CREATE TABLE IF NOT EXISTS "status_rating_scale_interpretation" (
  "id" SERIAL PRIMARY KEY,
  "point" INTEGER NOT NULL,
  "sign" VARCHAR(60) NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_interpretation" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Интерпретация)';
COMMENT ON COLUMN public."status_rating_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_interpretation".point IS 'Балл';
COMMENT ON COLUMN public."status_rating_scale_interpretation".sign IS 'Признак';

INSERT INTO "status_rating_scale_interpretation" ("point", "sign") VALUES
  ('0', 'Отсутствие клинических признаков сердечной недостаточности'),
  ('1', 'I ФК сердечной недостаточности'),
  ('2', 'I ФК сердечной недостаточности'),
  ('3', 'I ФК сердечной недостаточности'),
  ('4', 'II ФК сердечной недостаточности'),
  ('5', 'II ФК сердечной недостаточности'),
  ('6', 'II ФК сердечной недостаточности'),
  ('7', 'III ФК сердечной недостаточности'),
  ('8', 'III ФК сердечной недостаточности'),
  ('9', 'III ФК сердечной недостаточности'),
  ('10', 'IV ФК сердечной недостаточности'),
  ('11', 'IV ФК сердечной недостаточности'),
  ('12', 'IV ФК сердечной недостаточности'),
  ('13', 'IV ФК сердечной недостаточности'),
  ('14', 'IV ФК сердечной недостаточности'),
  ('15', 'IV ФК сердечной недостаточности'),
  ('16', 'IV ФК сердечной недостаточности'),
  ('17', 'IV ФК сердечной недостаточности'),
  ('18', 'IV ФК сердечной недостаточности'),
  ('19', 'IV ФК сердечной недостаточности'),
  ('20', 'IV ФК сердечной недостаточности');