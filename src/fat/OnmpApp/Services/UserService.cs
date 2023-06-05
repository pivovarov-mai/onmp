using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Maui.ApplicationModel.Communication;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using OnmpApp.Database;
using OnmpApp.Helpers;
using OnmpApp.Properties;

namespace OnmpApp.Services;

public static class UserService
{
    public static async Task<bool> Authenticate(string email, string password)
    {
        try
        {
            using var client = new HttpClient();
            var json = new JObject
            {
                ["email"] = email,
                ["password"] = password,
            };

            var content = new StringContent(json.ToString(), Encoding.UTF8, "application/json");

            var response = await client.PostAsync($"{Settings.ApiAddress}/account/token/", content);
            var responseContent = await response.Content.ReadAsStringAsync();

            if (response.IsSuccessStatusCode)
            {
                var token = JObject.Parse(responseContent)["token"].ToString();
                Settings.Token = token;

                await UserTable.Insert(email);

                return true;
            }

            var error = JObject.Parse(responseContent)["error"].ToString();
            if(error == "Подтвердите email")
            {
                bool answer = await Application.Current.MainPage.DisplayAlert("Ошибка", "У Вас неподтвержденный почтовый адрес. Отправить письмо для подтверждения снова?", "Да", "Нет");
                if (answer)
                {
                    if(await ResendEmail(email))
                    {
                        ToastHelper.Show("Подтверждение отправлено на почту");
                    }
                }

                return false;

            }
            throw new Exception($"{error}");
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"Ошибка: {0}", ex.Message);
#endif
            ToastHelper.Show($"Ошибка: {ex.Message}");
        }

        return false;
    }

    public static async Task<bool> ResendEmail(string email)
    {
        try
        {
            using var client = new HttpClient();
            var json = new JObject
            {
                ["email"] = email,
            };

            var content = new StringContent(json.ToString(), Encoding.UTF8, "application/json");

            var response = await client.PostAsync($"{Settings.ApiAddress}/account/resend_mail/", content);
            var responseContent = await response.Content.ReadAsStringAsync();

            if (response.IsSuccessStatusCode)
            {
                return true;
            }

            var error = JObject.Parse(responseContent)["error"].ToString();
            throw new Exception($"{error}");
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"Ошибка: {0}", ex.Message);
#endif
            ToastHelper.Show($"Ошибка: {ex.Message}");
        }

        return false;
    }

    public static async Task<bool> Register(string email, string password, string first_name, string last_name, string middle_name)
    {
        try
        {
            using var client = new HttpClient();
            var json = new JObject
            {
                ["email"] = email,
                ["password"] = password,
                ["first_name"] = first_name,
                ["last_name"] = last_name,
                ["middle_name"] = middle_name
            };

            var content = new StringContent(json.ToString(), Encoding.UTF8, "application/json");

            var response = await client.PostAsync($"{Settings.ApiAddress}/account/user_create/", content);
            var responseContent = await response.Content.ReadAsStringAsync();

            if (response.IsSuccessStatusCode)
            {
                _ = await UserTable.Insert(email);
                return true;
            }

            var errorContent = JsonConvert.DeserializeObject<Dictionary<string, List<string>>>(responseContent);
            if (errorContent.TryGetValue("email", out var value))
            {
                var emailErrors = string.Join(", ", value);
                throw new Exception($"{emailErrors}");
            }
            else if (errorContent.TryGetValue("password", out var value1))
            {
                var passwordErrors = string.Join(", ", value1);
                throw new Exception($"{passwordErrors}");
            }
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"Ошибка: {0}", ex.Message);
#endif
            ToastHelper.Show($"Ошибка: {ex.Message}");
        }

        return false;
    }

    public static async Task<int> GetId(string email)
    {
        try
        {
            return await UserTable.GetId(email);
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"Ошибка: {0}", ex.Message);
#endif
            ToastHelper.Show($"Ошибка: {ex.Message}");
        }

        return -1;
    }
}