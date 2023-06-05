using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OnmpApp.Database;
using OnmpApp.Helpers;
using OnmpApp.Models.Database;

namespace OnmpApp.Services;

public static class FullCardService
{
    public static async Task<bool> Update(FullCard card)
    {
        try
        {
            return await FullCardTable.Update(card);
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

    public static async Task<FullCard> Get(int id)
    {
        try
        {
            return await FullCardTable.Get(id);
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }
        return null;
    }

    public static async Task<bool> Remove(int id)
    {
        try
        {
            return await FullCardTable.Remove(id);
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
