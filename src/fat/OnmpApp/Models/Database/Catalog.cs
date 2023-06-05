using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using SQLite;

namespace OnmpApp.Models.Database;

[Table("Catalogs")]
public class Catalog
{
    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }

    // Название карты 
    [NotNull, Indexed(Name = "name_idx", Order = 1)]
    public string Name { get; set; }

    public string Text { get; set; }

    [NotNull, Indexed(Name = "lower_name_idx", Order = 1)]

    public string LowerName { get; set; }

    public CatalogType ElType { get; set; }

    [Ignore]
    public FormattedString FormattedText
    {
        get
        {
            return ElType switch
            {
                CatalogType.Diagnose => ParseDiangose(Text),
                CatalogType.Disease => ParseDisease(Text),
                CatalogType.Medicine => ParseMedicine(Text),
                _ => new FormattedString(),
            };
        }
    }

    private FormattedString ParseDiangose(string json)
    {
        if (string.IsNullOrEmpty(json))
            return null;

        dynamic data = JsonConvert.DeserializeObject(json);

        var formattedString = new FormattedString();

        foreach (var subItem in data)
        {
            string subKey = subItem.Name;
            dynamic subValue = subItem.Value;

            var subTitleSpan = new Span
            {
                Text = subKey + '\n',
                FontAttributes = FontAttributes.Bold,
                TextDecorations = TextDecorations.Underline,
                FontSize = new Span().FontSize + 2
            };
            formattedString.Spans.Add(subTitleSpan);

            if (subValue == null)
                continue;

            // OMPS
            if (subValue.ContainsKey("omps") && subValue["omps"] != null)
            {
                formattedString.Spans.Add(new Span { Text = "Объем мед. помощи:" + '\n' });
                foreach (var omp in subValue["omps"])
                {
                    if (omp.Value == null)
                        continue;
                    formattedString.Spans.Add(new Span { Text = "\t\u25cf " + omp.ToString() + '\n' });
                }


                formattedString.Spans.Add(new Span { Text = "\n" });
            }

            // tactics
            if (subValue.ContainsKey("tactics") && subValue["tactics"] != null)
            {
                formattedString.Spans.Add(new Span { Text = "Тактика действий:" + '\n' });
                List<dynamic> tacticsList = subValue["tactics"].ToObject<List<dynamic>>();
                tacticsList = tacticsList.OrderBy(x => x).ToList();
                foreach (var tactic in tacticsList)
                {
                    if(tactic == null)
                        continue;
                    formattedString.Spans.Add(new Span { Text = '\t' + tactic + '\n' });
                }

                formattedString.Spans.Add(new Span { Text = "\n" });
            }

            // sub_diagnoses
            if (subValue.ContainsKey("sub_diagnoses") && subValue["sub_diagnoses"] != null)
            {
                formattedString.Spans.Add(new Span { Text = "Поддиагнозы:" + '\n' });

                foreach (var subDiag in subValue["sub_diagnoses"])
                {
                    string subsubKey = subDiag.Name;
                    dynamic subsubValue = subDiag.Value;
                    formattedString.Spans.Add(new Span { Text = "\t\u25cf " + subsubKey.ToString() + '\n' });

                    if (subsubValue == null)
                        continue;
                    //sub_diag_omps
                    if (subsubValue.ContainsKey("sub_diag_omps"))
                    {
                        foreach (var omp in subsubValue["sub_diag_omps"])
                        {
                            if (omp.Value == null)
                                continue;

                            formattedString.Spans.Add(new Span { Text = "\t\t\u25C6 " + omp.Value.ToString() + '\n' });
                        }

                    }

                    //sub_diag_recommendation
                    if (subsubValue.ContainsKey("sub_diag_recommendation") && subsubValue["sub_diag_recommendation"].Value.ToString() != "Рекомендаций нет")
                    {
                        formattedString.Spans.Add(new Span { Text = "\tРекомендация поддиагноза: " + subsubValue["sub_diag_recommendation"].Value.ToString() + '\n' });
                    }
                    
                }

                formattedString.Spans.Add(new Span { Text = "\n" });

            }

            // diagnose_recommendation
            if (subValue.ContainsKey("diagnose_recommendation") && subValue["diagnose_recommendation"] != null
                && subValue["diagnose_recommendation"].Value.ToString() != "Рекомендаций нет")
            {
                formattedString.Spans.Add(new Span { Text = "Рекомендация: " + subValue["diagnose_recommendation"].Value.ToString() + '\n' });
            }

            formattedString.Spans.Add(new Span { Text = "\n" });
        }

        return formattedString;
    }

    private FormattedString ParseDisease(string json)
    {
        if (string.IsNullOrEmpty(json))
            return null;

        dynamic data = JsonConvert.DeserializeObject(json);

        var formattedString = new FormattedString();

        // tag
        if(data.ContainsKey("tag") && data["tag"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Группа: " + data["tag"].Value.ToString() + "\n\n" });
        }

        // description
        if(data.ContainsKey("description") && data["description"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Описание: " + data["description"].Value.ToString() + "\n\n" });
        }


        // period
        if(data.ContainsKey("period") && data["period"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Период: " + data["period"].Value.ToString() + "\n\n" });
        }

        //  symptomps
        if(data.ContainsKey("symptomps") && data["symptomps"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Симптомы: " + '\n' });
            foreach (var symptom in data["symptomps"])
            {
                if (symptom.Value == null)
                    continue;
                formattedString.Spans.Add(new Span { Text = "\t\u25cf " + symptom.ToString() + '\n' });
            }

            formattedString.Spans.Add(new Span { Text = "\n" });
        }

        // forms
        if(data.ContainsKey("forms") && data["forms"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Формы: " + '\n' });
            foreach (var form in data["forms"])
            {
                if (form.Value == null)
                    continue;
                formattedString.Spans.Add(new Span { Text = "\t\u25cf " + form.ToString() + '\n' });
            }

            formattedString.Spans.Add(new Span { Text = "\n" });
        }

        // form descriptions
        if(data.ContainsKey("form descriptions") && data["form descriptions"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Описание форм: " + '\n' });
            foreach (var formDesc in data["form descriptions"])
            {
                if (formDesc.Value == null)
                    continue;
                formattedString.Spans.Add(new Span { Text = "\t\u25cf " + formDesc.ToString() + '\n' });
            }

            formattedString.Spans.Add(new Span { Text = "\n" });
        }

        // form symptomps
        if(data.ContainsKey("form symptomps") && data["form symptomps"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Симптомы форм: " + '\n' });
            foreach (var formSymptom in data["form symptomps"])
            {
                if (formSymptom.Value == null)
                    continue;
                formattedString.Spans.Add(new Span { Text = "\t\u25cf " + formSymptom.ToString() + '\n' });
            }

            formattedString.Spans.Add(new Span { Text = "\n" });
        }

        return formattedString;
    }

    private FormattedString ParseMedicine(string json)
    {
        if (string.IsNullOrEmpty(json))
            return null;

        dynamic data = JsonConvert.DeserializeObject(json);

        var formattedString = new FormattedString();

        // genitive
        if(data.ContainsKey("genitive") && data["genitive"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Название в р.п.: " + data["genitive"].Value.ToString() + "\n\n" });
        }

        // unit
        if(data.ContainsKey("unit") && data["unit"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Мера: " + data["unit"].Value.ToString() + "\n\n" });
        }

        //  diagnoses
        if(data.ContainsKey("diagnoses") && data["diagnoses"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Диагнозы: " + '\n' });
            foreach (var diagnose in data["diagnoses"])
            {
                if (diagnose.Value == null)
                    continue;
                string diagKey = diagnose.Name;
                dynamic diagValue = diagnose.Value;
                formattedString.Spans.Add(new Span { Text = "\t\u25cf " + diagKey.ToString() + '\n' });

                if (diagValue == null)
                    continue;

                //adult_dosage
                if(diagValue.ContainsKey("adult_dosage") && diagValue["adult_dosage"] != null)
                {
                    formattedString.Spans.Add(new Span { Text = "\t\tВзрослая дозировка: " + diagValue["adult_dosage"].Value.ToString() + '\n' });
                }

                // child_dosage
                if(diagValue.ContainsKey("child_dosage") && diagValue["child_dosage"] != null)
                {
                    formattedString.Spans.Add(new Span { Text = "\t\tДетская дозировка: " + diagValue["child_dosage"].Value.ToString() + '\n' });
                }
                
            }

            formattedString.Spans.Add(new Span { Text = "\n" });
        }

        // contraindications
        if(data.ContainsKey("contraindications") && data["contraindications"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Противопоказания: " + '\n' });
            foreach (var contraindication in data["contraindications"])
            {
                if (contraindication.Value == null)
                    continue;
                formattedString.Spans.Add(new Span { Text = "\t\u25cf " + contraindication.ToString() + '\n' });
            }

            formattedString.Spans.Add(new Span { Text = "\n" });
        }

        // child_dosage_unit
        if(data.ContainsKey("child_dosage_unit") && data["child_dosage_unit"] != null)
        {
            formattedString.Spans.Add(new Span { Text = "Мера детской дозировки: " + data["child_dosage_unit"].Value.ToString() + "\n\n" });
        }

        return formattedString;
    }
}

public enum CatalogType
{
    Diagnose,
    Disease,
    Medicine
}

public class CatalogShort
{
    public string Name { get; set; }
    public CatalogType ElType { get; set; }

    public bool Loaded { get; set; }
}
