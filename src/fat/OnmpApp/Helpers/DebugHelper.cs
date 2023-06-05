using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Helpers;


public static class DebugHelper
{
    public static async Task<T> TryCatch<T>(Func<Task<T>> func)
    {
        try
        {
            return await func();
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
            return default(T);
        }
    }
}
