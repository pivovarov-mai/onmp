using OnmpApp.Data;
using OnmpApp.Helpers;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Services.Authorize;

public class RegistrationService
{
    public RegistrationService() { }

    public async Task<bool> RegisterUser(string email, string password)
    {
        try
        {
            if (await Database.UserEmailExists(email))
                return false;

            return await Database.UserCreate(email, password);
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
