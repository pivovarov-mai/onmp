using Microsoft.Maui.ApplicationModel.Communication;
using Newtonsoft.Json.Linq;
using OnmpApp.Database;
using OnmpApp.Helpers;
using OnmpApp.Models.Database;
using OnmpApp.Properties;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Services;

public static class InitService
{
    public static async Task LoadCatalogNames()
    {
        try
        {
            using var client = new HttpClient();
            HttpResponseMessage response = new();

            for (int i = 0; i < 3; i++)
            {
                if(i == 0)
                   response = await client.GetAsync($"{Settings.ApiAddress}/diagnoses/show_all_diagnoses/");
                else if (i == 1)
                    response = await client.GetAsync($"{Settings.ApiAddress}/diseases/show_all_diseases/");
                else if (i == 2)
                    response = await client.GetAsync($"{Settings.ApiAddress}/medicines/show_all_medicines/");

                var responseContent = await response.Content.ReadAsStringAsync();

                if (response.IsSuccessStatusCode)
                {
                    dynamic json = JArray.Parse(responseContent);

                    foreach(var item in json)
                    {
                        if(item == null)
                            continue;

                        string name = item.Value.ToString();
                        if(await CatalogTable.Get(name) == null)
                            await CatalogTable.Insert(name, (CatalogType)i);
                    }
                }
                else
                {
                    var error = JObject.Parse(responseContent)["error"].ToString();
                    throw new Exception($"{error}");
                }
            }
            
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"Ошибка: {0}", ex.Message);
#endif
            ToastHelper.Show($"Ошибка: {ex.Message}");
        }
    }

}
