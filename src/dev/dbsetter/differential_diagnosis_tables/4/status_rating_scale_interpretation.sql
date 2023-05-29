CREATE TABLE IF NOT EXISTS "status_rating_scale_interpretation" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "point" INTEGER NOT NULL,
  "sign" VARCHAR(60) NOT NULL
);

COMMENT ON TABLE public."status_rating_scale_interpretation" IS 'ХСН ШОКС (в модификации Мареева В.Ю.) - Интерпретация)';
COMMENT ON COLUMN public."status_rating_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."status_rating_scale_interpretation".point IS 'Балл';
COMMENT ON COLUMN public."status_rating_scale_interpretation".sign IS 'Признак';

INSERT INTO "status_rating_scale_interpretation" ("id", "point", "sign") VALUES
  ('1', '0', 'Отсутствие клинических признаков сердечной недостаточности'),
  ('2', '1', 'I ФК сердечной недостаточности'),
  ('3', '2', 'I ФК сердечной недостаточности'),
  ('4', '3', 'I ФК сердечной недостаточности'),
  ('5', '4', 'II ФК сердечной недостаточности'),
  ('6', '5', 'II ФК сердечной недостаточности'),
  ('7', '6', 'II ФК сердечной недостаточности'),
  ('8', '7', 'III ФК сердечной недостаточности'),
  ('9', '8', 'III ФК сердечной недостаточности'),
  ('10', '9', 'III ФК сердечной недостаточности'),
  ('11', '10', 'IV ФК сердечной недостаточности'),
  ('12', '11', 'IV ФК сердечной недостаточности'),
  ('13', '12', 'IV ФК сердечной недостаточности'),
  ('14', '13', 'IV ФК сердечной недостаточности'),
  ('15', '14', 'IV ФК сердечной недостаточности'),
  ('16', '15', 'IV ФК сердечной недостаточности'),
  ('17', '16', 'IV ФК сердечной недостаточности'),
  ('18', '17', 'IV ФК сердечной недостаточности'),
  ('19', '18', 'IV ФК сердечной недостаточности'),
  ('20', '19', 'IV ФК сердечной недостаточности'),
  ('21', '20', 'IV ФК сердечной недостаточности');