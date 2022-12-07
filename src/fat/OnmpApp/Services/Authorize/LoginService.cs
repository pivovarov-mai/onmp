using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using OnmpApp.Data;
using OnmpApp.Helpers;
using OnmpApp.Models;

namespace OnmpApp.Services.Authorize;

public class LoginService
{

    public LoginService() { }

    public async Task<bool> AuthenticateUser(string email, string password)
    {
        try
        {
            return await Database.UserDataValid(email, password);
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }
        
        return false;
    }
}
