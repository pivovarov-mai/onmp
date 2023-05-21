const enum Measure = {
  Mg = 'mg',
  Ml = 'ml',
  ME = 'ME',
  Blob = 'blob'
}

const enum CalculationParametr = {
  Age = 'age',
  Weight = 'weight'
}

interface DosesAtDiagnosis {
 diagnosis: string;
 dose: number;
}

interface Medication {
 id: number;
 name: string; // название на латыни в именительном падеже
 nameGenitiveCase: string; // название на латыни в родительном падеже
 measure: Measure; // мера дозировки препарата
 adultDosage: ReadonlyArray<DosesAtDiagnosis>; // взрослые дозировки
 childDosage: ReadonlyArray<DosesAtDiagnosis>; // детские дозировки
 childCalculationParametr: CalculationParametr; // физиологический параметр, по которому будет производиться расчет детской дозировки
 contraindications: ReadonlyArray<string>; // список противопоказаний
}